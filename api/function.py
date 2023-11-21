import datetime
import pandas as pd

import api.ysbaio
from api import ybm,config
import os
import execjs
from concurrent.futures import ThreadPoolExecutor

# 获取js逆向代码
def code():
    with open("./js/js.js", "r", encoding="utf-8") as f:
        js_code = f.read()
    ctx = execjs.compile(js_code)
    result = ctx.call("codes")
    return result
# 利用pandas将获取的数据写入csv文件中
# @data {name:文件名，data:数据}
def addcsv(data):
    header = ["产品ID", "公司名称", "产品规格", "已售订单", "总销量", "起订量", "价格", "其他价格", "有效期","限购或库存"]
    head = ['产品ID', '公司名称', '总销量', '价格', '有效期']
    date = datetime.datetime.now().strftime('%Y%m%d %H-%M-%S')

    if not os.path.exists('data'):
        os.mkdir('data')
    else:
        try:
            p = pd.DataFrame(data["data"], columns=header)
            p.to_csv(".\\data\\" + data['name'] + " 行情" + str(date) + ".csv", index=False)
            # print(p.loc[:, head])
            return {"resut": 200, "code": "ok"}
        except:
            return {"resut":400,"code":"error"}

def batchMain(file):
    dt = pd.read_csv(file, keep_default_na=False).to_dict()
    with ThreadPoolExecutor(max_workers=10) as executor:
        for key in dt["关键词"]:
            keyword = dt["关键词"][key]
            spec = dt["规格"][key]
            try:
                executor.submit(main_content({"i": 0, "k": keyword, "s": spec}))
                res =  {"resut": 200, "code": "ok"}
            except:
                res =  {"resut": 400, "code": "error"}
            # print(resul)
    return res

# # 获取数据并返回文件名与爬取的数据
# # 返回字典数据
# # return {name：文件名，data：数据}
# def content():
#     i = ['ybm','ysb']
#     iodata = input("请输入查询的平台：")
#
#     if not iodata in i:
#         print('输入错误请重新输入！')
#         iodata = input("请输入查询的平台：")
#
#     keywords = input("请输入关键词：")
#     spac = input("请输入规格：")
#     if iodata == 'ybm':
#         # 调取药帮忙接口
#         response = ybm.ybm_data(keywords, spac)
#     elif iodata == 'ysb':
#         # 调取药师帮接口
#         ex1 = input("请输入验证码：")
#         response = ysb.ysb_data(keywords, spac,ex1)
#     if len(spac) != 0:
#         spac = spac.split()
#     else:
#         spac = "-"
#
#     return {"name":str(iodata + keywords + spac[0]), "data":response}

# 获取数据并返回文件名与爬取的数据
# 返回字典数据
# return {name：文件名，data：数据}
def main_content(data):
    # i = ['ybm','ysb']
    if data['i'] == 1:
        # 调取药帮忙接口
        response = ybm.ybm_data(data['k'], data['s'])
        iodata = "药帮忙"
    elif data['i'] == 0:
        cookies = config.read_config_file(".\\config.json")["ysbcookies"]
        ysb = api.ysb.ysb(data['k'], data['s'], "销量从高到低", cookies)
        response = ysb.ysb_data()
        # 调取药师帮接口
        # ex1 = input("请输入验证码：")
        # response = ysb.ysb.ysb_data(data['k'], data['s'],code())
        iodata = "药师帮"
    if len(data['s']) != 0:
        spac = data['s'].split()
    else:
        spac = "-"

    try:
        addcsv({"name":str(iodata+ data['k'] + spac[0]), "data":response})
        return {"resut":200, "code": "ok"}
    except:
        return {"resut":400,"code":"error"}
