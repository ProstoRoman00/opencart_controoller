# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.clickBereg.setGeometry(QtCore.QRect(210, 240, 181, 41))
        self.clickBereg.setObjectName("clickBereg")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 320, 751, 261))
        self.listView.setObjectName("listView")
        self.shopLoadList = QtWidgets.QPushButton(self.centralwidget)
        self.shopLoadList.setGeometry(QtCore.QRect(400, 240, 181, 41))
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
        self.shopLoadList_2 = QtWidgets.QPushButton(self.centralwidget)
        self.shopLoadList_2.setGeometry(QtCore.QRect(590, 240, 181, 41))
        self.shopLoadList_2.setObjectName("shopLoadList_2")
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
        self.clickBereg.clicked.connect(openBereg)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">OpenCart Shop Controller</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<font size=30>OpenCart Shop controller</font>"))
        self.clickBereg.setText(_translate("MainWindow", "Загрузити Bereg"))
        self.shopLoadList.setText(_translate("MainWindow", "OpenCart список товарів"))
        self.apiKey.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Open Cart API KEY</span></p></body></html>"))
        self.shopConnection.setText(_translate("MainWindow", "Підключитися до OpenCart"))
        self.shopURL.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Посилання на головну сторінку магазина</span></p></body></html>"))
        self.shopLoadList_2.setText(_translate("MainWindow", "Обновити список товарів"))
        self.beta.setText(_translate("MainWindow", "BETA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
