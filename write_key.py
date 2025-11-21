from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    key_file = open("key.key", "wb")
    key_file.write(key)
    key_file.close()

write_key()

