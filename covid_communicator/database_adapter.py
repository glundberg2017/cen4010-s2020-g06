import requests

class DatabaseAdapter:
    LOGIN_URL = 'http://lamp.cse.fau.edu/~cen4010s2020_g06/login.php'
    SEND_MESSAGE_URL = 'http://lamp.cse.fau.edu/~cen4010s2020_g06/send_message.php'
    GET_USERS_URL = 'http://lamp.cse.fau.edu/~cen4010s2020_g06/get_users.php'

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
        requests.post(DatabaseAdapter.LOGIN_URL, data)
    
    def sendMessage(self, sender, recipient, message):
        # this function sends a message between two users by
        # storing the message in the messages database
        pass

    def getRandomRecipient(self, user_id):
        # this function gets a list of users in the database
        # and returns a random user_id that is not the same as the user_id given
        pass

##
## TEST - create an instance of DatabaseAdapter and try to connect to it
if __name__ == "__main__":
    db_adapter = DatabaseAdapter('lamp.eng.fau.edu', 'cen4010s2020_g06', 'faueng2020')
    db_adapter.login('glundberg2017@fau.edu', 'grantspassword')