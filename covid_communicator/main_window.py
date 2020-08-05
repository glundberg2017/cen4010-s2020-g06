import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from chat_window import ChatWindow
from database_adapter import DatabaseAdapter

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ui_file = os.path.dirname(sys.argv[0]) +"/main_window.ui"
        uic.loadUi(ui_file, self)
        self.db_adapter = DatabaseAdapter('lamp.eng.fau.edu', 'cen4010s2020_g06', 'faueng2020')

    def on_loginButton_released(self):
        self.startChat(self.emailLineEdit.text(), self.passwordLineEdit.text())

    def on_registerButton_released(self):
        self.startChat(self.emailLineEdit.text(), self.passwordLineEdit.text())

    def startChat(self, username, password):
        my_id = self.db_adapter.login(username, password)
        recipient_id,recipient_name = self.db_adapter.getRandomRecipient(my_id)
        chatWindow = ChatWindow(username, my_id, recipient_name, recipient_id)
        chatWindow.exec_()
            


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()