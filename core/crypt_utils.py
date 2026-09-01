from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id

def decryptOnePassword(password: str | bytes, private_key: bytes) -> str:
    try:
        f = Fernet(key=private_key)
        password = f.decrypt(password)
    except Exception as e:
        print(e)
        return('DECR_ERROR')
    else:
        return password.decode('utf-8')

def encryptOnePassword(password: bytes, private_key: bytes) -> bytes:
    try:
        f = Fernet(key=private_key)
        password = f.encrypt(password)
    except Exception as e:
        print(e)
        raise ValueError('ENCR_ERROR')
    else:
        return password

def deriveKey(user_key) -> bytes:
    kdf = Argon2id(
    salt=b'gknboier',
    length=32,
    iterations=1,
    lanes=4,
    memory_cost=64 * 1024,)
    try:
        enc_key = base64.urlsafe_b64encode(kdf.derive(user_key))
    except Exception as e:
        raise ValueError(e)
    else:
        return enc_key