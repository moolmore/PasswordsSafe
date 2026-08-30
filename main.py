import platform
from core import parse, lists_obj, key_obj, crypt_utils, cache_obj, helpers
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QGraphicsBlurEffect
from PySide6.QtCore import QTimer
import sys
import random
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

#App version
app_version = '2.1'

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
    def enableAllButtons(self):
        for element in self.ManagmentElementsList:
            element.setEnabled(True)
    def updateList(self):
        self.ui.PasswordList.clear()
        if cache_obj.AppCache.search_active:
            if cache_obj.AppCache.visibility_list == 'hide':
                self.ui.PasswordList.addItems(cache_obj.AppCache.search_hide_list)
            else:
                self.ui.PasswordList.addItems(cache_obj.AppCache.search_dec_list)
        else:
            if cache_obj.AppCache.visibility_list == 'hide':
                self.ui.PasswordList.addItems(cache_obj.AppCache.hide_list)
            else:
                self.ui.PasswordList.addItems(cache_obj.AppCache.dec_list)
        self.ui.PasswordList.sortItems()

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
        return self.ui.PasswordList.currentItem().text().split('  ')[0]
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
    Main_Window.setBlurOnElements()
    Main_Window.ui.lableVersion.setText(f'Platform: {platform.system()}    Version: {app_version}')
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
        Edit_Password_Window.ui.currentName.setText(_name)
        Edit_Password_Window.ui.currentPass.setText(_decPassword)
        Edit_Password_Window.ui.newNameEdit.setText(_name)
        Edit_Password_Window.ui.newPassEdit.setText(_decPassword)
        Edit_Password_Window.ui.ErrorsLable_2.setVisible(False)
        Edit_Password_Window.show()

def executeAddPassword():
    if Main_Window.ui.AddPassButton.isEnabled():
        global Add_Pass_Window
        Add_Pass_Window = AddPasswordWindow()
        Add_Pass_Window.connectFunctions()
        Add_Pass_Window.ui.ErrorsLable_2.setVisible(False)
        Add_Pass_Window.show()

# Exectuions for open windows
# Exectuions for open windows



# Buttons slots block start
# Buttons slots block start
# Buttons slots block start

def applyOpenFile():
    try:
        _key, _dict = parse.openFile(user_path=Open_File_Window.ui.PathInput.text(),
                                     user_key=Open_File_Window.ui.KeyInput.text().encode('utf-8'))
    except Exception as e:
        Open_File_Window.showException(exc=e)
    else:
        lists_obj.createListObject(passwords=_dict)
        key_obj.createKey(user_key=_key)
        cache_obj.createCacheObject()
        cache_obj.updateCache(list_visibility='hide', user_path=Open_File_Window.ui.PathInput.text())          
        Open_File_Window.close()
        Main_Window.ui.lableListBackground.setText('')
        #Show list in app
        Main_Window.enableAllButtons()
        Main_Window.removeBlurFromElements()
        Main_Window.updateList()

def applyNewFile():
    try:
        helpers.checkNewKey(New_File_Window.ui.KeyInput.text())
        _key, _path = helpers.processNewFile(user_key=New_File_Window.ui.KeyInput.text().encode('utf-8'), user_path=New_File_Window.ui.PathInput.text())
    except Exception as e:
        New_File_Window.showException(exc=e)
    else:
        lists_obj.createListObject(passwords={})
        key_obj.createKey(user_key=_key)
        cache_obj.createCacheObject()
        cache_obj.updateCache(list_visibility='hide', user_path=_path)
        New_File_Window.close()
        Main_Window.ui.lableListBackground.setText('')
        #Show list in app
        Main_Window.enableAllButtons()
        Main_Window.removeBlurFromElements()
        Main_Window.updateList()

def setDirDialog():
    dir, nonuse = QFileDialog.getOpenFileName(filter="JSON files (*.JSON)")
    Open_File_Window.ui.PathInput.setText(dir)
    New_File_Window.ui.PathInput.setText(dir)
def changePasswordsVisibility():
    if cache_obj.AppCache.visibility_list == 'hide':
        cache_obj.AppCache.visibility_list = 'decrypted'
    else:
        cache_obj.AppCache.visibility_list = 'hide'
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
        
        cache_obj.updateCacheSearchResults()
        Main_Window.updateList()
        Edit_Password_Window.close()

def applyNewPassword():
    try:
        _newName = Add_Pass_Window.ui.newNameEdit.text()
        helpers.checkNewName(user_input=_newName, is_new_pass=True)
    except Exception as e:
        Add_Pass_Window.ui.ErrorsLable_2.setVisible(True)
        Add_Pass_Window.ui.ErrorsLable_2.setText(str(e))
    else:
        _newPass = Add_Pass_Window.ui.newPassEdit.text()
        lists_obj.UserPasswordsList.passwords_list[_newName]=crypt_utils.encryptOnePassword(password=_newPass.encode('utf-8'), private_key=key_obj.UserCryptoKey.key).decode('utf-8')
        cache_obj.updateCache()
        parse.saveFile(passwords_dict=lists_obj.UserPasswordsList.passwords_list,
                    enc_key=key_obj.UserCryptoKey.key,
                    file_path=cache_obj.AppCache.user_path)
        cache_obj.updateCacheSearchResults()
        Main_Window.updateList()
        Add_Pass_Window.close()

def deletePassword():

    lists_obj.UserPasswordsList.passwords_list.pop(Main_Window.getCurItem())
    cache_obj.updateCache()
    parse.saveFile(passwords_dict=lists_obj.UserPasswordsList.passwords_list,
                       enc_key=key_obj.UserCryptoKey.key,
                       file_path=cache_obj.AppCache.user_path)
    cache_obj.updateCacheSearchResults()
    Main_Window.updateList()
    

def copyPassword():
    _pass = lists_obj.UserPasswordsList.passwords_list.get(Main_Window.getCurItem(), '')
    _pass = crypt_utils.decryptOnePassword(password=_pass, private_key=key_obj.UserCryptoKey.key)
    pyperclip.copy(text=_pass)
    Main_Window.changeTitleSec()

def searchPassword():
    user_input = Main_Window.ui.Search_Input.text()
    if user_input != ''.strip():
        cache_obj.updateCacheSearchResults(search_word=user_input)
        cache_obj.AppCache.search_active = True
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












