# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtDesignerProject/service.ui'
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
        self.statusbar = QtWidgets.QStatusBar(ServiceWindow)
        self.statusbar.setObjectName("statusbar")
        ServiceWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(ServiceWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 22))
        self.menubar.setObjectName("menubar")
        self.menuForrit = QtWidgets.QMenu(self.menubar)
        self.menuForrit.setObjectName("menuForrit")
        ServiceWindow.setMenuBar(self.menubar)
        self.actionLista_pantanir = QtWidgets.QAction(ServiceWindow)
        self.actionLista_pantanir.setObjectName("actionLista_pantanir")
        self.actionSkra_ut = QtWidgets.QAction(ServiceWindow)
        self.actionSkra_ut.setObjectName("actionSkra_ut")
        self.actionH_tta = QtWidgets.QAction(ServiceWindow)
        self.actionH_tta.setObjectName("actionH_tta")
        self.menuForrit.addAction(self.actionSkra_ut)
        self.menuForrit.addAction(self.actionH_tta)
        self.menubar.addAction(self.menuForrit.menuAction())

        self.retranslateUi(ServiceWindow)
        QtCore.QMetaObject.connectSlotsByName(ServiceWindow)

    def retranslateUi(self, ServiceWindow):
        _translate = QtCore.QCoreApplication.translate
        ServiceWindow.setWindowTitle(_translate("ServiceWindow", "Hraun Hótel - Þjónustuaðili"))
        self.label.setText(_translate("ServiceWindow", "Service"))
        self.menuForrit.setTitle(_translate("ServiceWindow", "Forrit"))
        self.actionLista_pantanir.setText(_translate("ServiceWindow", "Lista pantanir"))
        self.actionSkra_ut.setText(_translate("ServiceWindow", "Skrá út"))
        self.actionH_tta.setText(_translate("ServiceWindow", "Hætta"))

