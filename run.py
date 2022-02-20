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
    print("Welcome to Password Locker! Please enter your name to begin:  ")
    name = input ()
    print(f"{name}, Sign up to start")
    print('\n')
    print("*" * 80)
    print("Reply with  : cc - Sign Up,  ex -exit ")
    print("*" * 80)
    while True:
        short_code = input().lower()
        if short_code == 'cc':
            print("Account creating process begins...")
            print("Please enter the following information:")
            print("Username: ")
            username = input()

            print("Password: ")
            password = input()

            save_user(create_useraccount(username, password))
            print('\n')
            print(f"{name}'s Account information: ")
            print(f"Username: {username} , Password:{password}")
            print('\n')
            print(f"Logged in. Welcome {username}!")
            print("*" * 80)
         ##### utilize the credentials
            print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
            print("*" * 80)
        elif short_code == "ca":
            print("Enter account details: ")
            print("Account Name(e.g:linkedin): ")
            account = input()
            print("Email: ")
            email = input()
            print("Would you like a generated password?")
        if input()=="yes":
                characters= "mcnzbxvlkjhgfdsaqwertyuiop@#&$!()1234567890MCNZBXVLKJHGFDSAQWERTYUIOP"
                how_many = len(characters)
                print("How long would you like your password to be? ")
                print(f"p.s: Maximum length of password is {how_many}")
                lent = int(input())
                password = "".join(random.sample(characters, lent))
                print(f"Your password has {lent} characters ")
                print(password)
                save_credentials(create_credentials(account, email, password))
                print("saved! Enter 'da' to see account")
                print("*" * 80)
                print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
                print("*" * 80)
        elif input() == "no":
                print("Password: ")
                password=input()
                save_credentials(create_credentials(account, email, password))
                print("Credentials saved! Enter 'da' to see account")
                print("*" * 80)
                print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
                print("*" * 80)
                  ###generating and save new password
                save_user(create_credentials(account, email,password)) 
                save_credentials(create_credentials(account, email,password))
                print ('\n')
                print(f"New User {account} {email} created")
                print ('\n')

        else:
                print("Cant find it please use shortcode 'ca' and start again")
if __name__=='__main__':
  main()
    