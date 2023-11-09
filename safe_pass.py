from cryptography.fernet import Fernet
import json
import os

PASSWORD_FILE = "passwords.json"
KEY_FILE = "key.key"

def generate_key():
    return Fernet.generate_key()

def load_key():
    return open(KEY_FILE, "rb").read()

def save_key(key):
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

def save_password(account, password, key):
    try:
        with open(PASSWORD_FILE, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}

    encrypted_password = encrypt_password(password, key)
    data[account] = encrypted_password

    with open(PASSWORD_FILE, 'w') as file:
        json.dump(data, file)
    print(f"Password for {account} saved successfully!")

def retrieve_password(account, key):
    try:
        with open(PASSWORD_FILE, 'r') as file:
            data = json.load(file)
            encrypted_password = data.get(account)
            if encrypted_password:
                password = decrypt_password(encrypted_password, key)
                print(f"Password for {account}: {password}")
            else:
                print(f"No password found for {account}.")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print(f"No passwords saved yet.")

def main():
    if not os.path.exists(KEY_FILE):
        key = generate_key()
        save_key(key)
    else:
        key = load_key()

    print("Welcome to SafePass!")
    while True:
        print("\nMenu:")
        print("1. Generate Password")
        print("2. Save Password")
        print("3. Retrieve Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")
        elif choice == "2":
            account = input("Enter account name: ")
            password = input("Enter password: ")
            save_password(account, password, key)
        elif choice == "3":
            account = input("Enter account name: ")
            retrieve_password(account, key)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
