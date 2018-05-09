# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'service.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServiceWindow(object):
    def setupUi(self, ServiceWindow):
        ServiceWindow.setObjectName("ServiceWindow")
        ServiceWindow.resize(528, 501)
        self.centralwidget = QtWidgets.QWidget(ServiceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        ServiceWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ServiceWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 22))
        self.menubar.setObjectName("menubar")
        self.menuPantanir = QtWidgets.QMenu(self.menubar)
        self.menuPantanir.setObjectName("menuPantanir")
        ServiceWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ServiceWindow)
        self.statusbar.setObjectName("statusbar")
        ServiceWindow.setStatusBar(self.statusbar)
        self.actionLista_pantanir = QtWidgets.QAction(ServiceWindow)
        self.actionLista_pantanir.setObjectName("actionLista_pantanir")
        self.menuPantanir.addAction(self.actionLista_pantanir)
        self.menubar.addAction(self.menuPantanir.menuAction())

        self.retranslateUi(ServiceWindow)
        QtCore.QMetaObject.connectSlotsByName(ServiceWindow)

    def retranslateUi(self, ServiceWindow):
        _translate = QtCore.QCoreApplication.translate
        ServiceWindow.setWindowTitle(_translate("ServiceWindow", "Hraun Hótel - Þjónustuaðili"))
        self.label.setText(_translate("ServiceWindow", "Service"))
        self.menuPantanir.setTitle(_translate("ServiceWindow", "Pantanir"))
        self.actionLista_pantanir.setText(_translate("ServiceWindow", "Lista pantanir"))

