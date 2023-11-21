import json
import os
import pandas as pd

# 读取json文件获取配置信息
# 需传入文件地址文件名
def read_config_file(file_path):
    path = os.getcwd()
    with open(path+file_path, 'r') as f:
        config_data = json.load(f)
    return config_data
