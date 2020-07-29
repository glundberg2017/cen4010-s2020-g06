import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

class ChatWindow(QtWidgets.QDialog):
    def __init__(self):
        super(ChatWindow, self).__init__()
        uic.loadUi('./chat_window.ui', self)

    def on_sendButton_clicked(self):
        print('sending message to database: {}'.format(self.messageLineEdit.text()))