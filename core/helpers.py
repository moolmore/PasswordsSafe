
import os, base64
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id



from . import lists_obj
import platform



def processNewFile(user_key, user_path) -> tuple:
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
        return (enc_key, user_path)

def preInputDir() -> str:
    if platform.system() == "Darwin":
        return os.path.expandvars(r'$HOME/Documents/passwords.json')
    elif platform.system() == 'Windows':
        return os.path.expandvars(r'%USERPROFILE%\Documents\passwords.json')
    elif platform.system() == 'Linux':
        return os.path.expandvars(r'$XDG_DOCUMENTS_DIR/passwords.json')
    else:
        return ''

def checkNewKey(user_input: str) -> None:
    """
    func only raise exceptions
    """
    if 6 >= len(user_input) >= 3: 
        if user_input.isascii():
            for symbol in list(user_input):
                if symbol == ' ':
                    raise ValueError('Key with whitespaces')
        else:
            raise ValueError('Key with not ascii symbols')
    else:
        raise ValueError('Key min 3 symbols and 6 max')

def checkNewName(user_input: str) -> None:
    if 15 >= len(user_input) >= 3: 
        if user_input.isascii():
                    for symbol in list(user_input):
                        if symbol == ' ':
                            raise ValueError('Key with whitespaces')
                    if user_input in list(lists_obj.UserPasswordsList.passwords_list.keys()):
                        raise ValueError('Name alredy uses')
                    if user_input == '__keyVerif':
                        raise ValueError('This name is blocked')             
        else:
            raise ValueError('Key with not ascii symbols')
    else:
        raise ValueError('Key min 3 symbols and 15 max')


