import random
from types import NoneType
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from . import crypt_utils, list_obj, key_obj, helpers
import hashlib

## DEBUG COLORS 
red = "\033[1;31m"  
yel = "\033[1;33m"  
gre = "\033[1;32m"  
res = "\033[0m"
## DEBUG COLORS
class CachedData():
    def __init__(self):
        self.ui_lists_dflt = {
            "service":[],
            "se_ni_de":[],
            "se_em_pa":[],
            "all":[]
        }
        self.ui_lists_srch = self.ui_lists_dflt.copy()
        self.dflt_ind_map = {}
        self.srch_ind_map = {}
        self.srch_word = ''
        self.user_path = ''
        self.visibility_list = 1
        self.search_input = ''
        self.search_active = False

    

def createCacheObject() -> None:
    global AppCache
    AppCache = CachedData()

def updateCache(list_visibility: int=0, user_path: str='None') -> None:
    # 1: SERVICE
    # 2: SERVICE | NICKNAME | DESCRIPTION
    # 3: SERVICE | EMAIL | PASSWORD
    # 3: ALL DATA (! TEXT VERY SMALL !)
    passwords=list_obj.UserPasswordsList.passwords_list
    passwords.sort()
    #Clear the cache list values
    for key in list(AppCache.ui_lists_dflt.keys()):
        AppCache.ui_lists_dflt[key]=[]
    _writeUILists(passwords, "dflt")
    if AppCache.search_active:
        foundSearchResults(search_word=AppCache.srch_word)
    if user_path != 'None':
        AppCache.user_path = user_path


def foundSearchResults(search_word: str) -> None:
    search_word = search_word.lower()
    ln_sw = len(search_word)
    passwords = list_obj.UserPasswordsList.passwords_list
    founded_blocks = []

    # Searching algorithm
    for data_block in passwords.copy():
        # search in 4 data_type: 0 service | 1 name | 2 email | 3 password(skipped) | 4 misc
        for data_type in range(5):
            if data_type == 3:
                #Skipping the password
                continue
            for index in range(len(data_block[data_type])):
                # gets data block -> get data(username for example) -> 
                # data[sequential index of len data : sequential index of len data + len of search word].
                # for example: data is "Apple", search word is "ple", for loop algorithm:
                # 0 sequential: Apple -> plele, 1 seq.: Apple -> Aplee, 2 seq.: Apple -> Apple and searchable data is founded
                data = data_block[data_type][index:(index+ln_sw)].lower()
                if data == search_word:
                    founded_blocks.append(data_block)
                    break

    #Algorithm may be founded same data from username and misc data
    #Thats why he deletes the same data blocks
    for data_block in founded_blocks:
        while founded_blocks.count(data_block) != 1:
            founded_blocks.pop(founded_blocks.index(data_block))


    #Sorting in alphabet
    founded_blocks.sort()

    # Clearing and rewrite Qt UI search results lists
    for key in list(AppCache.ui_lists_srch.keys()):
        AppCache.ui_lists_srch[key]=[]
    _writeUILists(founded_blocks, "srch")
    
    

    # Write search results to indexes map because apps get item from list via Qt UI index
    # UI LIST INDEX : APP LIST
    AppCache.srch_word = search_word
    _writeSearchIndMap(srch_passwords=founded_blocks)

def _writeUILists(passwords: list, type: str) -> None:
    if type == 'dflt':
        ui_list = AppCache.ui_lists_dflt
    elif type == 'srch':
        ui_list = AppCache.ui_lists_srch
    
    for data in ui_list.keys():
        ui_list[data] = []

    for data in passwords:
        ui = (
            f"• Service: {data[0]}",
            f"• Nickname: {data[1]}",
            f"• Email: {data[2]}",
            f"• Password: {data[3]}",
            f"• Misc: {data[4]}"
        )
        ui_list["service"].append(data[0])
        ui_list["se_ni_de"].append(ui[0]+"\n"+ui[1]+"\n"+ui[4])
        ui_list["se_em_pa"].append(ui[0]+"\n"+ui[2]+"\n"+ui[3])
        ui_list["all"].append(ui[0]+"\n"+ui[1]+"\n"+ui[2]+"\n"+ui[3]+"\n"+ui[4])

def _writeSearchIndMap(srch_passwords: str) -> None:
    srch_map = AppCache.srch_ind_map
    passwords = list_obj.UserPasswordsList.passwords_list
    for x in range(len(srch_map)):
        del srch_map[x]
    for ind, word in enumerate(srch_passwords):
        srch_map[ind]=int(passwords.index(word))