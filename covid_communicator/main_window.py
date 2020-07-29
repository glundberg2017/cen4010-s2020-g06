import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from chat_window import ChatWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("./main_window.ui", self)
        self.logged_in = False

    def on_loginButton_clicked(self):
        self.startChat(self.emailLineEdit.text(), self.passwordLineEdit.text())

    def on_registerButton_clicked(self):
        self.startChat(self.emailLineEdit.text(), self.passwordLineEdit.text())

    def startChat(self, username, password):
        if not self.logged_in:
            self.logged_in = True
            chatWindow = ChatWindow()
            chatWindow.exec_()
            


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()