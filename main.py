import sys
import numpy as np
import pandas as pd

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from OpenCart import OpenCart


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 301, 51))
        self.label.setObjectName("label")
        self.clickBereg = QtWidgets.QPushButton(self.centralwidget)
        self.clickBereg.setGeometry(QtCore.QRect(400, 240, 181, 41))
        self.clickBereg.setObjectName("clickBereg")
        self.logs = QtWidgets.QListWidget(self.centralwidget)
        self.logs.setGeometry(QtCore.QRect(20, 320, 751, 261))
        self.logs.setObjectName("listView")
        self.shopLoadList = QtWidgets.QPushButton(self.centralwidget)
        self.shopLoadList.setGeometry(QtCore.QRect(210, 240, 181, 41))
        self.shopLoadList.setObjectName("shopLoadList")
        self.apiKey = QtWidgets.QTextEdit(self.centralwidget)
        self.apiKey.setGeometry(QtCore.QRect(30, 70, 351, 41))
        self.apiKey.setObjectName("apiKey")
        self.shopConnection = QtWidgets.QPushButton(self.centralwidget)
        self.shopConnection.setGeometry(QtCore.QRect(330, 130, 171, 41))
        self.shopConnection.setObjectName("shopConnection")
        self.shopURL = QtWidgets.QTextEdit(self.centralwidget)
        self.shopURL.setGeometry(QtCore.QRect(410, 70, 351, 41))
        self.shopURL.setObjectName("shopURL")
        self.loadToShop = QtWidgets.QPushButton(self.centralwidget)
        self.loadToShop.setGeometry(QtCore.QRect(590, 240, 181, 41))
        self.loadToShop.setObjectName("shopLoadList_2")
        self.beta = QtWidgets.QPushButton(self.centralwidget)
        self.beta.setGeometry(QtCore.QRect(20, 240, 181, 41))
        self.beta.setObjectName("beta")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.clickBereg.clicked.connect(open_bereg)
        self.shopConnection.clicked.connect(connection)
        self.shopLoadList.clicked.connect(load_list)
        self.loadToShop.clicked.connect(list_to_shop)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setToolTip(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">OpenCart Shop Controller</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<font size=30>OpenCart Shop controller</font>"))
        self.clickBereg.setText(_translate("MainWindow", "Load Bereg"))
        self.shopLoadList.setText(_translate("MainWindow", "OpenCart goods lost"))
        self.apiKey.setHtml(_translate("MainWindow",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Open Cart API KEY</span></p></body></html>"))
        self.shopConnection.setText(_translate("MainWindow", "Connect to Open Cart"))
        self.shopURL.setHtml(_translate("MainWindow",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Посилання на головну сторінку магазина</span></p></body></html>"))
        self.shopURL.setHtml("http://testcart.atwebpages.com/")
        self.apiKey.setHtml(
            "BCt9AeLzIs2TMRNTvMjHKvSq5lZne9MU6YV8Kqx0PA1YhfQEtLJYdxXTQAtaKp4kUUNGLNHdFU3cfXpkErGV7NuftPJR9E8vyu87ozwZbwYz6W8YReuH78g7zkuaf4MMiugF9lrelFT7Mtp0iE4Z71HzKpdfIAu8V5z5grGHlg3Jp6F7jzTvwPxa2GVKVvPwZoALR7u4268M2sM23Dghd9HqtkFkS296jMHiQupIiIcMG6pKvzEsJKRjinpKmUeB")
        self.loadToShop.setText(_translate("MainWindow", "Update goods list"))
        self.beta.setText(_translate("MainWindow", "BETA"))

    def addParam(self, text):
        self.logs.addItem(text)


def connection():
    key = ui.apiKey.toPlainText()
    url = ui.shopURL.toPlainText()
    try:
        if open_cart.connect(key, url) != 1:
            raise Exception('Unknown error!')
        ui.addParam("Connected!")
    except Exception as e:
        ui.addParam(str(e))


def load_list():
    try:
        count = open_cart.get_list()
        if count > 0:
            ui.addParam("You have " + str(count) + " goods in your shop!")
    except Exception as e:
        ui.addParam("Сервер не відповідає!")


def convert(page):
    returnList = []
    for row in page[1:]:
        list = []
        if (row[0] != "Номенклатура" and row[0] != "nan"):
            list.append(row[0])
            list.append(row[4])
            if (row[12] == "Скидка не распространяется") or (row[8] == "nan"):
                list.append(row[7])
            else:
                list.append(row[8])
            list.append(row[9].replace("≥", ""))
        if (list != []):
            returnList.append(list)
    return returnList


def list_to_shop():
    category = ""
    for page in shopList:
        for product in page:
            if (product[1] == "nan"):
                category = product[0]
            elif (int(product[2]) > 20):
                try:
                    id = int(open_cart.product_id(product[0]))
                    if id > 0:
                        list = open_cart.product_by_id(id)
                        list["price"] = product[2]
                        list["quantity"] = product[3]
                        list["name"] = product[0]
                        open_cart.product_edit(list)
                    else:
                        list = open_cart.product_build(product, category)
                        open_cart.product_add(list)
                except Exception as e:
                    ui.addParam("Error in getting server answer!!")
                    return
    ui.addParam("Your list successfully loaded into your OpenCart shop!")


def open_bereg():
    global shopList
    ui.addParam("Loading files!")
    filename = QFileDialog.getOpenFileName(MainWindow, 'Open file', '/')[0]
    try:
        df = pd.read_excel(filename, sheet_name=None)
        server = []
        for f in df:
            page = np.nan_to_num(df[f].values.tolist())
            if page[0][0] == "nan":
                continue
            server.append(convert(page))
        shopList = server
        ui.addParam("Your list successfully loaded into your OpenCart shop!")
    except Exception as e:
        ui.addParam(str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    open_cart = OpenCart()
    sys.exit(app.exec_())
