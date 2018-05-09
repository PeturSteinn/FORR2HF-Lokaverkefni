# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reception.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReceptionWindow(object):
    def setupUi(self, ReceptionWindow):
        ReceptionWindow.setObjectName("ReceptionWindow")
        ReceptionWindow.resize(583, 394)
        self.centralwidget = QtWidgets.QWidget(ReceptionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        ReceptionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ReceptionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 583, 22))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setObjectName("menubar")
        self.menuB_kanir = QtWidgets.QMenu(self.menubar)
        self.menuB_kanir.setObjectName("menuB_kanir")
        ReceptionWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ReceptionWindow)
        self.statusbar.setObjectName("statusbar")
        ReceptionWindow.setStatusBar(self.statusbar)
        self.actionBoka = QtWidgets.QAction(ReceptionWindow)
        self.actionBoka.setObjectName("actionBoka")
        self.actionSja_bokanir = QtWidgets.QAction(ReceptionWindow)
        self.actionSja_bokanir.setObjectName("actionSja_bokanir")
        self.menuB_kanir.addAction(self.actionBoka)
        self.menuB_kanir.addAction(self.actionSja_bokanir)
        self.menubar.addAction(self.menuB_kanir.menuAction())

        self.retranslateUi(ReceptionWindow)
        QtCore.QMetaObject.connectSlotsByName(ReceptionWindow)

    def retranslateUi(self, ReceptionWindow):
        _translate = QtCore.QCoreApplication.translate
        ReceptionWindow.setWindowTitle(_translate("ReceptionWindow", "Hraun Hótel - Móttökuritari"))
        self.label.setText(_translate("ReceptionWindow", "Reception"))
        self.menuB_kanir.setTitle(_translate("ReceptionWindow", "Bókanir"))
        self.actionBoka.setText(_translate("ReceptionWindow", "Bóka"))
        self.actionSja_bokanir.setText(_translate("ReceptionWindow", "Sjá bókanir"))

