# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(299, 326)
        LoginForm.setInputMethodHints(QtCore.Qt.ImhNone)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(LoginForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(LoginForm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.inputuser = QtWidgets.QLineEdit(LoginForm)
        self.inputuser.setObjectName("inputuser")
        self.horizontalLayout.addWidget(self.inputuser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(LoginForm)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.inputpass = QtWidgets.QLineEdit(LoginForm)
        self.inputpass.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.inputpass.setClearButtonEnabled(False)
        self.inputpass.setObjectName("inputpass")
        self.horizontalLayout_3.addWidget(self.inputpass)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btncancellogin = QtWidgets.QPushButton(LoginForm)
        self.btncancellogin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btncancellogin.setObjectName("btncancellogin")
        self.horizontalLayout_4.addWidget(self.btncancellogin)
        self.btnlogin = QtWidgets.QPushButton(LoginForm)
        self.btnlogin.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnlogin.setObjectName("btnlogin")
        self.horizontalLayout_4.addWidget(self.btnlogin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)


    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Hraun Hótel - Innskráning"))
        self.label_2.setText(_translate("LoginForm", "Username"))
        self.label_3.setText(_translate("LoginForm", "Password"))
        self.btncancellogin.setText(_translate("LoginForm", "Cancel"))
        self.btnlogin.setText(_translate("LoginForm", "Login"))

