# SafePass

SafePass is a command-line interface (CLI) tool developed in Python that allows users to generate strong passwords, store them securely, and retrieve passwords when needed. The program encrypts passwords before storing them, ensuring data security.

## Features

- **Password Generation:** Generate strong and complex passwords with customizable length and complexity.
- **Secure Storage:** Encrypt and securely store passwords along with account names.
- **Password Retrieval:** Retrieve stored passwords for specific accounts.
- **Encryption:** Utilizes the cryptography library for password encryption and decryption.
- **Key Management:** Handles encryption key generation and storage.

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/SafePass.git
   cd SafePass
   ```

## Usage

1. Run the SafePass program:
   ```shell
   python safe_pass.py
   ```
3. Select options from the menu to generate, save, and retrieve passwords.
4. Passwords are stored in encrypted format in the passwords.json file.
5. The encryption key is stored in the key.key file. Keep it secure and do not share it.
