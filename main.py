# (｡•́︿•̀｡)
import platform, csv, os
from core import parse, key_obj, crypt_utils, cache_obj, helpers, list_obj
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QGraphicsBlurEffect
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont
import sys
import pyperclip


if platform.system() == 'Darwin':
    pass
    #Change font size on macOS

from ui import edit_add_password, main_menu, new_file, open_file

## DEBUG COLORS 
red = "\033[1;31m"  
yel = "\033[1;33m"  
gre = "\033[1;32m"  
res = "\033[0m"
## DEBUG COLORS

#App version
app_version = '2.1.1'

# All windows classes
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = main_menu.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PasswordList.setWordWrap(True)
        self.connectFunctions()
        self.setBlurOnElements(True)
        self.ui.manage.setEnabled(False)
        self.ui.search.setEnabled(False)
        self.ui.lableVersion.setText(f'Platform: {platform.system()}    Version: {app_version}')
        self.ui.PasswordList.setVisible(False)
        self.ui.settings_frame.setVisible(False)
        

    def connectFunctions(self):
        self.ui.OpenFile.clicked.connect(executeOpenFile)
        self.ui.CreateFile.clicked.connect(executeNewFile)
        self.ui.VisibilityPassButton.clicked.connect(changePasswordsVisibility)
        self.ui.AddPassButton.clicked.connect(executeAddPassword)
        self.ui.DeletePassButton.clicked.connect(deletePassword)
        self.ui.EditPassButton.clicked.connect(executePasswordEdit)
        self.ui.CopyNameButton.clicked.connect(copyUsername)
        self.ui.CopyEmailButton.clicked.connect(copyEmail)
        self.ui.CopyPassButton.clicked.connect(copyPassword)
        self.ui.Search_Input.textChanged.connect(checkSearchNull)
        self.ui.settings.clicked.connect(executeSettings)
    ### DEBUG

    def importCSV(self):
        path = os.path.expandvars(r"%USERPROFILE%//Documents//passwords.csv")
        with open(path, mode='r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Пропускаем заголовок, если он не нужен
            next(csv_reader) 
            for row in csv_reader:
                list_obj.UserPasswordsList.passwords_list.append([row[0],row[2],"",row[3],row[4]])
            cache_obj.updateCache()
            Main_Window.updateList()

    ### DEBUG
    
    def enableManageAndSearch(self):
        Main_Window.ui.manage.setEnabled(True)
        Main_Window.ui.search.setEnabled(True)

    def updateList(self):

        self.ui.PasswordList.clear()
        ac = cache_obj.AppCache
        font = QFont()
        font.setBold(True)
        font.setFamilies([u"Google Sans"])

        if ac.search_active:
            data_blocks = ac.ui_lists_srch
        else:
            data_blocks = ac.ui_lists_dflt

        font.setPointSize(14)
        self.ui.PasswordList.addItems(data_blocks[list(data_blocks.keys())[ac.visibility_list-1]]) 
        if ac.visibility_list == 1:
            font.setPointSize(17)
        elif ac.visibility_list == 4:
            font.setPointSize(12)
            font.setBold(False)
        self.ui.PasswordList.setFont(font)

    def setBlurOnElements(self, turn_on):
        if turn_on:
            self.blur=QGraphicsBlurEffect()
            self.blur.setBlurRadius(4)  
            self.blur.setBlurHints(QGraphicsBlurEffect.QualityHint)

            self.blur2=QGraphicsBlurEffect()
            self.blur2.setBlurRadius(4)  
            self.blur2.setBlurHints(QGraphicsBlurEffect.QualityHint)
        else:
            del self.blur
            del self.blur2
        self.ui.manage.setGraphicsEffect(self.blur if turn_on else None)
        self.ui.search.setGraphicsEffect(self.blur2 if turn_on else None)

    def setOffAndBlurredList(self, turn_on):
        self.list_blur = QGraphicsBlurEffect()
        self.list_blur.setBlurHints(QGraphicsBlurEffect.QualityHint)
        self.ui.PasswordList.setGraphicsEffect(self.list_blur if turn_on else None)
        self.ui.PasswordList.setEnabled(False if turn_on else True)
        if not turn_on:
            del self.list_blur

    def getCurItem(self) -> int:
        if not cache_obj.AppCache.search_active:
            return self.ui.PasswordList.currentRow()
        else:
            return cache_obj.AppCache.srch_ind_map[self.ui.PasswordList.currentRow()]

    def changeTitleSec(self):
        self.setWindowTitle('Passwords Safe' + ' - Password copied')
        QTimer.singleShot(1500, lambda: self.setWindowTitle('Passwords Safe'))
    
class OpenFileWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = open_file.Ui_Form()
        self.ui.setupUi(self)
        self.connectFunctions()
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
        self.ui = new_file.Ui_Form()
        self.ui.setupUi(self)
        self.connectFunctions()
    def connectFunctions(self):
        self.ui.ApplyButton.clicked.connect(applyNewFile)
        self.ui.QuickDirButton.clicked.connect(setDirDialog)
    def showException(self, exc):
        self.ui.ErrorsLable.setVisible(True)
        self.ui.ErrorsIcon.setVisible(True)
        self.ui.ErrorsBack.setVisible(True)
        self.ui.ErrorsLable.setText(str(exc))

class AddPasswordWindow(QWidget, edit_add_password.Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = edit_add_password.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
    def connectFunctions(self):
        self.ui.ApplyButton.clicked.connect(applyAddPassword)
        self.ui.CancelButton.clicked.connect(cancelAddPassword)

class EditPasswordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = edit_add_password.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.connectFunctions()
    def connectFunctions(self):
        self.ui.ApplyButton.clicked.connect(applyEditPassword)
        self.ui.CancelButton.clicked.connect(cancelEditPassword)



# Exectuions for open windows
# Exectuions for open windows

def executeMain():
    global Main_Window
    Main_Window = MainWindow()
    Main_Window.ui.lableVersion.setText(f'Platform: {platform.system()}    Version: {app_version}')
    Main_Window.ui.PasswordList.setVisible(False)
    Main_Window.show()

def executeOpenFile():
    global Open_File_Window
    Open_File_Window = OpenFileWindow()
    Open_File_Window.ui.ErrorsLable.setVisible(False)
    Open_File_Window.ui.ErrorsIcon.setVisible(False)
    Open_File_Window.ui.ErrorsBack.setVisible(False)
    Open_File_Window.ui.PathInput.setText(helpers.preInputDir())
    Open_File_Window.show()

def executeNewFile():
    global New_File_Window
    New_File_Window = NewFileWindow()
    New_File_Window.ui.ErrorsLable.setVisible(False)
    New_File_Window.ui.ErrorsIcon.setVisible(False)
    New_File_Window.ui.ErrorsBack.setVisible(False)
    New_File_Window.ui.PathInput.setText(helpers.preInputDir())
    New_File_Window.show()

def executePasswordEdit():
    global Edit_Password_Window
    Edit_Password_Window = EditPasswordWindow()
    cur_data_block = list_obj.UserPasswordsList.passwords_list[Main_Window.getCurItem()]
    title = f"Edit «{cur_data_block[0]}» data"
    Edit_Password_Window.setWindowTitle(title)
    Edit_Password_Window.ui.ErrorsLable.setVisible(False)
    Edit_Password_Window.ui.newNameEdit.setText(cur_data_block[0])
    Edit_Password_Window.ui.newNicknameEdit.setText(cur_data_block[1])
    Edit_Password_Window.ui.newMailEdit.setText(cur_data_block[2])
    Edit_Password_Window.ui.newPassEdit.setText(cur_data_block[3])
    Edit_Password_Window.ui.newDescEdit.setText(cur_data_block[4])
    
    Edit_Password_Window.show()
    Main_Window.setOffAndBlurredList(True)

def executeAddPassword():
    global Add_Pass_Window
    Add_Pass_Window = AddPasswordWindow()
    Add_Pass_Window.connectFunctions()
    Add_Pass_Window.setWindowTitle("New password data")
    Add_Pass_Window.ui.ErrorsLable.setVisible(False)
    Add_Pass_Window.show()
    Main_Window.setOffAndBlurredList(True)

def executeSettings():
    Main_Window.ui.settings_frame.setVisible(True)
    Main_Window.ui.close_setngs.clicked.connect(lambda: Main_Window.ui.settings_frame.setVisible(False))

# Exectuions for open windows
# Exectuions for open windows



# Buttons slots block start
# Buttons slots block start
# Buttons slots block start

def applyOpenFile():
    inpt_path = str(Open_File_Window.ui.PathInput.text())
    inpt_key = str(Open_File_Window.ui.KeyInput.text())
    try:
        passwords = parse.openFile(inpt_path,inpt_key.encode('utf-8'))
        derv_key = crypt_utils.deriveKey(user_key=inpt_key.encode('utf-8'))
    except Exception as e:
        Open_File_Window.showException(exc=e)
    else:
        list_obj.createListObject(passwords=passwords)
        key_obj.createKey(user_key=derv_key)
        cache_obj.createCacheObject()
        cache_obj.updateCache(list_visibility=1, user_path=inpt_path)      

            
        Open_File_Window.close()
        Main_Window.ui.lableListBackground.setText('')
        Main_Window.enableManageAndSearch()
        Main_Window.ui.PasswordList.setVisible(True)
        Main_Window.setBlurOnElements(False)
        Main_Window.updateList()

def applyNewFile():
    inpt_key = str(New_File_Window.ui.KeyInput.text())
    inpt_path = str(New_File_Window.ui.PathInput.text())
    try:
        helpers.checkNewKey(inpt_key)
        derv_key = crypt_utils.deriveKey(user_key=inpt_key.encode('utf-8'))
    except Exception as e:
        New_File_Window.showException(exc=e)
    else:
        list_obj.createListObject(passwords=[])
        key_obj.createKey(user_key=derv_key)
        cache_obj.createCacheObject()
        cache_obj.updateCache(list_visibility=1, user_path=inpt_path)


        New_File_Window.close()
        Main_Window.ui.lableListBackground.setText('')
        Main_Window.enableManageAndSearch()
        Main_Window.ui.PasswordList.setVisible(True)
        Main_Window.setBlurOnElements(False)
        Main_Window.updateList()

def setDirDialog():
    dir, nonuse = QFileDialog.getOpenFileName(filter="JSON files (*.JSON)")
    Open_File_Window.ui.PathInput.setText(dir)
    New_File_Window.ui.PathInput.setText(dir)

def changePasswordsVisibility():
    visibility = cache_obj.AppCache.visibility_list
    if 4 > visibility >= 0:
        visibility += 1
    else:
        visibility = 1
    Main_Window.updateList()

def applyEditPassword():
    data_block = [
        Edit_Password_Window.ui.newNameEdit.text(),
        Edit_Password_Window.ui.newNicknameEdit.text(),
        Edit_Password_Window.ui.newMailEdit.text(),
        Edit_Password_Window.ui.newPassEdit.text(),
        Edit_Password_Window.ui.newDescEdit.text()
    ]
    try:
        helpers.CheckEditPassword(data_block=data_block)
    except Exception as e:
        Edit_Password_Window.ui.ErrorsLable.setVisible(True)
        Edit_Password_Window.ui.ErrorsLable.setText(str(e))
    else:
        list_obj.UserPasswordsList.passwords_list[Main_Window.getCurItem()]=data_block
        cache_obj.updateCache()
        parse.saveFile()
        Edit_Password_Window.close()
        Main_Window.updateList()
        Main_Window.switchListVisible(False)
        Main_Window.setEnabled(True)

def cancelEditPassword():
    Edit_Password_Window.close()
    Main_Window.setOffAndBlurredList(False)
    Main_Window.setEnabled(True)

def applyAddPassword():
    data_block = [
    Add_Pass_Window.ui.newNameEdit.text(),
    Add_Pass_Window.ui.newNicknameEdit.text(),
    Add_Pass_Window.ui.newMailEdit.text(),
    Add_Pass_Window.ui.newPassEdit.text(),
    Add_Pass_Window.ui.newDescEdit.text()
    ]

    try:
        helpers.CheckNewPassword(data_block=data_block)
    except Exception as e:
        Add_Pass_Window.ui.ErrorsLable.setVisible(True)
        Add_Pass_Window.ui.ErrorsLable.setText(str(e))
    else:
        list_obj.UserPasswordsList.passwords_list.append(data_block)
        cache_obj.updateCache()
        parse.saveFile()
        Add_Pass_Window.close()
        Main_Window.updateList()
        Main_Window.setOffAndBlurredList(False)
        Main_Window.setEnabled(True)

def cancelAddPassword():
    Add_Pass_Window.close()
    Main_Window.setOffAndBlurredList(False)
    Main_Window.setEnabled(True)

def deletePassword():
    del list_obj.UserPasswordsList.passwords_list[Main_Window.getCurItem()]

    cache_obj.updateCache()
    Main_Window.updateList()
    parse.saveFile()



def copyUsername():
    pyperclip.copy(str(list_obj.UserPasswordsList.passwords_list[Main_Window.getCurItem()][1]))

def copyEmail():
    pyperclip.copy(str(list_obj.UserPasswordsList.passwords_list[Main_Window.getCurItem()][2]))

def copyPassword():
    pyperclip.copy(str(list_obj.UserPasswordsList.passwords_list[Main_Window.getCurItem()][3]))


def checkSearchNull():
    if Main_Window.ui.Search_Input.text().replace(" ", "") == '':
        cache_obj.AppCache.search_active = False
        Main_Window.ui.Search_Input.clearFocus()
        Main_Window.updateList()
    else:
        cache_obj.foundSearchResults(search_word=Main_Window.ui.Search_Input.text())
        cache_obj.AppCache.search_active = True
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
    
    












