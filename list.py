import pandas as pd
import os
import operator
from tqdm import tqdm
from datetime import datetime,timedelta
import pymongo
import pandas

class list():
    def __init__(self,keyword):
        self.times = datetime.now().strftime("%Y%m%d")
        self.keyword = keyword

    def mongdb(self):
        client = pymongo.MongoClient("mongodb://apidata:fmrF8az6b43zr23Y@47.110.40.82:27017/apidata")
        db = client['apidata']
        mydb = db['api']
        return mydb

    def listdata(self):
        c = []
        file = os.listdir("./data")
        header = ["id", "compname", "spec", "price", "endtime", "count","ordernum","price2","total","addtime"]
        # head = ['产品ID',"产品规格",'公司名称','总销量','价格','有效期']
        for f in tqdm(file):
            if operator.contains(f,str(self.times)):
                # print(f.split("行情")[1].split(" ")[0])
                filetime = datetime.fromtimestamp(os.path.getatime(str("./data/"+f)))
                times = datetime.now() - timedelta(days=0)
                dt = pd.read_csv(f"./data/{f}")
                dt = dt.sort_values(by='总销量',ascending=False)
                # dt = dt.loc[:,head]
                dt = dt[dt["总销量"]>0]
                dt["添加时间"] = f.split("行情")[1].split(" ")[0]
                for i in dt.values.tolist():
                    c.append(dict(zip(header,i)))

        # print(c)
        res = self.mongdb().insert_many(c)
        return res
        # print(res)

    def toaddcsv(self):
        data = []
        for i in range(4):
            times = datetime.now() - timedelta(days=i)
            times = times.strftime("%Y%m%d")
            data.append(self.mongdb().aggregate([
                {"$match": {"addtime": f"{str(times)}", "spec": {"$regex": ""}}},
                # {"$group": {"_id": "$compname",
                #            "total": {"$sum": "$total"},
                #            "ordernum": {"$sum": "$ordernum"},
                #            "spec":{"$first":"$spec"},
                #            "price2":{"$first":"$price2"},
                #            "addtime":{"$first":"$addtime"},
                #            "count":{"$sum":1}
                #     }
                # },
                {"$project": {"_id": 0, "id": 1, "compname": 1, "spec": 1, "addtime": 1, "total": 1, "ordernum": 1,
                              'endtime': 1, "price2": 1, "count": 1}},
                {"$sort": {"total": -1}}
            ]))

        # data = mydb.delete_many({"addtime":"20231110"})
        assemble = []
        for i in data:
            for v in i:
                assemble.append(v)
                # print(f'ID:{v["id"]}:{v["compname"]}:{v["spec"]}-{v["addtime"]}:总销量：{v["total"]}  总订单数：{v["ordernum"]},现有链接数量：{v["count"]}')
        df = pandas.DataFrame(assemble)
        # 将addtime字段转换为日期类型
        df['addtime'] = pandas.to_datetime(df['addtime'])
        # 对数据进行排序
        df = df.sort_values(['id', 'addtime'])
        # 计算每天每个ID对应的total与前一天的差值
        df['diff'] = df.groupby('id')['total'].diff()
        # 显示对应的id、compname、spec、price2和差值
        df[['id', 'compname', 'spec', 'price2', 'diff', 'endtime']]
        df.to_csv(f"{self.keyword}.csv")

#
#
# dt = pd.read_csv("C:\\getb2b\\data\\药师帮养生堂 天然维生素E软胶囊200粒 行情20231102 09-38-52.csv")
# dt2 = pd.read_csv("C:\\getb2b\\data\\药师帮养生堂 天然维生素E软胶囊200粒 行情20231103 10-04-15.csv")
# # dt3 = pd.read_csv("d:/getB2B/data/ysb妇炎洁380ml 行情20231012 23-13-41.csv",encoding="gbk")
# # dt4 = pd.read_csv("d:/getB2B/data/ysb妇炎洁380ml 行情20231013 20-31-24.csv")
#
# head = ['产品ID','公司名称','总销量','价格','有效期']
#
# dt = dt.sort_values(by='总销量',ascending=False)
# dt = dt.loc[:,head]
# dt = dt[dt["总销量"]>0]
# #
# dt2 = dt2.sort_values(by='总销量',ascending=False)
# dt2 = dt2.loc[:,head]
# dt2 = dt2[dt2["总销量"]>0]
#
# # dt3 = dt3.sort_values(by='总销量',ascending=False)
# # dt3 = dt3.loc[:,head]
# # dt3 = dt3[dt3["总销量"]>0]
# #
# # dt4 = dt4.sort_values(by='总销量',ascending=False)
# # dt4 = dt4.loc[:,head]
# # dt4 = dt4[dt4["总销量"]>0]
# # data = pd.concat([dt,dt2]).drop_duplicates(keep=False)
#
# data = dt2.merge(dt,on=["产品ID","公司名称"])
# data["昨日销量"] = data['总销量_x']-data['总销量_y']
# data.to_csv("蓝莓叶黄素.csv", index=False)
# print(data)