# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ConverterDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 123)
        MainWindow.setMaximumSize(QtCore.QSize(443, 123))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.FileSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.FileSelectButton.setObjectName("FileSelectButton")
        self.gridLayout.addWidget(self.FileSelectButton, 0, 0, 1, 1)
        self.h265Button = QtWidgets.QPushButton(self.centralwidget)
        self.h265Button.setObjectName("h265Button")
        self.gridLayout.addWidget(self.h265Button, 1, 0, 1, 1)
        self.h264Button = QtWidgets.QPushButton(self.centralwidget)
        self.h264Button.setObjectName("h264Button")
        self.gridLayout.addWidget(self.h264Button, 2, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 1, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 443, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ffmpegConverterController"))
        self.FileSelectButton.setText(_translate("MainWindow", "Выбрать видео..."))
        self.h265Button.setText(_translate("MainWindow", "Логи"))
        self.h264Button.setText(_translate("MainWindow", "Конвертировать"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action.setText(_translate("MainWindow", "Выбрать рабочий кодек..."))
        self.action_2.setText(_translate("MainWindow", "Выбор рабочей директории..."))
        self.action_3.setText(_translate("MainWindow", "Справка"))
