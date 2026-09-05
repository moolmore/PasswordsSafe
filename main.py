import platform
import csv
import os
from core import parse, lists_obj, key_obj, crypt_utils, cache_obj, helpers
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QGraphicsBlurEffect
from PySide6.QtCore import QTimer
from PySide6.QtGui import QFont
from pyqt_custom_titlebar_window import customTitlebarWindow
import sys
import pyperclip

if platform.system() == 'Darwin':
    from ui import main_menu_darwin as main_window
    from ui import add_password_darwin as add_password_window
    from ui import edit_password_darwin as edit_password_window
    from ui import new_file_darwin as new_file_window
    from ui import open_file_darwin as open_file_window
elif platform.system() == 'Windows':
    from ui import main_menu_win64 as main_window
    from ui import add_password_win64 as add_password_window
    from ui import edit_password_win64 as edit_password_window
    from ui import new_file_win64 as new_file_window
    from ui import open_file_win64 as open_file_window
else:
    raise ValueError('App "Passwords Safe" allows only macOS and Windows')

## DEBUG COLORS 
red = "\033[1;31m"  
yel = "\033[1;33m"  
gre = "\033[1;32m"  
res = "\033[0m"
## DEBUG COLORS

#App version
app_version = '2.0 WIP'

# All windows classes
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ManagmentElementsList = [
            # Только объекты, хозяин! (｡•́︿•̀｡)
            self.ui.OpenFile,
            self.ui.CreateFile,
            self.ui.VisibilityPassButton,
            self.ui.AddPassButton,
            self.ui.DeletePassButton,
            self.ui.EditPassButton,
            self.ui.CopyPassButton,
            self.ui.SearchButton,
            self.ui.Search_Input
        ]
        self.blurElements = self.ManagmentElementsList[2:9]
        self.blurElements.append(self.ui.label)
        self.blurElements.append(self.ui.label_2)
        self.ui.PasswordList.setWordWrap(True)
        

    def connectFunctions(self):
        self.ui.OpenFile.clicked.connect(executeOpenFile)
        self.ui.CreateFile.clicked.connect(executeNewFile)
        self.ui.VisibilityPassButton.clicked.connect(changePasswordsVisibility)
        self.ui.AddPassButton.clicked.connect(executeAddPassword)
        self.ui.DeletePassButton.clicked.connect(deletePassword)
        self.ui.EditPassButton.clicked.connect(executePasswordEdit)
        self.ui.CopyPassButton.clicked.connect(copyPassword)
        self.ui.SearchButton.clicked.connect(searchPassword)
        self.ui.Search_Input.textChanged.connect(checkSearchNull)
    ### DEBUG
    def connectDebSlots(self):
        self.ui.test1.clicked.connect(self.returnSelDataBlock)
        self.ui.test2.clicked.connect(self.importCSV)
        #self.ui.test3.clicked.connect()
        #self.ui.test4.clicked.connect()
    def returnSelDataBlock(self):
        userlist = lists_obj.UserPasswordsList.passwords_list
        # srch_map = cache_obj.AppCache.srch_ind_map
        ui_index = self.ui.PasswordList.currentRow()
        
        
        if cache_obj.AppCache.search_active:
            helpers.showDict(cache_obj.AppCache.srch_ind_map)
            app_index = cache_obj.AppCache.srch_ind_map[ui_index]
            data_block = userlist[app_index] 
        else:
            data_block = userlist[ui_index] 
        
        print("\n")
        for data in data_block:

            print(data if data != "" else "Пусто")
    def importCSV(self):
        path = os.path.expandvars(r"%USERPROFILE%//Documents//passwords.csv")
        with open(path, mode='r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Пропускаем заголовок, если он не нужен
            next(csv_reader) 
            for row in csv_reader:
                lists_obj.UserPasswordsList.passwords_list.append([row[0],row[2],"",row[3],row[4]])
            cache_obj.updateCache()
            Main_Window.updateList()
        
    ### DEBUG
    
    def enableAllButtons(self):
        for element in self.ManagmentElementsList:
            element.setEnabled(True)


    # 1: SERVICE
    # 2: SERVICE | NICKNAME | DESCRIPTION
    # 3: SERVICE | EMAIL | PASSWORD
    # 3: ALL DATA (! TEXT VERY SMALL !)
    def updateList(self):

        self.ui.PasswordList.clear()
        ac = cache_obj.AppCache
        print(yel+"updating Qt list...")
        print('Search active?', f"{gre}Yes" if cache_obj.AppCache.search_active else f"{red}No", res)
        font = QFont()
        font.setBold(True)
        font.setFamilies([u"Google Sans"])

        if cache_obj.AppCache.search_active:
            data_blocks = cache_obj.AppCache.ui_lists_srch
        else:
            data_blocks = cache_obj.AppCache.ui_lists_dflt
        
        if ac.visibility_list == 1:
            self.ui.PasswordList.addItems(data_blocks["service"])
            font.setPointSize(17)
            
            self.ui.PasswordList.setFont(font)
        elif ac.visibility_list == 2:
            self.ui.PasswordList.addItems(data_blocks["se_ni_de"])
            font.setPointSize(14)
            self.ui.PasswordList.setFont(font)

        elif ac.visibility_list == 3:
            font.setPointSize(14)
            self.ui.PasswordList.addItems(data_blocks["se_em_pa"])
            self.ui.PasswordList.setFont(font)

        elif ac.visibility_list == 4:
            font.setPointSize(12)
            font.setBold(False)
            self.ui.PasswordList.addItems(data_blocks["all"])
            self.ui.PasswordList.setFont(font)

        print("end of update"+res)

    # BLUR ON ELEMENTS OF MANAGMENT

    def setBlurOnElements(self):
        for element in self.blurElements:
            blur = QGraphicsBlurEffect()
            blur.setBlurRadius(3.5)  
            blur.setBlurHints(QGraphicsBlurEffect.QualityHint)
            element.setGraphicsEffect(blur)
            element.hash0 = blur


    def removeBlurFromElements(self):
        for element in self.blurElements:
            element.setGraphicsEffect(None)
            del element.hash0

    # BLUR ON ELEMENTS OF MANAGMENT

    def getCurItem(self) -> str:
        return self.ui.PasswordList.currentRow()
    def changeTitleSec(self):
        self.setWindowTitle('Passwords Safe' + ' - Password copied')
        QTimer.singleShot(1500, lambda: self.setWindowTitle('Passwords Safe'))
    
class OpenFileWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = open_file_window.Ui_Form()
        self.ui.setupUi(self)
    def connectFunctions(self):
        self.ui.ApplyButton.clicked.connect(applyOpenFile)
        self.ui.QuickDirButton.clicked.connect(setDirDialog)

    def showException(self, exc):
        self.ui.ErrorsLable.setVisible(True)
        self.ui.ErrorsIcon.setVisible(True)
        self.ui.ErrorsBack.setVisible(True)
        self.ui.ErrorsLable.setText(str(exc))

class NewFileWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = new_file_window.Ui_Form()
        self.ui.setupUi(self)
    def connectFunctions(self):
        self.ui.ApplyButton.clicked.connect(applyNewFile)
        self.ui.QuickDirButton.clicked.connect(setDirDialog)
    def showException(self, exc):
        self.ui.ErrorsLable.setVisible(True)
        self.ui.ErrorsIcon.setVisible(True)
        self.ui.ErrorsBack.setVisible(True)
        self.ui.ErrorsLable.setText(str(exc))

class EditPasswordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = edit_password_window.Ui_Form()
        self.ui.setupUi(self)
    def connectFunctions(self):
        self.ui.applyButton.clicked.connect(applyEditPassword)

class AddPasswordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = add_password_window.Ui_Form()
        self.ui.setupUi(self)
    def connectFunctions(self):
        self.ui.applyButton.clicked.connect(applyNewPassword)
# All windows classes



# Exectuions for open windows
# Exectuions for open windows

def executeMain():
    global Main_Window
    Main_Window = MainWindow()
    Main_Window.connectFunctions()
    Main_Window.connectDebSlots()
    Main_Window.setBlurOnElements()
    Main_Window.ui.lableVersion.setText(f'Platform: {platform.system()}    Version: {app_version}')
    Main_Window.ui.PasswordList.setVisible(False)
    Main_Window.show()

def executeOpenFile():
    global Open_File_Window
    Open_File_Window = OpenFileWindow()
    Open_File_Window.ui.ErrorsLable.setVisible(False)
    Open_File_Window.ui.ErrorsIcon.setVisible(False)
    Open_File_Window.ui.ErrorsBack.setVisible(False)
    Open_File_Window.connectFunctions()
    Open_File_Window.ui.PathInput.setText(helpers.preInputDir())
    Open_File_Window.show()

def executeNewFile():
    global New_File_Window
    New_File_Window = NewFileWindow()
    New_File_Window.ui.ErrorsLable.setVisible(False)
    New_File_Window.ui.ErrorsIcon.setVisible(False)
    New_File_Window.ui.ErrorsBack.setVisible(False)
    New_File_Window.connectFunctions()
    New_File_Window.ui.PathInput.setText(helpers.preInputDir())
    New_File_Window.show()

def executePasswordEdit():
    if Main_Window.ui.EditPassButton.isEnabled():
        global Edit_Password_Window
        Edit_Password_Window = EditPasswordWindow()
        Edit_Password_Window.connectFunctions()
        _name = Main_Window.ui.PasswordList.currentItem().text().split('  ')[0]
        _encPassword = lists_obj.UserPasswordsList.passwords_list.get(_name)
        _decPassword = crypt_utils.decryptOnePassword(password=str(_encPassword), private_key=key_obj.UserCryptoKey.key)
        # Edit_Password_Window.ui.currentName.setText(_name)
        # Edit_Password_Window.ui.currentPass.setText(_decPassword)
        Edit_Password_Window.ui.newNameEdit.setText(_name)
        Edit_Password_Window.ui.newPassEdit.setText(_decPassword)
        # Edit_Password_Window.ui.ErrorsLable_2.setVisible(False)
        Edit_Password_Window.show()

def executeAddPassword():
    if Main_Window.ui.AddPassButton.isEnabled():
        global Add_Pass_Window
        Add_Pass_Window = AddPasswordWindow()
        Add_Pass_Window.connectFunctions()
        #Add_Pass_Window.ui.ErrorsLable_2.setVisible(False)
        Add_Pass_Window.show()

# Exectuions for open windows
# Exectuions for open windows



# Buttons slots block start
# Buttons slots block start
# Buttons slots block start

def applyOpenFile():
    i_path = Open_File_Window.ui.PathInput
    i_key = Open_File_Window.ui.KeyInput
    try:
        _key, _passwords = parse.openFile(i_path.text(),i_key.text().encode('utf-8'))
    except Exception as e:
        Open_File_Window.showException(exc=e)
    else:
        lists_obj.createListObject(passwords=_passwords)
        key_obj.createKey(user_key=_key)
        cache_obj.createCacheObject()
        cache_obj.updateCache(list_visibility=1, user_path=i_path.text())          
        Open_File_Window.close()
        Main_Window.ui.lableListBackground.setText('')
        Main_Window.enableAllButtons()
        Main_Window.ui.PasswordList.setVisible(True)
        Main_Window.removeBlurFromElements()
        Main_Window.updateList()

def applyNewFile():
    i_key = New_File_Window.ui.KeyInput
    _path = New_File_Window.ui.PathInput
    try:
        helpers.checkNewKey(i_key.text())
        _key = crypt_utils.deriveKey(user_key=i_key.text().encode('utf-8'))

    except Exception as e:
        New_File_Window.showException(exc=e)
    else:
        lists_obj.createListObject(passwords=[])
        key_obj.createKey(user_key=_key)
        cache_obj.createCacheObject()
        cache_obj.updateCache(list_visibility=1, user_path=_path.text())
        New_File_Window.close()
        Main_Window.ui.lableListBackground.setText('')
        Main_Window.enableAllButtons()
        Main_Window.removeBlurFromElements()
        Main_Window.updateList()

def setDirDialog():
    dir, nonuse = QFileDialog.getOpenFileName(filter="JSON files (*.JSON)")
    Open_File_Window.ui.PathInput.setText(dir)
    New_File_Window.ui.PathInput.setText(dir)

def changePasswordsVisibility():
    co = cache_obj.AppCache
    print(gre+'Visibility was changes',co.visibility_list,"->",end=' ')

    if 4 > co.visibility_list>= 0:
        co.visibility_list += 1
    else:
        co.visibility_list = 1
    print(co.visibility_list)
    Main_Window.updateList()

def applyEditPassword():
    try:
        _newName = Edit_Password_Window.ui.newNameEdit.text()
        helpers.checkNewName(user_input=_newName, is_new_pass=False)
    except Exception as e:
        Edit_Password_Window.ui.ErrorsLable_2.setVisible(True)
        Edit_Password_Window.ui.ErrorsLable_2.setText(str(e))
    else:
        _newPass = Edit_Password_Window.ui.newPassEdit.text()
        lists_obj.UserPasswordsList.passwords_list.pop(Main_Window.getCurItem())
        lists_obj.UserPasswordsList.passwords_list[_newName]=crypt_utils.encryptOnePassword(password=_newPass.encode('utf-8'), private_key=key_obj.UserCryptoKey.key).decode('utf-8')
        cache_obj.updateCache()
        parse.saveFile(passwords_dict=lists_obj.UserPasswordsList.passwords_list,
                    enc_key=key_obj.UserCryptoKey.key,
                    file_path=cache_obj.AppCache.user_path)
        
        Main_Window.updateList()
        Edit_Password_Window.close()

def applyNewPassword():
    try:
        _newName = Add_Pass_Window.ui.newNameEdit.text()
        _newNickname = Add_Pass_Window.ui.newNicknameEdit.text()
        _newMail = Add_Pass_Window.ui.newMailEdit.text()
        _newPass = Add_Pass_Window.ui.newPassEdit.text()
        _newDisc = Add_Pass_Window.ui.newDescEdit.text()
        
    except Exception as e:
        Add_Pass_Window.ui.ErrorsLable_2.setVisible(True)
        Add_Pass_Window.ui.ErrorsLable_2.setText(str(e))
    else:
        passwords = lists_obj.UserPasswordsList.passwords_list
        passwords.insert(int(len(passwords)+1 if len(passwords) != 0 else 0), 
                         [_newName, _newNickname, _newMail, _newPass, _newDisc])
    
        cache_obj.updateCache()
        parse.saveFile()
        Main_Window.updateList()
        Add_Pass_Window.close()

def deletePassword():
    pass

def copyPassword():
    pass

def searchPassword():
    cache_obj.foundSearchResults(search_word=Main_Window.ui.Search_Input.text())
    cache_obj.AppCache.search_active = True
    print('show dict after fsr')
    print(cache_obj.AppCache.srch_ind_map)
    Main_Window.updateList()

def checkSearchNull():
    if Main_Window.ui.Search_Input.text() == ''.strip():
        cache_obj.AppCache.search_active = False
        Main_Window.ui.Search_Input.clearFocus()
        Main_Window.updateList()

# Buttons slots block end
# Buttons slots block end
# Buttons slots block end

def main():
    
    App = QApplication()
    executeMain()
    sys.exit(App.exec())
    

if __name__ == '__main__':
    main()
    












