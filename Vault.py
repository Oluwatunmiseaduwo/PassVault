import os
import json

from cryptography.fernet import Fernet

Vault_file = "Vault.json"
Key_file = "Secret.key"

def create_key():
    if not os.path.exists(Key_file):
        key = Fernet.generate_key()

        with open(Key_file, "wb") as file:
            file.write(key)

def load_key():
    with open(Key_file, "rb") as file:
        return file.read()

def encrypt_data(data):
    key = load_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(
        data.encode()
    )

    return encrypted.decode()

def decrypt_data(data):
    key = load_key()
    cipher = Fernet(key)
    decrypted = cipher.decrypt(
        data.encode()
    )

    return decrypted.decode()

def create_vault():

    if not os.path.exists(Vault_file):

        vault = {
            "entries": []
        }

        with open(Vault_file, "w") as file:
            json.dump(
                vault,
                file,
                indent=4
            )

def load_vault():
    with open(Vault_file, "r") as file:
        return json.load(file)

def save_vault(vault):
    with open(Vault_file, "w") as file:
        json.dump(
            vault, file, indent=4
        )