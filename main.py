import sys
from frames.login import Ui_LoginForm
from frames.admin import Ui_AdminWindow
from frames.reception import Ui_ReceptionWindow
from frames.service import Ui_ServiceWindow
from Database.HotelConnect import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class LoginWindow(QtWidgets.QDialog, Ui_LoginForm):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        self.btnlogin.clicked.connect(self.check_login)
        self.inputpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btncancellogin.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.label.setPixmap(QPixmap('resources/logo150.png'))


        self.show()

    def mainReceptionWindow(self):
        self.receptionWindow = ReceptWindow()
        self.hide()

    def mainAdminWindow(self):
        self.adminWindow = AdminWindow()
        self.hide()

    def mainServiceWindow(self):
        self.serviceWindow = ServiceWindow()
        self.hide()

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def check_login(self):
        User = Employee()
        user = self.inputuser.text()
        passwd = self.inputpass.text()
        result = User.EmployeeList()
        for i in result:
            if user == i[8] and passwd == i[9]:
                print("Login successful!")
                EmpID = i[0]
                EmpTitle = i[3]
                print('EmpID:', EmpID)
                print('Title:', EmpTitle)
                if EmpTitle == "Admin":
                    self.mainAdminWindow()
                elif EmpTitle == "Recept":
                    self.mainReceptionWindow()
                elif EmpTitle == "Service":
                    self.mainServiceWindow()
                break

        else:
            print("Login unsuccessful!")
            self.showMessageBox('Warning', 'User not found in database!')


class AdminWindow(QtWidgets.QMainWindow, Ui_AdminWindow):
    def __init__(self):
        super(AdminWindow, self).__init__()
        self.setupUi(self)
        self.show()

class ReceptWindow(QtWidgets.QMainWindow, Ui_ReceptionWindow):
    def __init__(self):
        super(ReceptWindow, self).__init__()
        self.setupUi(self)

        self.label.setText("Receptionist Anne Frank <3")

        self.show()

class ServiceWindow(QtWidgets.QMainWindow, Ui_ServiceWindow):
    def __init__(self):
        super(ServiceWindow, self).__init__()
        self.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())
