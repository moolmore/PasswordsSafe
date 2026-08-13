import random, time
from types import NoneType
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id



from . import crypt_utils, lists_obj, key_obj

class CachedData():
    def __init__(self):
        self.hide_list = []
        self.dec_list = []
        self.search_hide_list = []
        self.search_dec_list = []
        self.user_path = ''
        self.visibility_list = ''
        self.search_input = ''
        self.search_active = False
        

def createCacheObject():
    global AppCache
    AppCache = CachedData()

def updateCache(list_visibility: str='None', user_path: str='None'):
    private_dict=lists_obj.UserPasswordsList.passwords_list
    private_key=key_obj.UserCryptoKey.key
    hide_list = [] 
    decrypted_list = []
    kdf = Argon2id(
        salt=b'gknboier',
        length=32,
        iterations=1,
        lanes=4,
        memory_cost=64 * 1024,
    )

    for key, value in private_dict.items():
        hide_list.append(key+" | "+"[##"+"#"*random.randint(2, 5)+"]")
        decrypted_list.append(key+"  "+crypt_utils.decryptOnePassword(password=value, private_key=private_key)) 


    if user_path != 'None':
        AppCache.user_path = user_path
    if list_visibility != 'None':
        AppCache.visibility_list = list_visibility

    AppCache.hide_list = hide_list
    AppCache.dec_list = decrypted_list

def updateCacheSearchResults(search_word: str|NoneType=None):
    AppCache.search_hide_list = []
    AppCache.search_dec_list = []
    if search_word == None:
        search_word = AppCache.search_input
    else:
        AppCache.search_input = search_word
    
    if search_word.strip() != '':
        results_list = _searchWordCache(search_word=search_word, names_list=list(lists_obj.UserPasswordsList.passwords_list.keys()))
        if results_list != []:
            for result in results_list:
                AppCache.search_hide_list.append(result+"  "+"[##"+"#"*random.randint(2, 5)+"]")
                AppCache.search_dec_list.append(result+"  "+crypt_utils.decryptOnePassword(password=lists_obj.UserPasswordsList.passwords_list[result], private_key=key_obj.UserCryptoKey.key) )

def _searchWordCache(search_word: str, names_list: list[str]) -> list:
    founded_words = []
    search_word = search_word.strip().lower()
    for object in names_list:
        if search_word == object.lower():
            founded_words.append(object)
        else:
            if object[0:len(search_word)].lower() == search_word:
                founded_words.append(object)
    return founded_words
