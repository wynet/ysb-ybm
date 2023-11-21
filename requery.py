import api.content
from datetime import datetime,timedelta
import pymongo
import pandas
#
# starttime = datetime.datetime.now()
client = pymongo.MongoClient("mongodb://apidata:fmrF8az6b43zr23Y@47.110.40.82:27017/apidata")
db = client['apidata']
mydb = db['api']

data = []
for i in range(4):
    times = datetime.now() - timedelta(days=i)
    times = times.strftime("%Y%m%d")
    data.append(mydb.aggregate([
        {"$match":{"addtime":f"{str(times)}","spec":{ "$regex": "" }}},
        # {"$group": {"_id": "$compname",
        #            "total": {"$sum": "$total"},
        #            "ordernum": {"$sum": "$ordernum"},
        #            "spec":{"$first":"$spec"},
        #            "price2":{"$first":"$price2"},
        #            "addtime":{"$first":"$addtime"},
        #            "count":{"$sum":1}
        #     }
        # },
        {"$project": {"_id":0,"id":1,"compname": 1, "spec": 1, "addtime": 1, "total": 1, "ordernum": 1, 'endtime':1,"price2": 1,"count":1}},
        {"$sort":{"total":-1}}
    ]))

# data = mydb.delete_many({"addtime":"20231110"})
assemble =  []
for i in data:
    for v in i:
        assemble.append(v)
        # print(f'ID:{v["id"]}:{v["compname"]}:{v["spec"]}-{v["addtime"]}:总销量：{v["total"]}  总订单数：{v["ordernum"]},现有链接数量：{v["count"]}')
# print(assemble)
df = pandas.DataFrame(assemble)
# 将addtime字段转换为日期类型
df['addtime'] = pandas.to_datetime(df['addtime'])
# 对数据进行排序
df = df.sort_values(['id', 'addtime'])
# 计算每天每个ID对应的total与前一天的差值
df['diff'] = df.groupby('id')['total'].diff()
# 显示对应的id、compname、spec、price2和差值
df[['id', 'compname', 'spec', 'price2', 'diff','endtime']]
df.to_csv("1.csv")
# print(df)
# mydb = db['api_asse']
# res = mydb.insert_many(assemble)
# print(res)
client.close()
    # pddata.append(i)
    # total += int(i['total'])
    # ordernum += int(i['ordernum'])
# ysb = api.ysb.ysb(data['k'], data['s'], "销量从高到低", self.cookies)
# response = ysb.ysb_data()
# c = api.content.content()
# print(c.func({"i":0,"k":"妇炎洁","s":"380"}))
# js= api.jscode.jscode()
# code=js.start_thread()
# print(code)
# endtime = datetime.datetime.now()
#
# print(f"运行时间：{(endtime - starttime).seconds}秒")