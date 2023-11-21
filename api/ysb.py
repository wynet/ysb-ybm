import requests
import operator
import re
from api.jscode import jscode
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ysb():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'rcfp=b5d0dcd92a5d9b0d6510f299a4ecd7b92066; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22565593%22%2C%22first_id%22%3A%2218a88ae03a7ab-09a43488d073be8-26031f51-2073600-18a88ae03a8111b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhODhhZTAzYTdhYi0wOWE0MzQ4OGQwNzNiZTgtMjYwMzFmNTEtMjA3MzYwMC0xOGE4OGFlMDNhODExMWIiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI1NjU1OTMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22565593%22%7D%2C%22%24device_id%22%3A%2218a88ae03a7ab-09a43488d073be8-26031f51-2073600-18a88ae03a8111b%22%7D; __snaker__id=Al3NKRMji30N5fIy; YD00545705772953%3AWM_TID=h9sg15fdXldERAVABAOEzJ0ufrloKdEI; YD00545705772953%3AWM_NI=ZD1BDMBM08rSzifZFIN0FTuoBfgn0mAU%2BoRaBRZDT0RP%2BIYlSB5u1bRGcafRNTxtqp4Uxk%2Be1BnhvOLeZbYFLwEYGIUJJYvXD%2FBIz8LcnPsJ1Fke0nBgdanCIFy28mOBQTk%3D; YD00545705772953%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb3c747f6e782b4c65e83ac8fb2d55b978b9b82d8629487a6b5f35ef2a8abb0fc2af0fea7c3b92a9a9cffa3c747829300d9f159bab7aabbc5438ef08ab5f86582baa98fb367838be590d16b828e96a5d73c9290e5aadc68919efb96b46a9299ad82e55a8e8cb895f47cf88bb88caa6ff39ea289f54590bb9683dc4e90a98bbac643979686baf55488f18eaaf93490bda2b1f242f39aa586b36682b9ac82ed498b9ab7d3bb678d9e9fb5ea37e2a3; gdxidpyhxdE=5B5T5Shx%5CEvhIgAWh9LtUK2PwaU5yv1qNHYolOL%2FHS%2BQ7ZXLxxA%2BH%2Fv7%2B%2F0zoOLOHBzK%2Fk71nGgysuE%2B%2BG6xUPBx0RuG8tq0Xu9WH4guodbQ%2FqmpVbQgcfgHbocZuXTdRDjSgVCAjeJ7l6HjMZWmgX247a1q9m3OA507qY8CmE%5CWapb7%3A1695802004740; Token=e4297351ca5c45579ed118344ebe183f',
        'Origin': 'https://dian.ysbang.cn',
        'Referer': 'https://dian.ysbang.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sentry-trace': 'e1fdea4c0a534876aaac4d02812b037a-a51e5359d3f44040-1',
    }
    url = {
        'view': 'https://dian.ysbang.cn/wholesale-drug/api/teambuy/getMoreRecordsForActivityDetail/v4120',
        'list': 'https://dian.ysbang.cn/wholesale-drug/sales/getWholesaleList/v4270',
        'specs': 'https://dian.ysbang.cn/wholesale-drug/sales/facetWholesaleListBySpecification/v4270'
    }

    def __init__(self,keywords,data,sort,cookies):
        self.keywords = keywords
        self.sort = sort
        self.cookies = cookies
        self.urls = ''

        self.spec = self.specs(data)

    async def areq(self,data):
        async with aiohttp.ClientSession() as session:
            resp = await session.post(
                self.urls,
                cookies=self.cookies,
                headers=self.headers,
                json=data
            )
            result = await resp.json()
            return result

    # request 提交post请求
    def req(self,data):
        session = requests.session()

        response = session.post(
            self.urls,
            cookies=self.cookies,
            headers=self.headers,
            json=data,
        )
        return response.json()

    def json_data(self,data):
        # print(data)
        if data['type'] == 1:
            json_data = {
                'platform': 'pc',
                'version': '5.26.0',
                'ua': 'Chrome118',
                'ex': '',
                'trafficType': 3,
                'ex1': jscode().code(),
                'operationtype': 6,
                'pagesize': 2000,
                'classifyFilter': '',
                'page': 1,
                'searchkey': self.keywords,
                'sort': self.sort,
                'showClassify': False,
                'onlyShowRecentlyPurchased': False,
                'serviceTags': [],
                'provider_filter': '',
                'factoryNames': '',
                'specs': str(self.spec),
                'urlNeedParams': False,
                'purchaseLimitFloor': 0,
                'purchaseLimitFloorList': [],
                'validMonthFloor': 0,
                'validMonthFloorList': [],
                'onlySimpleLoan': 0,
                'token': self.cookies['Token'],
            }
        elif data['type'] == 2:
            json_data = {
                'platform': 'pc',
                'version': '5.26.0',
                'ua': 'Chrome118',
                'ex': '2023-10-7 15:56 drugInfo 10-08 16:31:39 10-08 16:31:39',
                'trafficType': 2,
                'ex1': 'depvk7ux2',
                'pageSize': 100,
                'pageNo': 1,
                'wholesaleId': data.get("wholesaleId"),
                'token': self.cookies["Token"],
            }
        elif data['type'] == 0:
            json_data = {
                'platform': 'pc',
                'version': '5.26.0',
                'ua': 'Chrome118',
                'ex': '',
                'trafficType': 3,
                'ex1': 'depvk7ux2',
                'fetchAll': 1,
                'searchkey': self.keywords,
                'factoryNames': '',
                'provider_filter': '',
                'specs': '[]',
                'operationtype': 6,
                'token': self.cookies["Token"],
            }
        return json_data

    # 接口调用获取当前搜索关键词的产品规格
    # 返回规格列表
    # {data:规格信息}
    def specs(self,data):
        self.urls = self.url['specs']
        spec_data = self.json_data({"type":0})
        response = self.req(spec_data)
        vals = []
        for res in response["data"]:
            # vals.append(res["name"])
            # 获取的列表中和输入规格进行匹配，如有责返回值
            if operator.contains(res['name'], data):
                vals.append(res["name"])
        return vals

    # 接口调用
    # 对抓取的数据进行整理拼接
    # 提供给外部调用
    # 返回列表数据结构，抓取失败返回-1
    def ysb_data(self):
        self.urls = self.url['list']
        json_data = self.json_data({"type":1})
        # list_data = self.req(json_data)
        loop = asyncio.get_event_loop()
        list_data = loop.run_until_complete(self.areq(json_data))
        if list_data['code'] == '40060':
            return {"resut": 401, "code": "error"}
        if not list_data['data'] is None:
            res_data = list_data["data"]["wholesales"]

            vals = []
            wholesaleid = []
            # print(res_data)
            self.urls = self.url['view']
            with ThreadPoolExecutor(max_workers=10) as executor:
                for res in res_data:
                    # print(dict(zip(res['stepCnt'].insert(0,res['step']),res['stepPrice'])))
                    # arr_data['price'] = dict(zip(res['stepCnt'].insert(0,res['step']),res['stepPrice']))
                    result = executor.submit(self.ysbdata,res)
                    id = executor.submit(self.json_data, {'type': 2, 'wholesaleId': res['wholesaleid']})
                    wholesaleid.append(id.result())
                    vals.append(result.result())
            # for res in res_data:
            #     result = self.ysbdata(res)
            #     vals.append(result)
            #     wholesaleid.append(self.json_data({'type': 2, 'wholesaleId': res['wholesaleid']}))
            re = self.Yswholesaleid(wholesaleid)
            for k in range(len(vals)):
                vals[k].append(re[k])
            return vals
        else:
            # 获取数据失败返回-1
            return -1
            # print(" ID:" + str(res['wholesaleid']) + '-------------------')

    def ysbdata(self,data):
        stepCnt = data["stepCnt"]
        stepCnt.insert(0,data["start_amount"])
        price = dict(zip(stepCnt,data['stepPrice']))

        # json_data = self.json_data({'type': 2, 'wholesaleId': data['wholesaleid']})
        # loop = asyncio.get_event_loop()
        # result = loop.run_until_complete(self.areq(json_data))
        vals = [data['wholesaleid'], data['provider_name'], data['specification'], price, data['valid_date'],
                data['max_amount']]
        return vals


    def Yswholesaleid(self,json_data):
        loop = asyncio.get_event_loop()
        task = self.run(json_data)
        result = loop.run_until_complete(task)
        # if result['code'] == "40001":
        return result

    async  def run(self,json_data):
        task_list = []
        for v in json_data:
            task_list.append(self.areq(v))
        result = await asyncio.gather(*task_list)
        results = []
        for res in result:
            results.append(res['data'])
        return results

    def ysbView(self,data):
        repl = r'\d+'
        json_data = self.json_data({'type': 2, 'wholesaleId': data['wholesaleid']})
        # print(json_data)
        # 获取详情页信息
        arr = self.req(json_data)
        # print(data['provider_name'] + '：' + data['specification'] + "  已售" + str(data["data"]['totalRecord']) + "  共售：" + str(data["data"]['accumulateAmount']) + '  价格：' + str(data['minamount']) + '*' + str(data['price']))
        if len(data["providerDisInfo"]) != 0:
            for i in data['providerDisInfo']:
                price2 = i['tagTitle']
        else:
            price2 = "无"
        # print(price2)
        total = re.findall(repl, arr["data"]['totalRecord'])
        Amount = re.findall(repl, arr["data"]['accumulateAmount'])
        vals = [data['wholesaleid'], data['provider_name'], self.spec, total[0], Amount[0],
                     data['minamount'], data['price'], price2, data['valid_date'],data['max_amount']]
        # vals =[data['wholesaleid'], data['provider_name'], data['specification'], total[0], Amount[0],
        #              data['minamount'], data['price'], price2, data['valid_date'],data['max_amount']]

        return vals