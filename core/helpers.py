
import os, base64
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from . import lists_obj
import platform
import asyncio
## DEBUG COLORS 
red = "\033[1;31m"  
yel = "\033[1;33m"  
gre = "\033[1;32m"  
res = "\033[0m"
## DEBUG COLORS


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

def checkNewName(user_input: str, is_new_pass: bool) -> None:
    if 15 >= len(user_input) >= 3: 
        if user_input.isascii():
                    for symbol in list(user_input):
                        if symbol == ' ':
                            raise ValueError('Key with whitespaces')
                    if is_new_pass:
                        if user_input in list(lists_obj.UserPasswordsList.passwords_list.keys()):
                            raise ValueError('Name alredy uses')
                    if user_input == '__keyVerif':
                        raise ValueError('This name is blocked')             
        else:
            raise ValueError('Key with not ascii symbols')
    else:
        raise ValueError('Key min 3 symbols and 15 max')



