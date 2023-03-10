# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\windows\UEM_Test_Tools\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from help_main import helper_main 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 612)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(helper_main.resource_path(os.path.join("res","skins\\uem.ico"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setStyleSheet("color:#0000ff")
        self.label_23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_23.setTextFormat(QtCore.Qt.AutoText)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 1, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 2, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#aaaa7f")
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setStyleSheet("background-color:#00ff00")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_4.addWidget(self.pushButton_10, 3, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setStyleSheet("background-color:#00ff00")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 3, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setStyleSheet("color:#0000ff")
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 4, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setStyleSheet("background-color:#00ff00")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_4.addWidget(self.pushButton_6, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#aaaa7f")
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 5, 1, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setStyleSheet("background-color:#00ff00")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#aaaa7f")
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 6, 1, 1, 2)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setStyleSheet("background-color:#00ff00")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_4.addWidget(self.pushButton_7, 7, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setStyleSheet("color:#0000ff")
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 8, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.tab)
        self.pushButton_14.setStyleSheet("background-color:#00ff00")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_4.addWidget(self.pushButton_14, 9, 0, 1, 2)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_13.setStyleSheet("")
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_4.addWidget(self.lineEdit_13, 9, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.tab)
        self.pushButton_13.setStyleSheet("background-color:#00ff00")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_4.addWidget(self.pushButton_13, 9, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setStyleSheet("color:#0000ff")
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 10, 0, 1, 4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_4.addWidget(self.lineEdit_5, 11, 0, 1, 2)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_4.addWidget(self.pushButton_11, 11, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.tab)
        self.pushButton_12.setStyleSheet("background-color:#00ff00")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_4.addWidget(self.pushButton_12, 11, 3, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setBaseSize(QtCore.QSize(0, 0))
        self.textBrowser_2.setStyleSheet("color:#0000ff")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_4.addWidget(self.textBrowser_2, 12, 0, 1, 4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setStyleSheet("color:#0000ff")
        self.label_30.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_30.setTextFormat(QtCore.Qt.AutoText)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 0, 0, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_20.setStyleSheet("background-color:#00ff00")
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_3.addWidget(self.pushButton_20, 1, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color:#7d7d7d")
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 1, 1, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_21.setStyleSheet("background-color:#00ff00")
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_3.addWidget(self.pushButton_21, 2, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_22.setStyleSheet("background-color:#00ff00")
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_3.addWidget(self.pushButton_22, 2, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setStyleSheet("color:#0000ff")
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 3, 0, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_19.setStyleSheet("background-color:#00ff00")
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_3.addWidget(self.pushButton_19, 4, 0, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setBaseSize(QtCore.QSize(0, 0))
        self.textBrowser_3.setStyleSheet("color:#0000ff")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_3.addWidget(self.textBrowser_3, 5, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setStyleSheet("color:#0000ff")
        self.label_25.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_25.setTextFormat(QtCore.Qt.AutoText)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 0, 0, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 0, 1, 2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 2, 1, 2)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 1, 4, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_3)
        self.lcdNumber.setSizeIncrement(QtCore.QSize(0, 0))
        self.lcdNumber.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lcdNumber.setStyleSheet("background-color:#55ffff")
        self.lcdNumber.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 2, 2, 1, 2)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setStyleSheet("background-color:#00ff00")
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 2, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setStyleSheet("color:#0000ff")
        self.label_26.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_26.setTextFormat(QtCore.Qt.AutoText)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 5, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 6, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 7, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 8, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 4, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 5, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_3, 6, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_4, 7, 1, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab_3)
        self.lcdNumber_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.lcdNumber_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lcdNumber_2.setStyleSheet("background-color:#55ffff")
        self.lcdNumber_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lcdNumber_2.setLineWidth(1)
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setDigitCount(6)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("intValue", 0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_2.addWidget(self.lcdNumber_2, 8, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setStyleSheet("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 5, 2, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 6, 2, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_8.setStyleSheet("")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 7, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color:#00ff00")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 8, 2, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color:#ff0000")
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 8, 4, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setBaseSize(QtCore.QSize(0, 0))
        self.textBrowser.setStyleSheet("color:#0000ff")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 9, 0, 1, 6)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_27 = QtWidgets.QLabel(self.tab_4)
        self.label_27.setStyleSheet("color:#0000ff")
        self.label_27.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_27.setTextFormat(QtCore.Qt.AutoText)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 0, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_5.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_5.addWidget(self.pushButton_16, 1, 1, 1, 2)
        self.pushButton_29 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_5.addWidget(self.pushButton_29, 1, 3, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_5.addWidget(self.pushButton_17, 1, 4, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_5.addWidget(self.pushButton_23, 1, 5, 1, 2)
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_5.addWidget(self.pushButton_24, 1, 7, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.tab_4)
        self.label_28.setStyleSheet("color:#0000ff")
        self.label_28.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_28.setTextFormat(QtCore.Qt.AutoText)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 2, 0, 1, 8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_9.setStyleSheet("")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_5.addWidget(self.lineEdit_9, 3, 0, 1, 4)
        self.pushButton_25 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_5.addWidget(self.pushButton_25, 3, 4, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_26.setStyleSheet("background-color:#aaff00")
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_5.addWidget(self.pushButton_26, 3, 6, 1, 2)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_14.setStyleSheet("")
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_5.addWidget(self.lineEdit_14, 4, 0, 1, 4)
        self.pushButton_28 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_5.addWidget(self.pushButton_28, 4, 4, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_10.setStyleSheet("")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_5.addWidget(self.lineEdit_10, 5, 0, 1, 2)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_11.setStyleSheet("")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_5.addWidget(self.lineEdit_11, 5, 2, 1, 2)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_12.setStyleSheet("")
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_5.addWidget(self.lineEdit_12, 5, 4, 1, 2)
        self.pushButton_27 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_27.setStyleSheet("background-color:#00ff00")
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_5.addWidget(self.pushButton_27, 5, 6, 1, 2)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_4.setBaseSize(QtCore.QSize(0, 0))
        self.textBrowser_4.setStyleSheet("color:#0000ff")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout_5.addWidget(self.textBrowser_4, 6, 0, 1, 8)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UEM??????????????????v1.7"))
        self.label_23.setText(_translate("MainWindow", "1.UEM???????????????"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "?????????MD5????????????"))
        self.pushButton.setText(_translate("MainWindow", "????????????"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "?????????UEM????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "???????????????"))
        self.label_3.setText(_translate("MainWindow", "?????????UEM??????"))
        self.pushButton_10.setText(_translate("MainWindow", "??????????????????MD5"))
        self.pushButton_4.setText(_translate("MainWindow", "??????UEM????????????"))
        self.label_10.setText(_translate("MainWindow", "2.UEM??????????????????"))
        self.pushButton_6.setText(_translate("MainWindow", "??????UEM????????????"))
        self.label_5.setText(_translate("MainWindow", "?????????UEM??????"))
        self.pushButton_5.setText(_translate("MainWindow", "??????UEM???????????????"))
        self.label_4.setText(_translate("MainWindow", "??????????????????"))
        self.pushButton_7.setText(_translate("MainWindow", "????????????UEM???????????????"))
        self.label_18.setText(_translate("MainWindow", "3.UEM??????????????????"))
        self.pushButton_14.setText(_translate("MainWindow", "??????UEM??????????????????????????????"))
        self.lineEdit_13.setPlaceholderText(_translate("MainWindow", "???????????????ID"))
        self.pushButton_13.setText(_translate("MainWindow", "??????????????????????????????"))
        self.label_24.setText(_translate("MainWindow", "4.PC??????????????????????????????????????????????????????????????????????????????????????????"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "?????????PC??????????????????"))
        self.pushButton_11.setText(_translate("MainWindow", "???????????????"))
        self.pushButton_12.setText(_translate("MainWindow", "????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "UEM??????????????????"))
        self.label_30.setText(_translate("MainWindow", "1.UEM?????????????????????"))
        self.pushButton_20.setText(_translate("MainWindow", "???????????????UEM??????????????????????????????"))
        self.label_32.setText(_translate("MainWindow", "(bRet=1???????????????bRet=1????????????)"))
        self.pushButton_21.setText(_translate("MainWindow", "?????????????????????????????????????????????"))
        self.pushButton_22.setText(_translate("MainWindow", "??????????????????????????????????????????"))
        self.label_29.setText(_translate("MainWindow", "2.???????????????????????????"))
        self.pushButton_19.setText(_translate("MainWindow", "??????UEM??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "UEM??????????????????"))
        self.label_25.setText(_translate("MainWindow", "1.???????????????????????????"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "?????????????????????"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "????????????????????????????????????"))
        self.pushButton_9.setText(_translate("MainWindow", "????????????"))
        self.label_19.setText(_translate("MainWindow", "?????????????????????"))
        self.pushButton_8.setText(_translate("MainWindow", "????????????????????????"))
        self.label_26.setText(_translate("MainWindow", "2.?????????????????????"))
        self.label_13.setText(_translate("MainWindow", "???????????????"))
        self.label_14.setText(_translate("MainWindow", "???????????????"))
        self.label_15.setText(_translate("MainWindow", "???????????????"))
        self.label_16.setText(_translate("MainWindow", "???????????????"))
        self.label_17.setText(_translate("MainWindow", "???????????????"))
        self.comboBox.setItemText(0, _translate("MainWindow", "TELNET"))
        self.comboBox.setItemText(1, _translate("MainWindow", "HTTP"))
        self.comboBox.setItemText(2, _translate("MainWindow", "HTTPS"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "??????IP"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "IP??????"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "??????"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "????????????"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "????????????"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "????????????"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "?????????"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "????????????"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "?????????10.242.2.158"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "?????????80"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "??????????????????"))
        self.pushButton_15.setText(_translate("MainWindow", "START"))
        self.pushButton_18.setText(_translate("MainWindow", "STOP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "UEM??????????????????"))
        self.label_27.setText(_translate("MainWindow", "1.???????????????????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "Procexp"))
        self.pushButton_16.setText(_translate("MainWindow", "ResHacker"))
        self.pushButton_29.setText(_translate("MainWindow", "DebugView"))
        self.pushButton_17.setText(_translate("MainWindow", "Procmon"))
        self.pushButton_23.setText(_translate("MainWindow", "hash_1.0.4"))
        self.pushButton_24.setText(_translate("MainWindow", "FVIE"))
        self.label_28.setText(_translate("MainWindow", "2.??????????????????????????????????????????????????????????????????,??????????????????????????????Execl???"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "?????????exe??????"))
        self.pushButton_25.setText(_translate("MainWindow", "????????????"))
        self.pushButton_26.setText(_translate("MainWindow", "????????????????????????"))
        self.lineEdit_14.setPlaceholderText(_translate("MainWindow", "?????????????????????Excel????????????"))
        self.pushButton_28.setText(_translate("MainWindow", "???????????????"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "?????????????????????"))
        self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "???????????????"))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "???????????????"))
        self.pushButton_27.setText(_translate("MainWindow", "??????execl??????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "??????????????????"))
