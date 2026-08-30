import os, json, base64
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet, InvalidToken
from . import crypt_utils
# Button for open passwords file
# Use method with exceptions
# Click -> Open window -> Try open file -> Verifing word for check -> Password list parsing into object

check_words = [
    b'mt7lxS6IaM-ps-moolmore', b'vIaHPdoch6-ps-moolmore', b'ugSvdtSIQy-ps-moolmore', b'u0SroF0Dgc-ps-moolmore'
]

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
                _checkKeyValid(raw_dict=raw_dict, user_key=user_key)
            except Exception as e:
                raise ValueError(e)
            else:
                return _convertDataKeyList(raw_dict=raw_dict, user_key=user_key)
    else: raise ValueError('File not found!')


def saveFile(passwords: list, enc_key: bytes, file_path: str):
    # Save 4 check words & passwords dict
    dict_to_save = {}
    dict_to_save["check_word_01"]=crypt_utils.encryptOnePassword(check_words[0], enc_key).decode('utf-8')
    dict_to_save["check_word_02"]=crypt_utils.encryptOnePassword(check_words[1], enc_key).decode('utf-8')
    dict_to_save["check_word_03"]=crypt_utils.encryptOnePassword(check_words[2], enc_key).decode('utf-8')
    dict_to_save["check_word_04"]=crypt_utils.encryptOnePassword(check_words[3], enc_key).decode('utf-8')
    dict_to_save["passwords"] = passwords
    with open(file=file_path, mode='w', encoding='utf-8') as f:
        json.dump(obj=dict_to_save, ensure_ascii=False, fp=f, indent=1)


def _checkKeyValid(raw_dict: dict, user_key: bytes):
    # Check 4 decrypted check words via user input key 
    kdf = Argon2id(
    salt=b'gknboier',
    length=32,
    iterations=1,
    lanes=4,
    memory_cost=64 * 1024,
    )
    try:
        user_key = base64.urlsafe_b64encode(kdf.derive(user_key))

    except Exception as e:
        raise ValueError(e)
    else:
        for index in range(4):
            try:
                check_word = raw_dict.get(list(raw_dict.keys())[index])
                check_word = crypt_utils.decryptOnePassword(check_word, user_key)
                if check_word != check_words[index]:
                    raise ValueError('Key is wrong!')
            except InvalidToken:
                print('Parse: invalid token exception!')
                raise ValueError('Key is wrong!')
            except Exception as e:
                raise ValueError(e)

def _convertDataKeyList(raw_dict: dict, user_key: bytes) -> tuple:
    # Return encrypted_word + passwords
    kdf = Argon2id(
    salt=b'gknboier',
    length=32,
    iterations=1,
    lanes=4,
    memory_cost=64 * 1024,)
    
    return (base64.urlsafe_b64encode(kdf.derive(user_key)), raw_dict.get("passwords"))


















