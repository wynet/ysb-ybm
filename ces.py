import pandas as pd
import re

# 去掉中文
def remove_chinese(text):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    return re.sub(pattern, '', text)

# 去掉符号
def remove_chineses(text):
    pattern = re.compile(r'[\W]')
    return re.sub(pattern, '', text)

v = pd.read_csv("C:\\Users\\ASUS\\Desktop\\德康堂.csv")

r = v["单据摘要"].apply(remove_chinese)
r= r.apply(remove_chineses)

v['单据摘要']=r
v.to_csv("C:\\Users\\ASUS\\Desktop\\德康堂2.csv")