import os, json, base64
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet, InvalidToken
from . import crypt_utils
# Button for open passwords file
# Use method with exceptions
# Click -> Open window -> Try open file -> Verifing word for check -> Password list parsing into object

## DEBUG COLORS 
red = "\033[1;31m"  
yel = "\033[1;33m"  
gre = "\033[1;32m"  
res = "\033[0m"
## DEBUG COLORS

check_words = [
    b'mt7lxS6IaM-ps-moolmore01', 
    b'vIaHPdoch6-ps-moolmore02', 
    b'ugSvdtSIQy-ps-moolmore03', 
    b'u0SroF0Dgc-ps-moolmore04'
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
                _key = crypt_utils.deriveKey(user_key)
                enc_passwords = raw_dict.get("passwords")
                dec_passwords = []
                for password_block in enc_passwords:
                    new_pass_block = []
                    for element in password_block:
                        new_pass_block.append(crypt_utils.decryptOnePassword(element.encode("utf-8"), _key))
                    dec_passwords.append(new_pass_block)
                return (_key, dec_passwords)
                

    else: raise ValueError('File not found!')


def saveFile(passwords: list, enc_key: bytes, file_path: str):
    # Save 4 check words & passwords dict
    enc_passwords = []
    for password_block in passwords:
        new_pass_block = []
        for element in password_block:
            new_pass_block.append(crypt_utils.encryptOnePassword(element.encode("utf-8"), enc_key).decode("utf-8"))
        enc_passwords.append(new_pass_block)
    dict_to_save = {}
    for index in range(4):
        dict_to_save[f"check_word_0{index}"]=crypt_utils.encryptOnePassword(check_words[index], enc_key).decode('utf-8')
    dict_to_save["passwords"] = enc_passwords

    with open(file=file_path, mode='w', encoding='utf-8') as f:
        json.dump(obj=dict_to_save, ensure_ascii=False, fp=f, indent=1)
    print(gre+"JSON file is saved"+res)


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
                if check_word != check_words[index].decode('utf-8'):
                    print(red,'PARSE / CHECK KEY VALID file cw not same')
                    print("file:",check_word,"app:",check_words[index],res)
                    raise ValueError('Key is wrong!')
            except InvalidToken:
                print('Parse: invalid token exception!')
                raise ValueError('Key is wrong!')
            except Exception as e:
                raise ValueError(e)




















