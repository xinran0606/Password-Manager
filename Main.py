from cryptography.fernet import Fernet
import add_and_view_account

while True:
    choi = input("Would you like to add a new password or view existing ones (view / add ), press q to quit? ").lower()
    if choi == "q":
        break
    elif choi == "view":
        add_and_view_account.view_account()
    elif choi == "add":
        add_and_view_account.add_account()
    else:
        print("Invalid mode. Please try again.")
        continue