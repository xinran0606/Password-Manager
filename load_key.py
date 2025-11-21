def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
        return key
