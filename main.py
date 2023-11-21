from concurrent.futures import ThreadPoolExecutor
import datetime
from api import function,ysb
import pandas as pd
import execjs

def red_excel(file_path):
    dt = pd.read_csv(file_path,keep_default_na=False).to_dict()
    return dt
# with ThreadPoolExecutor(max_workers=10) as executor:
# 运行程序体
# while True:
    # response = function.content()
if __name__ == "__main__":
    file = red_excel("./keyword.csv")
    starttime = datetime.datetime.now()
    with ThreadPoolExecutor(max_workers=10) as executor:

    # print(file)
        for key in file["关键词"]:
            keyword = file["关键词"][key]
            spec = file["规格"][key]
            resul = executor.map(function.main_content({"i": 0, "k": keyword, "s": spec, "c": code()}))
            print(resul)

    endtime = datetime.datetime.now()
    print(f"运行时间：{(endtime - starttime).seconds}秒")

