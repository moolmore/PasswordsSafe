

class CryptoKey:
    def __init__(self):
        #Storage private_key, not user public
        self.__key = b''
    
    @property
    def key(self) -> bytes:
        return self.__key

    @key.setter
    def key(self, value: bytes):
        self.__key = value


def createKey(user_key: bytes):
    global UserCryptoKey
    UserCryptoKey = CryptoKey()
    UserCryptoKey.key = user_key







