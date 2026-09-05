import random
from types import NoneType
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from . import crypt_utils, lists_obj, key_obj, helpers
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
    passwords.sort()
    #Clear the cache list values
    for key in list(AppCache.ui_lists_dflt.keys()):
        AppCache.ui_lists_dflt[key]=[]
    _writeUILists(passwords, "dflt")
    if user_path != 'None':
        AppCache.user_path = user_path

def foundSearchResults(search_word: str):
    search_word = search_word.lower()
    ln_sw = len(search_word)
    passwords = lists_obj.UserPasswordsList.passwords_list
    founded_blocks = []

    
    for data_block in passwords.copy():
        # search in 3 data_type: 0 service | 1 name | 2 email
        for data_type in range(3):
            if data_type == 2:
                data_block[data_type] = data_block[data_type].split('@')[0]
            for index in range(len(data_block[data_type])):
                data = data_block[data_type][index:(index+ln_sw)].lower()
                if data == search_word:
                    founded_blocks.append(data_block)
                    break
    for data_block in founded_blocks:
        while founded_blocks.count(data_block) != 1:
            founded_blocks.pop(founded_blocks.index(data_block))
    founded_blocks.sort()
    # SEARCH IN NICKNAMES
    # SEARCH IN EMAILS

    for key in list(AppCache.ui_lists_srch.keys()):
        AppCache.ui_lists_srch[key]=[]
    _writeUILists(founded_blocks, "srch")
    # Write search results to indexes map
    # UI LIST INDEX : APP LIST
    _writeSearchIndMap(srch_passwords=founded_blocks)

    helpers.showDict(AppCache.srch_ind_map)

#def foundSearchResults(search_word: str) -> bool | None 

def _writeUILists(passwords: list, type: str):
    if type == 'dflt':
        print('Writing default cache list')
        ui_list = AppCache.ui_lists_dflt
    elif type == 'srch':
        print('Writing search cache list')
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

def _writeSearchIndMap(srch_passwords: str):
    srch_map = AppCache.srch_ind_map
    passwords = lists_obj.UserPasswordsList.passwords_list
    for x in range(len(srch_map)):
        del srch_map[x]
    for ind, word in enumerate(srch_passwords):
        srch_map[ind]=int(passwords.index(word))
    print('srch map is writed')