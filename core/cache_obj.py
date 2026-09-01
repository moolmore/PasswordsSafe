import random
from types import NoneType
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from . import crypt_utils, lists_obj, key_obj
## DEBUG COLORS 
red = "\033[1;31m"  
yel = "\033[1;33m"  
gre = "\033[1;32m"  
res = "\033[0m"
## DEBUG COLORS
class CachedData():
    def __init__(self):
        self.ui_lists = {
            "service":[],
            "se_ni_de":[],
            "se_em_pa":[],
            "all":[]
        }
        self.search_hide_list = []
        self.search_dec_list = []
        self.user_path = ''
        self.visibility_list = 1
        self.search_input = ''
        self.search_active = False
        

def createCacheObject():
    global AppCache
    AppCache = CachedData()

def updateCache(list_visibility: int=0, user_path: str='None'):
    # 1: SERVICE
    # 2: SERVICE | NICKNAME | DESCRIPTION
    # 3: SERVICE | EMAIL | PASSWORD
    # 3: ALL DATA (! TEXT VERY SMALL !)
    passwords=lists_obj.UserPasswordsList.passwords_list

    private_key=key_obj.UserCryptoKey.key
    
    kdf = Argon2id(
        salt=b'gknboier',
        length=32,
        iterations=1,
        lanes=4,
        memory_cost=64 * 1024,
    )
    for key in list(AppCache.ui_lists.keys()):
        AppCache.ui_lists[key]=[]
    

    for data in passwords:
        print("data: "+str(data))
        #passwords: service ; nickname ; email ; password ; description
        AppCache.ui_lists["service"].append(data[0])
        AppCache.ui_lists["se_ni_de"].append(f"{data[0]}      {data[1]}      {data[4]}")
        AppCache.ui_lists["se_em_pa"].append(f"{data[0]}      {data[2]}      {data[3]}")
        AppCache.ui_lists["all"].append(f"{data[0]} {data[1]} {data[2]} {data[3]} {data[4]}")
    print(AppCache.ui_lists)
    if user_path != 'None':
        AppCache.user_path = user_path
    if list_visibility != 0:
        AppCache.visibility_list = list_visibility

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
