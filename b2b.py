# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'b2b.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(632, 343)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.keywords = QtWidgets.QLineEdit(self.centralwidget)
        self.keywords.setEnabled(True)
        self.keywords.setGeometry(QtCore.QRect(210, 99, 251, 31))
        self.keywords.setObjectName("keywords")
        self.space = QtWidgets.QLineEdit(self.centralwidget)
        self.space.setEnabled(True)
        self.space.setGeometry(QtCore.QRect(210, 140, 251, 31))
        self.space.setObjectName("space")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 110, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(170, 150, 54, 12))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 61, 251, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 70, 54, 12))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 190, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox.raise_()
        self.keywords.raise_()
        self.space.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 632, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        mainWindow.setMenuBar(self.menuBar)
        self.actions = QtWidgets.QAction(mainWindow)
        self.actions.setObjectName("actions")
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(mainWindow)
        self.action_2.setObjectName("action_2")
        self.action_token = QtWidgets.QAction(mainWindow)
        self.action_token.setObjectName("action_token")
        self.menu.addAction(self.actions)
        self.menu.addAction(self.action_token)
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.comboBox, self.keywords)
        mainWindow.setTabOrder(self.keywords, self.space)
        mainWindow.setTabOrder(self.space, self.pushButton)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.keywords.setPlaceholderText(_translate("mainWindow", "请输入关键词"))
        self.space.setPlaceholderText(_translate("mainWindow", "请输入规格"))
        self.label.setText(_translate("mainWindow", "关键词："))
        self.label_2.setText(_translate("mainWindow", "规格："))
        self.comboBox.setItemText(0, _translate("mainWindow", "药师帮"))
        self.comboBox.setItemText(1, _translate("mainWindow", "药帮忙"))
        self.label_3.setText(_translate("mainWindow", "选择平台："))
        self.pushButton.setText(_translate("mainWindow", "立即查询"))
        self.menu.setTitle(_translate("mainWindow", "文件"))
        self.menu_2.setTitle(_translate("mainWindow", "帮助"))
        self.actions.setText(_translate("mainWindow", "批量查询"))
        self.action.setText(_translate("mainWindow", "退出"))
        self.action_2.setText(_translate("mainWindow", "关于"))
        self.action_token.setText(_translate("mainWindow", "获取token"))
