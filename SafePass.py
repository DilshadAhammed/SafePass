import random
import string
import json

PASSWORD_FILE = "passwords.json"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def save_password(account, password):
    try:
        with open(PASSWORD_FILE, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}

    data[account] = password

    with open(PASSWORD_FILE, 'w') as file:
        json.dump(data, file)
    print(f"Password for {account} saved successfully!")

def retrieve_password(account):
    try:
        with open(PASSWORD_FILE, 'r') as file:
            data = json.load(file)
            password = data.get(account)
            if password:
                print(f"Password for {account}: {password}")
            else:
                print(f"No password found for {account}.")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print(f"No passwords saved yet.")

def main():
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
            save_password(account, password)
        elif choice == "3":
            account = input("Enter account name: ")
            retrieve_password(account)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
