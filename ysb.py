from api import content
import time
import schedule
import list

def files():
    fileName1 = "./keyword.csv"
    c = content.content()
    c.batchMain(fileName1)

def getdata():
    li = list.list("ysb3日数据")
    li.listdata()
    li.toaddcsv()

if __name__ == '__main__':
    print("本程序会在每日上午9.30开始执行爬取“keyword.csv”文件中关键词操作，\n并在9.33分开始生成3日的数据对比表，存放在程序根目录下“ysb3日数据.csv”文件中！！！\n请勿关闭此程序！！！！")
    schedule.every().day.at("09:30").do(files)
    schedule.every().day.at("09:33").do(getdata)
    while True:
        schedule.run_pending()
        time.sleep(1)