# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Nick\Desktop\vwyl.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.video_frame = QtWidgets.QFrame(self.centralwidget)
        self.video_frame.setStyleSheet("background-color: gray;")
        self.video_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_frame.setObjectName("video_frame")
        self.horizontalLayout.addWidget(self.video_frame)
        self.status_frame = QtWidgets.QFrame(self.centralwidget)
        self.status_frame.setStyleSheet("")
        self.status_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.status_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status_frame.setObjectName("status_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.status_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.status_frame)
        self.widget.setStyleSheet("background-color:rgb(170, 85, 255)")
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.listView = QtWidgets.QListView(self.status_frame)
        self.listView.setStyleSheet("background-color:rgb(255, 170, 0)")
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.horizontalLayout.addWidget(self.status_frame)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "微网优联SOP"))
