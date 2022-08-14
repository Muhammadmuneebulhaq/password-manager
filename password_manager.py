'''Author: Muhammad Muneeb Ul Haq
Date started: 16 may 2022
Date completed: 18 may 2022'''
from cryptography.fernet import Fernet

'''with open("key.key","w") as key_file:
    # generate a key from the fernet package in cryptography module
    # and write it in a key file
    key = Fernet.generate_key()
    key_file.write(str(key))
'''
def load_key():
    '''returns the above generated key'''
    with open("key.key","r") as key_file:
        key = key_file.read()
        fernet = Fernet(key)
    return fernet
        
def add():
    '''The password is encrypted with the above key'''
    # take input
    account = str(input("Please enter account name:\n"))
    # encrypt
    pwd = Fernet.encrypt(load_key(),str(input("Please enter your password:\n")).encode())
    # write in file passwords
    with open("passwords.txt","a") as passw:
        passw.write(f"{account}|{pwd.decode()}\n")

def view():
    '''The password is ecrypted with the above key'''
    # access the file passwords
    with open("passwords.txt","r") as passw:
        # collect everything
        passwords = passw.readlines()
        # iterate through the lines
        for password in passwords:
            # remove any new line and split with |
            data = (password.rstrip("\n")).split("|")
            # printing the data
            print(f"Account:{data[0]}, Password:{str(Fernet.decrypt(load_key(),data[1].encode()))}")


if str(input("Please enter your master password:\n")) == "py@9792":

    while True:
        mode = str(input("What do you want to do?(view/add) \
    press q to quit.\n")).lower()

        
        if mode == "q":
            quit()
        elif mode == "add":
            add()
        elif mode == "view":
            view()
