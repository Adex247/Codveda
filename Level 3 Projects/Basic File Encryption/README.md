# File Encryption/Decryption Tool

A simple Python command-line tool that encrypts and decrypts text files using **Fernet symmetric encryption** (AES-128-CBC with HMAC authentication) from the `cryptography` library.

## Features

- Encrypt any file and save the result as a new `.enc` file
- Decrypt an encrypted file back to its original contents
- Auto-generates and stores an encryption key on first run
- Simple interactive menu — no command-line arguments needed

## Why Fernet instead of a Caesar cipher?

Fernet was chosen over a classic Caesar cipher because it provides real, secure symmetric encryption rather than a trivially reversible substitution. It combines AES-128 encryption with HMAC message authentication, so tampered or corrupted files are detected automatically on decryption.

## Requirements

- Python 3.7+
- [`cryptography`](https://pypi.org/project/cryptography/) package

Install the dependency with:

```bash
pip install cryptography
```

## Usage

Run the script:

```bash
python file_crypto.py
```

You'll be shown a menu:

```
=== Basic File Encryption/Decryption Tool ===

What would you like to do?
  1. Encrypt a file
  2. Decrypt a file
  3. Generate a new key (overwrites the old one)
  4. Quit
```

### Encrypting a file

1. Choose option `1`
2. Enter the path to the file you want to encrypt (e.g., `notes.txt`)
3. The encrypted output is saved alongside it as `notes.txt.enc`

### Decrypting a file

1. Choose option `2`
2. Enter the path to the encrypted file (e.g., `notes.txt.enc`)
3. The decrypted output is saved as `notes.txt.dec`

## Key management

- On first run, a key is generated and saved to `secret.key` in the working directory.
- This same key is reused for all future encrypt/decrypt operations.
- **Keep `secret.key` safe** — without it, encrypted files cannot be recovered.
- Choosing "Generate a new key" overwrites `secret.key`; any files encrypted with the old key will no longer be decryptable unless you keep a backup of that old key.

> ⚠️ `secret.key` should never be committed to version control. Add it to your `.gitignore`.

## Example

```bash
$ echo "Hello, world!" > message.txt
$ python file_crypto.py
# Choose 1, enter message.txt -> creates message.txt.enc

$ python file_crypto.py
# Choose 2, enter message.txt.enc -> creates message.txt.dec

$ cat message.txt.dec
Hello, world!
```

## License

This project is provided for educational purposes as part of a coursework assignment.
