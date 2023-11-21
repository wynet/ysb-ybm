import sys
from api import content
from b2b import Ui_mainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox,QFileDialog
import datetime
import threading

class MyWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("药师帮 药帮忙API")
        self.pushButton.clicked.connect(self.change_text)
        self.action_2.triggered.connect(self.about_text)
        self.action.triggered.connect(self.close)
        self.actions.triggered.connect(self.files)

    def change_text(self):
        iodata = self.comboBox.currentIndex()
        keyword = self.keywords.text()
        spec = self.space.text()
        c = content.content()
        res = c.func({"i":iodata,"k":keyword,"s":spec})
        # print(f"平台：{iodata}，关键词：{keyword}，分类：{spec}")
        # res = content.content({"i":iodata,"k":keyword,"s":spec})
        # function.addcsv(res)
        if res['resut'] == 200:
            QMessageBox.question(self,"通知",f"文件已存入data目录，请查看",QMessageBox.Ok)
        elif res['resut'] ==400:
            QMessageBox.question(self, "通知", f"获取数据失败，请检查输入或联系管理员", QMessageBox.No)
        elif res['resut'] == 401:
            QMessageBox.question(self, "通知", f"获取数据失败，需要前端行为认证，请打开浏览器进行验证", QMessageBox.No)

    def about_text(self):
        QMessageBox.question(self,"关于","本软件只为获取药师帮、药帮忙获取产品数据信息并生成CSV格式表格信息。不能用作其他商用途径。",QMessageBox.Ok)

    def files(self):
        starttime = datetime.datetime.now()
        fileName1,filetype = QFileDialog.getOpenFileName(self,"选取文件","","CSV Files (*.csv)")
        if fileName1 != "":
            c = content.content()
            c.batchMain(fileName1)
        endtime = datetime.datetime.now()
        print(f"运行时间：{(endtime - starttime).seconds}秒")

    def start_thread(self):
        # 让files函数在子线程中运行
        thread = threading.Thread(target=self.files, args=())
        # 下面是设置守护线程：如果在程序中将子线程设置为守护线程，则该子线程会在主线程结束时自动退出
        thread.setDaemon(True)
        thread.start()  # 启动线程

if __name__ == '__main__':
    app = QApplication(sys.argv)

    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec())
