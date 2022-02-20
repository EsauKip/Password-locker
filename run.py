#!/usr/bin/env python3.9
from credentials import Credentials
from user import User
import random
# create user accounts
def create_useraccount(username, password):
    '''
    method creates a user account
    '''
    new_user = User(username, password)
    return new_user
