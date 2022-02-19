
class Credentials:
    '''generate instance of Credentials class
    '''
    credentials_list = []
    # assign property to credential list
    def __init__(self,account,email,password):
        self.account = account
        self.email = email
        self.password = password
    def save_credentials(self):
        '''
        self credentials in credential_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete credentials 
        '''
        Credentials.credentials_list.remove(self) 