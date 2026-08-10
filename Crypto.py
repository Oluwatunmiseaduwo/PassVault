import os
import base64
import hashlib

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

Salt_file = "salt.bin"

def get_salt():
    if not os.path.exists(Salt_file):
      salt = os.urandom(16)
      with open(Salt_file, "wb") as file:
          file.write(salt)

    with open(Salt_file, "rb") as file:
        return file.read()

def hash_master_password(password):
    salt = get_salt()

    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        600000
    ).hex()

def derive_key(password):
    salt = get_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600000
    )
    
    key = base64.urlsafe_b64encode(
        kdf.derive(password.encode())
    )
    
    return key

def encrypt(text, password):
    key = derive_key(password)
    cipher = Fernet(key)

    encrypted = cipher.encrypt(
        text.encode()
    )
    return encrypted.decode()


def decrypt(token, password):
    key = derive_key(password)
    cipher = Fernet(key)

    decrypted = cipher.decrypt(
        token.encode()
    )
    return decrypted.decode()