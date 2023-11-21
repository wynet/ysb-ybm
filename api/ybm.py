import requests
from api import config
import operator

def req(url,data):
    cookies = config.read_config_file(".\\config.json")["ybmcookies"]

    headers = {
        'authority': 'www.ybm100.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryEAjdwn2AZdJIGA79',
        # 'cookie': 'Hm_lvt_9f4bfe0c69e174e92f282183ee72bed2=1695691517,1696821089; web_did=%7B%22did%22%3A%20%2209cc6c30-43b6-4f0d-b09b-1757da8be33b%22%7D; isDeviceUpload=1; xyy_principal=114158&MDYxMGZiOTE2NTA5OWM2ZjA4MTEyZWUyNzhjM2RjYTUxMzc5YjZkMg&114158; xyy_last_login_time=1696821238159; xyy=MTE0MTU4JjE3Mzc4MTQ1MTYy; acw_tc=2f624a7916968312161855205e6b5a97e2b2055cb97680c2aec4c2af066170; web_info=%7B%22sid%22%3A%201696831217798%2C%22updated%22%3A%201696831217799%2C%22info%22%3A%200%2C%22superProperty%22%3A%20%22%7B%5C%22channelCode%5C%22%3A%20%5C%22B2B%5C%22%7D%22%2C%22referrerDomain%22%3A%20%22www.ybm100.com%22%2C%22cuid%22%3A%20%22114158%22%7D; JSESSIONID=50BE3EA6FD3299A3D98C2DBE1739A1FE; web_8b5e1b0f250a436e8c6af9871354bfba=%7B%22sid%22%3A%200%2C%22updated%22%3A%200%2C%22info%22%3A%200%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E5%B0%8F%E8%8D%AF%E8%8D%AFio%5C%22%7D%22%7D; Hm_lpvt_9f4bfe0c69e174e92f282183ee72bed2=1696831750',
        'origin': 'https://www.ybm100.com',
        'referer': 'https://www.ybm100.com/search/skuInfo.htm?keyword=%E5%A6%87%E7%82%8E%E6%B4%81',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'terminaltype': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    req = requests.post(url, cookies=cookies, headers=headers,data=data)
    return req
def ybmPostData(data):
    data = '------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="keyword"\r\n\r\n' + data["keywords"] + '\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="categoryFirstId"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="categorySecondId"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="categoryThirdId"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="categoryId"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="manufacturerList"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="shopCodes"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="spec"\r\n\r\n' + data["spec"] + '\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="drugClassificationStr"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="property"\r\n\r\nsmsr.sale_num\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="productTypes"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="highGross"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="tagList"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="isThirdCompany"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="hasStock"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="isAvailableCoupons"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="minPrice"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="maxPrice"\r\n\r\n\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="pageNum"\r\n\r\n1\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="pageSize"\r\n\r\n1000\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="spFrom"\r\n\r\n1\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="requestType"\r\n\r\n1\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="direction"\r\n\r\ndesc\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79\r\nContent-Disposition: form-data; name="type"\r\n\r\n1\r\n------WebKitFormBoundaryEAjdwn2AZdJIGA79--\r\n'
    return str(data)

# 抓取药帮忙数据并进行数据整理
# 返回列表数据
def ybm_data(keywords,spec):
    if not spec:
        specs = ybmPostData({"keywords":keywords,"spec":spec})
    else:
        specsdata = ybmPostData({"keywords":keywords,"spec":""})
        specpost = req("https://www.ybm100.com/pc/search/v1/aggs",specsdata.encode())
        s=[]
        for r in specpost.json()["data"]["aggregations"]["specStats"]:
            if operator.contains(r["key"],spec):
                s.append(r["key"])
        specs = ybmPostData({"keywords":keywords,"spec":",".join(s)})
    # print(",".join(s))
    response = req('https://www.ybm100.com/pc/search/v1/productList',specs.encode())
    response = response.json()['data']['rows']
    # print(response)
    res = []
    for i in response:
        if 'actPt' in i:
            # header = ["产品ID", "公司名称", "产品规格", "阶梯价格", "有效期", "限购或库存", "已售订单", "价格",
            #           "总销量"]
            price = ''.join([f'{value},' for value in i['actPt']['stepPriceShowTexts']])[:-1]
            res.append([i['id'],i['companyName'],i['spec'],price,i['nearEffect'],i['availableQty'],"",i['actPt']['assemblePrice'],i['actPt']['orderNum']])
            # res.append({
            #     "id":i['id'],
            #     "name": i['companyName'],
            #     "spec": i['spec'],
            #     "total": "",
            #     "amount":i['actPt']['orderNum'],
            #     "endtime": i['nearEffect'],
            #     "skunum": i['actPt']['skuStartNum'],
            #     "price": i['actPt']['assemblePrice'],
            #     "price2": ""
            # })
    return res
