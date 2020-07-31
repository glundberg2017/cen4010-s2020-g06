import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

class ChatWindow(QtWidgets.QDialog):
    def __init__(self, senderName, senderID, recipientName, recipientId):
        super(ChatWindow, self).__init__()
        uic.loadUi('./chat_window.ui', self)
        self.senderName = senderName
        self.senderId = senderID
        self.recipientName = recipientName
        self.recipientId = recipientName

    def on_sendButton_released(self):
        print('sending message to database: {}'.format(self.messageLineEdit.text()))
        self.chatTextEdit.insertPlainText(self.senderName +': '+ self.messageLineEdit.text() +'\n')
        self.messageLineEdit.clear()