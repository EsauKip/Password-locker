class Credentials:
    '''generate instance of Credentials class
    '''
    credentials_list = []
    # assign property to credential list
    def __init__(self,account,email,password):
        self.account = account
        self.email = email
        self.password = password