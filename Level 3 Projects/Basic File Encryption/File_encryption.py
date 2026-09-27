"""
Task 2: Basic File Encryption/Decryption
------------------------------------------
A simple command-line tool that encrypts and decrypts text files using
Fernet symmetric encryption (from the `cryptography` library).

Fernet is used instead of a Caesar cipher because it provides real,
secure encryption (AES-128 in CBC mode with HMAC authentication) while
still being simple to use in a script like this.

Usage:
    python file_crypto.py

You will be prompted to:
    1. Generate a new key (or reuse an existing one)
    2. Choose to encrypt or decrypt a file
    3. Provide the path to the input file
    4. The result is saved as a new file
"""

from cryptography.fernet import Fernet, InvalidToken
import os
import sys

KEY_FILE = "secret.key"


def generate_key():
    """Generate a new encryption key and save it to KEY_FILE."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print(f"New key generated and saved to '{KEY_FILE}'.")
    print("Keep this file safe — you need it to decrypt your files!")
    return key


def load_key():
    """Load the encryption key from KEY_FILE, or generate one if missing."""
    if not os.path.exists(KEY_FILE):
        print(f"No key found at '{KEY_FILE}'.")
        return generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()


def encrypt_file(input_path, key):
    """Encrypt the contents of input_path and save as a new .enc file."""
    if not os.path.exists(input_path):
        print(f"Error: file '{input_path}' not found.")
        return

    fernet = Fernet(key)

    with open(input_path, "rb") as f:
        data = f.read()

    encrypted_data = fernet.encrypt(data)

    output_path = input_path + ".enc"
    with open(output_path, "wb") as f:
        f.write(encrypted_data)

    print(f"File encrypted successfully -> '{output_path}'")


def decrypt_file(input_path, key):
    """Decrypt an encrypted file and save the result as a new file."""
    if not os.path.exists(input_path):
        print(f"Error: file '{input_path}' not found.")
        return

    fernet = Fernet(key)

    with open(input_path, "rb") as f:
        encrypted_data = f.read()

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except InvalidToken:
        print("Error: could not decrypt file. Wrong key or corrupted/invalid file.")
        return

    # Build output filename: strip ".enc" if present, else add ".dec"
    if input_path.endswith(".enc"):
        output_path = input_path[:-4] + ".dec"
    else:
        output_path = input_path + ".dec"

    with open(output_path, "wb") as f:
        f.write(decrypted_data)

    print(f"File decrypted successfully -> '{output_path}'")


def main():
    print("=== Basic File Encryption/Decryption Tool ===\n")

    key = load_key()

    while True:
        print("\nWhat would you like to do?")
        print("  1. Encrypt a file")
        print("  2. Decrypt a file")
        print("  3. Generate a new key (overwrites the old one)")
        print("  4. Quit")
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            path = input("Enter path to the text file to encrypt: ").strip()
            encrypt_file(path, key)

        elif choice == "2":
            path = input("Enter path to the encrypted file to decrypt: ").strip()
            decrypt_file(path, key)

        elif choice == "3":
            confirm = input(
                "This will make old encrypted files unreadable with the new key. "
                "Continue? (y/n): "
            ).strip().lower()
            if confirm == "y":
                key = generate_key()

        elif choice == "4":
            print("Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice, please enter a number from 1-4.")


if __name__ == "__main__":
    main()