# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoDlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(342, 363)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushBtnCancle = QtWidgets.QPushButton(Dialog)
        self.pushBtnCancle.setGeometry(QtCore.QRect(130, 310, 75, 25))
        self.pushBtnCancle.setObjectName("pushBtnCancle")
        self.pushBtnOkay = QtWidgets.QPushButton(Dialog)
        self.pushBtnOkay.setGeometry(QtCore.QRect(225, 310, 75, 25))
        self.pushBtnOkay.setObjectName("pushBtnOkay")
        self.labelNo = QtWidgets.QLabel(Dialog)
        self.labelNo.setGeometry(QtCore.QRect(40, 30, 30, 16))
        self.labelNo.setObjectName("labelNo")
        self.lineEdNo = QtWidgets.QLineEdit(Dialog)
        self.lineEdNo.setEnabled(False)
        self.lineEdNo.setGeometry(QtCore.QRect(75, 30, 225, 20))
        self.lineEdNo.setObjectName("lineEdNo")
        self.labelOtherInfo = QtWidgets.QLabel(Dialog)
        self.labelOtherInfo.setGeometry(QtCore.QRect(40, 230, 30, 16))
        self.labelOtherInfo.setObjectName("labelOtherInfo")
        self.textEdOtherinfo = QtWidgets.QTextEdit(Dialog)
        self.textEdOtherinfo.setGeometry(QtCore.QRect(75, 230, 225, 70))
        self.textEdOtherinfo.setObjectName("textEdOtherinfo")
        self.labelPhone = QtWidgets.QLabel(Dialog)
        self.labelPhone.setGeometry(QtCore.QRect(40, 190, 30, 16))
        self.labelPhone.setObjectName("labelPhone")
        self.lineEdPhone = QtWidgets.QLineEdit(Dialog)
        self.lineEdPhone.setGeometry(QtCore.QRect(75, 190, 225, 20))
        self.lineEdPhone.setObjectName("lineEdPhone")
        self.labelName = QtWidgets.QLabel(Dialog)
        self.labelName.setGeometry(QtCore.QRect(40, 70, 30, 16))
        self.labelName.setObjectName("labelName")
        self.lineEdName = QtWidgets.QLineEdit(Dialog)
        self.lineEdName.setGeometry(QtCore.QRect(75, 70, 225, 20))
        self.lineEdName.setObjectName("lineEdName")
        self.labelAge = QtWidgets.QLabel(Dialog)
        self.labelAge.setGeometry(QtCore.QRect(40, 110, 30, 16))
        self.labelAge.setObjectName("labelAge")
        self.lineEdAge = QtWidgets.QLineEdit(Dialog)
        self.lineEdAge.setGeometry(QtCore.QRect(75, 110, 225, 20))
        self.lineEdAge.setObjectName("lineEdAge")
        self.labelGender = QtWidgets.QLabel(Dialog)
        self.labelGender.setEnabled(True)
        self.labelGender.setGeometry(QtCore.QRect(40, 150, 30, 20))
        self.labelGender.setMinimumSize(QtCore.QSize(20, 20))
        self.labelGender.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelGender.setObjectName("labelGender")
        self.comboBoxGender = QtWidgets.QComboBox(Dialog)
        self.comboBoxGender.setEnabled(True)
        self.comboBoxGender.setGeometry(QtCore.QRect(75, 150, 225, 20))
        self.comboBoxGender.setMinimumSize(QtCore.QSize(210, 0))
        self.comboBoxGender.setObjectName("comboBoxGender")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "联系人信息"))
        self.pushBtnCancle.setText(_translate("Dialog", "清空"))
        self.pushBtnOkay.setText(_translate("Dialog", "保存"))
        self.labelNo.setText(_translate("Dialog", "序号:"))
        self.labelOtherInfo.setText(_translate("Dialog", "备注:"))
        self.labelPhone.setText(_translate("Dialog", "电话:"))
        self.labelName.setText(_translate("Dialog", "姓名:"))
        self.labelAge.setText(_translate("Dialog", "年龄:"))
        self.labelGender.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.labelGender.setText(_translate("Dialog", "性别:"))
        self.comboBoxGender.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))

