from cryptography.fernet import Fernet
import load_key

key = load_key.load_key()
fer = Fernet(key)

def add_account():
    '''THis Funktion will be used to add an account in password.txt'''
    name = input("Account Name: ")
    pwd = input("Password: ")
    while True:
        pwd_check = input("Please type your password again to check: ")
        if pwd_check != pwd:
            print("❌ Passwords do not match. Please try again.\n")
            continue
        else:
            print("✅ Password confirmed.")
            break
    with open('password.txt', 'a') as passwordFile:
        passwordFile.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


def view_account():
    '''This funktion will be used to view all the accounts in password.txt'''
    with open('password.txt', 'r') as passwordFile:
        for line in passwordFile.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(pwd.encode()).decode())
