# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/addlistUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import test


class AddListUI_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 600)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 600))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(0, 90, 145, 200);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgba(255, 255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gobackButton = QtWidgets.QPushButton(Dialog)
        self.gobackButton.setGeometry(QtCore.QRect(20, 20, 30, 30))
        self.gobackButton.setStyleSheet("background-color: rgba(0, 90, 145, 0);\n"
                                        "border-image: url(:/newPrefix/backarrow.png);")
        self.gobackButton.setText("")
        self.gobackButton.setObjectName("gobackButton")
        self.workimageLabel = QtWidgets.QLabel(Dialog)
        self.workimageLabel.setGeometry(QtCore.QRect(160, 80, 80, 80))
        self.workimageLabel.setStyleSheet("\n"
                                          "border-radius: 40px;\n"
                                          "")
        self.workimageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.workimageLabel.setObjectName("workimageLabel")
        self.processComboBox = QtWidgets.QComboBox(Dialog)
        self.processComboBox.setGeometry(QtCore.QRect(30, 200, 340, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.processComboBox.setFont(font)
        self.processComboBox.setAccessibleName("")
        self.processComboBox.setStyleSheet("background-color: rgba(0, 90, 145, 0);\n"
                                           "border:none;\n"
                                           "border-bottom: 1px solid rgba(255, 255, 255, 80);\n"
                                           "color: rgba(255, 255, 255, 255);\n"
                                           "padding-bottom:7px;\n"
                                           "selection-color: rgb(255, 255, 255);\n"
                                           "selection-background-color: rgb(0, 0, 0);\n"
                                           "gridline-color: rgb(255, 255, 255);")
        self.processComboBox.setIconSize(QtCore.QSize(12, 12))
        self.processComboBox.setObjectName("processComboBox")
        self.processComboBox.addItem("")
        self.processComboBox.addItem("")
        self.detailsLineEdit = QtWidgets.QLineEdit(Dialog)
        self.detailsLineEdit.setGeometry(QtCore.QRect(30, 410, 340, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.detailsLineEdit.setFont(font)
        self.detailsLineEdit.setStyleSheet("background-color: rgba(0, 90, 145, 0);\n"
                                           "border:none;\n"
                                           "border-bottom: 1px solid rgba(255, 255, 255, 80);\n"
                                           "color: rgba(255, 255, 255, 240);\n"
                                           "padding-bottom:7px;")
        self.detailsLineEdit.setObjectName("detailsLineEdit")
        self.completeadditemButton = QtWidgets.QPushButton(Dialog)
        self.completeadditemButton.setGeometry(QtCore.QRect(30, 500, 340, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setBold(True)
        font.setWeight(75)
        self.completeadditemButton.setFont(font)
        self.completeadditemButton.setStyleSheet("background-color: rgb(0, 180, 220);\n"
                                                 "color: rgba(255, 255, 255, 255);")
        self.completeadditemButton.setObjectName("completeadditemButton")
        self.worktypeComboBox = QtWidgets.QComboBox(Dialog)
        self.worktypeComboBox.setGeometry(QtCore.QRect(30, 270, 340, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.worktypeComboBox.setFont(font)
        self.worktypeComboBox.setAccessibleName("")
        self.worktypeComboBox.setStyleSheet("background-color: rgba(0, 90, 145, 0);\n"
                                            "border:none;\n"
                                            "border-bottom: 1px solid rgba(255, 255, 255, 80);\n"
                                            "color: rgba(255, 255, 255, 255);\n"
                                            "padding-bottom:7px;\n"
                                            "selection-color: rgb(255, 255, 255);\n"
                                            "selection-background-color: rgb(0, 0, 0);\n"
                                            "gridline-color: rgb(255, 255, 255);")
        self.worktypeComboBox.setObjectName("worktypeComboBox")
        self.worktypeComboBox.addItem("")
        self.worktypeComboBox.addItem("")
        self.worktypeComboBox.addItem("")
        self.worktypeComboBox.addItem("")
        self.worktypeComboBox.addItem("")
        self.importanceComboBox = QtWidgets.QComboBox(Dialog)
        self.importanceComboBox.setGeometry(QtCore.QRect(30, 340, 340, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.importanceComboBox.setFont(font)
        self.importanceComboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.importanceComboBox.setAccessibleName("")
        self.importanceComboBox.setStyleSheet("background-color: rgba(0, 90, 145, 0);\n"
                                              "border:none;\n"
                                              "border-bottom: 1px solid rgba(255, 255, 255, 80);\n"
                                              "color: rgba(255, 255, 255, 255);\n"
                                              "padding-bottom:7px;\n"
                                              "selection-color: rgb(255, 255, 255);\n"
                                              "selection-background-color: rgb(0, 0, 0);\n"
                                              "gridline-color: rgb(255, 255, 255);")
        self.importanceComboBox.setObjectName("importanceComboBox")
        self.importanceComboBox.addItem("")
        self.importanceComboBox.addItem("")
        self.importanceComboBox.addItem("")

        self.retranslateUi(Dialog)
        self.processComboBox.setCurrentIndex(0)
        self.worktypeComboBox.setCurrentIndex(0)
        self.importanceComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.processComboBox, self.detailsLineEdit)
        Dialog.setTabOrder(self.detailsLineEdit, self.completeadditemButton)
        Dialog.setTabOrder(self.completeadditemButton, self.gobackButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Add new thing"))
        self.workimageLabel.setText(_translate("Dialog", "TextLabel"))
        self.processComboBox.setItemText(0, _translate("Dialog", "TO DO"))
        self.processComboBox.setItemText(
            1, _translate("Dialog", "IN PROGRESS"))
        self.detailsLineEdit.setPlaceholderText(
            _translate("Dialog", "Details"))
        self.completeadditemButton.setText(
            _translate("Dialog", "ADD YOUR THING"))
        self.worktypeComboBox.setItemText(0, _translate("Dialog", "Study"))
        self.worktypeComboBox.setItemText(1, _translate("Dialog", "Cleaning"))
        self.worktypeComboBox.setItemText(2, _translate("Dialog", "Exercise"))
        self.worktypeComboBox.setItemText(3, _translate("Dialog", "Rest"))
        self.worktypeComboBox.setItemText(4, _translate("Dialog", "Reading"))
        self.importanceComboBox.setItemText(0, _translate("Dialog", "Major"))
        self.importanceComboBox.setItemText(1, _translate("Dialog", "Normal"))
        self.importanceComboBox.setItemText(2, _translate("Dialog", "Minor"))
