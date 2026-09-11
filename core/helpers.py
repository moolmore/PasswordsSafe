
import os, base64
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from . import list_obj
import platform
## DEBUG COLORS 
red = "\033[1;31m"  
yel = "\033[1;33m"  
gre = "\033[1;32m"  
res = "\033[0m"
## DEBUG COLORS

data_block_names = [
    "service name",
    "username",
    "email",
    "password",
    "misc"
]

blocked_words = {
    r"\n",
    r"\n",
    r"\r",
    r"\r\n",
    r"\t",
    r"\x00",      
    r"\u0000",      
    r"\x08",
}

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
    if 6 >= len(user_input) >= 3: 
        if user_input.isascii():
            for symbol in list(user_input):
                if symbol == ' ':
                    raise ValueError('Key with whitespaces')
        else:
            raise ValueError('Key with not ascii symbols')
    else:
        raise ValueError('Key min 3 symbols and 6 max')

def CheckEditPassword(data_block: list):

    #if data_block in lists_obj.UserPasswordsList.passwords_list:
        #raise ValueError('This password block already exists.')
        
    for ind in range(5):
        data = data_block[ind]
        data_name = data_block_names[ind]
        data_len = len(data.replace(" ", ""))

        if ind != 4:
            if data_len <= 1:
                raise ValueError(f'Lenght of {data_name} <= 1.')

        for sym_ind in range(data_len):
            if data[sym_ind:sym_ind+data_len] in blocked_words:
                    raise ValueError(f'In {data_name} uses blocked words.')           

        if not data.isascii():
            raise ValueError(f"{data_name} not in ASCII symbols.")

    if not "@" in list(data_block[2]):
        raise ValueError('Email has not "@" symbol.')


def CheckNewPassword(data_block: list):

    if data_block in list_obj.UserPasswordsList.passwords_list:
        raise ValueError('This password block already exists.')
        
    for ind in range(5):
        data = data_block[ind]
        data_name = data_block_names[ind]
        data_len = len(data.replace(" ", ""))

        if ind != 4:
            if data_len <= 1:
                raise ValueError(f'Lenght of {data_name} <= 1.')

        for sym_ind in range(data_len):
            if data[sym_ind:sym_ind+data_len] in blocked_words:
                    raise ValueError(f'In {data_name} uses blocked words.')           

        if not data.isascii():
            raise ValueError(f"{data_name} not in ASCII symbols.")

    if not "@" in list(data_block[2]):
        raise ValueError('Email has not "@" symbol.')



