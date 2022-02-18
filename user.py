## create a class
class User:
    """generate an instance of a class
    """
    user_list=[]#list of users
    def __init__(self,username,password):
        self.username = username
        self.password =password
        ##save users
    def save_user(self):
        User.user_list.append(self)
   
    def delete_user(self):
        User.user_list.remove(self)