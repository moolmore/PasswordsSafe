import os, json, base64
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet, InvalidToken
from . import crypt_utils
# Button for open passwords file
# Use method with exceptions
# Click -> Open window -> Try open file -> Verifing word for check -> Password list parsing into object


def openFile(user_path: str, user_key: bytes) -> tuple:
    #Import json file in app and convert he in dict
    raw_dict = None
    if os.path.exists(user_path):
        try:
            with open(file=user_path, mode='r', encoding='utf-8') as f:
                raw_dict = json.load(f)
        except json.JSONDecodeError:
            raise ValueError('File is broken!')
        except Exception as e:
            raise ValueError(e)
        else:
            try:
                #Check user input key to valid via __keyVerif (valid word)
                _checkKeyValid(raw_dict=raw_dict, user_key=user_key)
            except Exception as e:
                raise ValueError(e)
            else:
                #Finally return dict with encrypted key

                return _convertDataKeyList(raw_dict=raw_dict, user_key=user_key)
    else: raise ValueError('File not found!')


def saveFile(passwords_dict: dict, enc_key: bytes, file_path: str):
    # Adding __keyVerif to dict
    passwords_dict = passwords_dict.copy()
    key_verif = crypt_utils.encryptOnePassword(password=b'_E5D6::::0000_', private_key=enc_key).decode('utf-8')
    passwords_dict['__keyVerif']=key_verif
    with open(file=file_path, mode='w', encoding='utf-8') as f:
        json.dump(obj=passwords_dict, ensure_ascii=False, fp=f, indent=1)


def _checkKeyValid(raw_dict: dict, user_key: bytes):
    kdf = Argon2id(
    salt=b'gknboier',
    length=32,
    iterations=1,
    lanes=4,
    memory_cost=64 * 1024,
    )
    try:
        user_key = base64.urlsafe_b64encode(kdf.derive(user_key))
        decoder = Fernet(key=user_key)
    except Exception as e:
        raise ValueError(e)
    else:
        if raw_dict.get('__keyVerif') != None:
            verifyWord = str(raw_dict.get('__keyVerif')).encode('utf-8')
            try:
                verifyWord = decoder.decrypt(token=verifyWord)
                
                if not verifyWord == b'_E5D6::::0000_':
                    raise ValueError('Key is wrong!')
            except InvalidToken:
                print('Parse: invalid token exception!')
                raise ValueError('Key is wrong!')
            except Exception as e:
                raise ValueError(e)
        else:
            raise ValueError('Key is wrong!')



def _convertDataKeyList(raw_dict: dict, user_key: bytes) -> tuple:
    kdf = Argon2id(
    salt=b'gknboier',
    length=32,
    iterations=1,
    lanes=4,
    memory_cost=64 * 1024,)

    enc_key = base64.urlsafe_b64encode(kdf.derive(user_key))

    passwords_dict = raw_dict.copy()
    passwords_dict.pop('__keyVerif')

    return (enc_key, passwords_dict)


















