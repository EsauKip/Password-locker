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
### save the user account
def save_user(user):
    '''
    method save user  account
    '''
    user.save_user()

def save_credentials(credentials):

    '''
    method save credentials  account
    '''

    credentials.save_credentials
    ### find user using username

def find_user(username):
    '''
    method for find user using username
    '''
    return User.find_user(username)
         # create credentials
def create_credentials(account, email, passcode):
    '''
    method credentials details
    '''
    new_credentials = Credentials(account, email, passcode)
    return new_credentials
####save_credentials
def save_credentials(credentials):
    '''
    save credentials
    '''
    credentials.save_credentials()
##Display all the saved credentials
def display_credentials():
    '''
    method to display all the saved credentials
    '''
    return Credentials.display_credentials()
    #search for the account credentials

def find_account(account):
    '''
    method to search for an account
    '''
    return Credentials.find_account(account)
##delete the account credentials
def delete_credentials(account):
    '''
    method to delete account
    '''
    account.delete_credentials()




def main():
    # Dealing user class first
    print("Welcome to Password Locker! Please enter your name:  ")
    name = input ()
    print(f"{name}, Sign up to continue")
    print('\n')
    print("*" * 80)
    print("Reply with  : cc - Sign Up,  ex -exit ")
    print("*" * 80)
if __name__=='__main__':
  main()
    