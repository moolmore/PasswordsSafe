from cryptography.fernet import Fernet

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


