import pandas as pd
import datetime
import re
import os
import api.ysb
from api import config,ybm
from concurrent.futures import ThreadPoolExecutor

class content():
    cookies = config.read_config_file("./config.json")["ysbcookies"]

    def func(self,js_data):
        if js_data['i'] == 1:
            response = {"name":"药帮忙"+js_data['k']+js_data['s'],"type":js_data['i'],"data": self.ybmapi(js_data)}
        else:
            response = {"name":"药师帮"+js_data['k']+js_data['s'],"type":js_data['i'],"data": self.ysbapi(js_data)}
        # print(response)
        return self.addcsv(response)

    def ysbapi(self,data):
        ysb = api.ysb.ysb(data['k'], data['s'], "销量从高到低", self.cookies)
        response = ysb.ysb_data()
        # 调取药师帮接口
        # ex1 = input("请输入验证码：")
        # response = ysb.ysb.ysb_data(data['k'], data['s'],code())
        return response

    def ybmapi(self,data):
        # 调取药帮忙接口
        response = ybm.ybm_data(data['k'], data['s'])
        return response

    def batchMain(self,file):
        dt = pd.read_csv(file, keep_default_na=False).to_dict()
        with ThreadPoolExecutor(max_workers=10) as executor:
            for key in dt["关键词"]:
                keyword = dt["关键词"][key]
                spec = dt["规格"][key]
                try:
                    executor.submit(self.func({"i": 0, "k": keyword, "s": spec}))
                    res = {"resut": 200, "code": "ok"}
                except:
                    res = {"resut": 400, "code": "error"}
                # print(resul)
        return res

    # 利用pandas将获取的数据写入csv文件中
    # @data {name:文件名，data:数据}
    def addcsv(self,data):
        repl = r'\d+'
        # header = ["产品ID", "公司名称", "产品规格", "已售订单", "总销量","价格","有效期","限购或库存"]
        header = ["产品ID", "公司名称", "产品规格", "阶梯价格", "有效期", "限购或库存","已售订单","价格","总销量"]
        head = ['产品ID', '公司名称', '价格', '有效期',"已售订单","总销量"]
        date = datetime.datetime.now().strftime('%Y%m%d %H-%M-%S')
        # p = pd.DataFrame(data["data"], columns=header)
        # print(p.loc[:, head])
        #
        # print(data)
        if(data['type']==1):
            padata = data['data']
        else:
            padata = []
            for r in data['data']:
                r.append(list(r[3].values())[0])
                r[3] = ''.join([f'数量：{key}*价格：{value},' for key, value in r[3].items()])[:-1]
                r.append(re.findall(repl, r[len(r)-2]['accumulateAmount'])[0])
                r[len(r)-3] = re.findall(repl, r[len(r)-3]['totalRecord'])[0]
                padata.append(r)

        if not os.path.exists('data'):
            os.mkdir('data')
        else:
            try:
                p = pd.DataFrame(padata, columns=header)
                p.to_csv(".\\data\\" + data['name'] + " 行情" + str(date) + ".csv", index=False)
                return {"resut": 200, "code": "ok"}
            except:
                return {"resut": 400, "code": "error"}