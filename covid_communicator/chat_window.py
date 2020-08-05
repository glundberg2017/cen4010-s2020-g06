import os
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from database_adapter import DatabaseAdapter

class ChatWindow(QtWidgets.QDialog):

    def __init__(self, senderName, senderId, recipientName, recipientId):
        super(ChatWindow, self).__init__()
        ui_file = os.path.dirname(os.path.abspath(__file__)) + '/chat_window.ui'
        uic.loadUi(ui_file, self)
        self.senderName = senderName
        self.senderId = senderId
        self.recipientName = recipientName
        self.recipientId = recipientId
        self.db_adapter = DatabaseAdapter('lamp.eng.fau.edu', 'cen4010s2020_g06', 'faueng2020')
        self.recipientLabel.setText(self.recipientName)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.timer.start(3000)

    def refresh(self):
        # Get messages between users
        messages = self.db_adapter.getMessages(self.senderId, self.recipientId)
        self.chatTextEdit.setText(messages)

    def on_sendButton_released(self):
        self.db_adapter.sendMessage(self.senderId, self.recipientId, self.messageLineEdit.text())
        self.messageLineEdit.clear()