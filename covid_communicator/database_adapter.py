import requests
import random
import time
import datetime

class DatabaseAdapter:
    LOGIN_URL = 'https://lamp.cse.fau.edu/~cen4010s2020_g06/login.php'
    SEND_MESSAGE_URL = 'https://lamp.cse.fau.edu/~cen4010s2020_g06/send_message.php'
    GET_USERS_URL = 'https://lamp.cse.fau.edu/~cen4010s2020_g06/get_users.php'
    GET_MESSAGES_URL = 'https://lamp.cse.fau.edu/~cen4010s2020_g06/get_messages.php'

    def __init__(self, host='', username='', password=''):
        self.host = host
        self.username = username
        self.password = password

    def login(self, user, password):
        # this function performs the login/register action.
        # it sends the user & password to the login.php page to
        # authenticate and add users to the database
        data = {'email': user,
                'password': password}
        result = requests.post(DatabaseAdapter.LOGIN_URL, data)
        return result.text
    
    def sendMessage(self, sender, recipient, message):
        # this function sends a message between two users by
        # storing the message in the messages database
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        data = {'timestamp': timestamp,
                'sender_id': sender,
                'recipient_id': recipient,
                'message': message}
        requests.post(DatabaseAdapter.SEND_MESSAGE_URL, data)

    def getRandomRecipient(self, user_id):
        # this function gets a list of users in the database
        # and returns a random user_id that is not the same as the user_id given
        data = {'id': user_id}
        result = requests.post(DatabaseAdapter.GET_USERS_URL, data)
        result = result.text.split('||')
        rnd = random.randrange(0, len(result)-1)
        recipient = result[rnd]
        return recipient.split('|')

    def getMessages(self, id1, id2):
        data = {'id1': id1,
                'id2': id2}
        result = requests.post(DatabaseAdapter.GET_MESSAGES_URL, data)
        return result.text

##
## TEST - create an instance of DatabaseAdapter and try to connect to it
if __name__ == "__main__":
    db_adapter = DatabaseAdapter('lamp.eng.fau.edu', 'cen4010s2020_g06', 'faueng2020')
    #db_adapter.login('glundberg2017@fau.edu', 'grantspassword')
    #print(db_adapter.getRandomRecipient('9'))
    print(db_adapter.getMessages(9,10))