# (｡•́︿•̀｡)
import sys, os
#For create cache in windows temp (in builded pyinstaller app cache not generates (PyInstaller problem))
sys.pycache_prefix = os.path.expandvars(r"%temp%\passwords_safe\cache")
import platform, csv
from core import parse, key_obj, crypt_utils, cache_obj, helpers, list_obj
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QGraphicsBlurEffect
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont
import pyperclip


from ui import edit_add_password, main_menu, new_file, open_file

#App version
app_version = '2.1.1'

# All windows classes start
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = main_menu.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PasswordList.setWordWrap(True)
        self.connectFunctions()
        self.setBlurOnElements(True)
        self.blur_status = False
        self.ui.manage.setEnabled(False)
        self.ui.search.setEnabled(False)
        self.ui.lableVersion.setText(f'Platform: {platform.system()}    Version: {app_version}')
        self.ui.PasswordList.setVisible(False)
        self.ui.settings_frame.setVisible(False)
        self.ui.saved.setVisible(False)
    
    def connectFunctions(self) -> None:
        self.ui.OpenFile.clicked.connect(executeOpenFile)
        self.ui.CreateFile.clicked.connect(executeNewFile)
        self.ui.VisibilityPassButton.clicked.connect(changePasswordsVisibility)
        self.ui.AddPassButton.clicked.connect(executeAddPassword)
        self.ui.DeletePassButton.clicked.connect(deletePassword)
        self.ui.EditPassButton.clicked.connect(executePasswordEdit)
        self.ui.CopyNameButton.clicked.connect(lambda: copyData(1))
        self.ui.CopyEmailButton.clicked.connect(lambda: copyData(2))
        self.ui.CopyPassButton.clicked.connect(lambda: copyData(3))
        self.ui.Search_Input.textChanged.connect(checkSearchNull)
        self.ui.settings.clicked.connect(executeSettings)
        self.ui.import_csv.clicked.connect(importCSV)
        self.ui.export_passes_1.clicked.connect(lambda: exportPasswords(type='default'))
        self.ui.export_passes_2.clicked.connect(lambda: exportPasswords(type='moolmore'))

    def showAutosaved(self) -> None:
        self.ui.saved.setVisible(True)
        QTimer.singleShot(3000, lambda: self.ui.saved.setVisible(False))

    def enableManageAndSearch(self) -> None:
        Main_Window.ui.manage.setEnabled(True)
        Main_Window.ui.search.setEnabled(True)

    def updateList(self) -> None:

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

    def setBlurOnElements(self, turn_on) -> None:

        if turn_on:
            self.blur_status = True
            self.blur=QGraphicsBlurEffect()
            self.blur.setBlurRadius(4)  
            self.blur.setBlurHints(QGraphicsBlurEffect.QualityHint)

            self.blur2=QGraphicsBlurEffect()
            self.blur2.setBlurRadius(4)  
            self.blur2.setBlurHints(QGraphicsBlurEffect.QualityHint)
        else:
            try:
                del self.blur
                del self.blur2
            except:
                pass

            self.blur_status = False
        self.ui.manage.setGraphicsEffect(self.blur if turn_on else None)
        self.ui.search.setGraphicsEffect(self.blur2 if turn_on else None)

    def setOffAndBlurredList(self, turn_on) -> None:

        self.list_blur = QGraphicsBlurEffect()
        self.list_blur.setBlurHints(QGraphicsBlurEffect.QualityHint)
        self.ui.PasswordList.setGraphicsEffect(self.list_blur if turn_on else None)
        self.ui.PasswordList.setEnabled(False if turn_on else True)
        if not turn_on:
            del self.list_blur

    def setEnabledManagment(self, turn_on) -> None:
        self.ui.parse.setEnabled(turn_on)
        self.ui.manage.setEnabled(turn_on)
        self.ui.search.setEnabled(turn_on)

    def getCurItem(self) -> int:
        if not cache_obj.AppCache.search_active:
            return self.ui.PasswordList.currentRow()
        else:
            return cache_obj.AppCache.srch_ind_map[self.ui.PasswordList.currentRow()]

    def changeTitleSec(self) -> None:
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
# All windows classes end


# Exectuions for open Qt windows start
# Exectuions for open Qt windows start

def executeMain() -> None:
    global Main_Window
    Main_Window = MainWindow()
    Main_Window.ui.lableVersion.setText(f'{platform.system()} {platform.release()} - {app_version}')
    Main_Window.ui.PasswordList.setVisible(False)
    Main_Window.show()

def executeOpenFile() -> None:
    global Open_File_Window
    Open_File_Window = OpenFileWindow()
    Open_File_Window.ui.ErrorsLable.setVisible(False)
    Open_File_Window.ui.ErrorsIcon.setVisible(False)
    Open_File_Window.ui.ErrorsBack.setVisible(False)
    Open_File_Window.ui.PathInput.setText(helpers.preInputDir())
    Open_File_Window.show()

def executeNewFile() -> None:
    global New_File_Window
    New_File_Window = NewFileWindow()
    New_File_Window.ui.ErrorsLable.setVisible(False)
    New_File_Window.ui.ErrorsIcon.setVisible(False)
    New_File_Window.ui.ErrorsBack.setVisible(False)
    New_File_Window.ui.PathInput.setText(helpers.preInputDir())
    New_File_Window.show()

def executePasswordEdit() -> None:
    global Edit_Password_Window
    Edit_Password_Window = EditPasswordWindow()
    

    Edit_Password_Window.ui.ErrorsLable.setVisible(False)

    #qol autoadded passwords data
    cur_data_block = list_obj.UserPasswordsList.passwords_list[Main_Window.getCurItem()] 
    Edit_Password_Window.ui.newNameEdit.setText(cur_data_block[0])
    Edit_Password_Window.ui.newNicknameEdit.setText(cur_data_block[1])
    Edit_Password_Window.ui.newMailEdit.setText(cur_data_block[2])
    Edit_Password_Window.ui.newPassEdit.setText(cur_data_block[3])
    Edit_Password_Window.ui.newDescEdit.setText(cur_data_block[4])
    
    title = f"Edit «{cur_data_block[0]}» data"
    Edit_Password_Window.setWindowTitle(title)

    Main_Window.setOffAndBlurredList(True)
    Main_Window.setEnabledManagment(False)
    Edit_Password_Window.show()

def executeAddPassword() -> None:
    global Add_Pass_Window
    Add_Pass_Window = AddPasswordWindow()
    Add_Pass_Window.connectFunctions()
    Add_Pass_Window.setWindowTitle("New password data")
    Add_Pass_Window.ui.ErrorsLable.setVisible(False)

    
    Main_Window.setOffAndBlurredList(True)
    Main_Window.setEnabledManagment(False)
    Add_Pass_Window.show()

def executeSettings() -> None:
    Main_Window.ui.settings_frame.setVisible(True)
    Main_Window.ui.close_setngs.clicked.connect(lambda: Main_Window.ui.settings_frame.setVisible(False))

# Exectuions for open Qt windows end 
# Exectuions for open Qt windows end



# Buttons slots block start
# Buttons slots block start
# Buttons slots block start

def applyOpenFile() -> None:
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
        if Main_Window.blur_status == False:
            Main_Window.ui.PasswordList.setVisible(True)
        Main_Window.setBlurOnElements(False)
        Main_Window.updateList()

def applyNewFile() -> None:
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
        if Main_Window.blur_status == False:
            Main_Window.ui.PasswordList.setVisible(True)
        Main_Window.setBlurOnElements(False)
        Main_Window.updateList()

def setDirDialog() -> None:
    dir, nonuse = QFileDialog.getOpenFileName(filter="JSON files (*.JSON)")
    Open_File_Window.ui.PathInput.setText(dir)
    New_File_Window.ui.PathInput.setText(dir)

def changePasswordsVisibility() -> None:

    appcache = cache_obj.AppCache

    if 4 > appcache.visibility_list >= 0:
        appcache.visibility_list += 1
    else:
        appcache.visibility_list = 1

    Main_Window.updateList()

def applyEditPassword() -> None:
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
        Main_Window.showAutosaved()
        Edit_Password_Window.close()
        Main_Window.updateList()
        Main_Window.setOffAndBlurredList(False)
        Main_Window.setEnabledManagment(True)
        
def cancelEditPassword() -> None:
    Edit_Password_Window.close()
    Main_Window.setOffAndBlurredList(False)
    Main_Window.setEnabledManagment(True)

def applyAddPassword() -> None:
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
        Main_Window.showAutosaved()
        Add_Pass_Window.close()
        Main_Window.updateList()
        Main_Window.setOffAndBlurredList(False)
        Main_Window.setEnabledManagment(True)

def cancelAddPassword() -> None:
    Add_Pass_Window.close()
    Main_Window.setOffAndBlurredList(False)
    Main_Window.setEnabledManagment(True)

def deletePassword() -> None:
    del list_obj.UserPasswordsList.passwords_list[Main_Window.getCurItem()]

    cache_obj.updateCache()
    Main_Window.updateList()
    parse.saveFile()
    Main_Window.showAutosaved()

def copyData(value: int) -> None:
    data = str(list_obj.UserPasswordsList.passwords_list[Main_Window.getCurItem()][value])
    pyperclip.copy(data if data.replace(" ", "") != "" else "Data is empty")

def checkSearchNull() -> None:
    if Main_Window.ui.Search_Input.text().replace(" ", "") == '':
        cache_obj.AppCache.search_active = False
        Main_Window.ui.Search_Input.clearFocus()
        Main_Window.updateList()
    else:
        cache_obj.foundSearchResults(search_word=Main_Window.ui.Search_Input.text())
        cache_obj.AppCache.search_active = True
        Main_Window.updateList()

def importCSV() -> None:
    path = QFileDialog.getOpenFileName(filter="CSV files (*.csv)")[0]
    print(path)
    with open(path, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Пропускаем заголовок, если он не нужен
        next(csv_reader) 
        for row in csv_reader:
            list_obj.UserPasswordsList.passwords_list.append([row[0],row[2],"",row[3],row[4]])
        cache_obj.updateCache()
        Main_Window.updateList()
        parse.saveFile()
        Main_Window.showAutosaved()

def exportPasswords(type: str) -> None:
    fileName = QFileDialog.getSaveFileName(dir=r"%USERPROFILE%\Documents\ps_passwords.csv",filter="Passwords (*.csv)")[0]

    with open(fileName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if type == 'default':
            writer.writerow(["name","url","username","password","note"])
            for data_block in list_obj.UserPasswordsList.passwords_list:
                writer.writerow([data_block[0],"Not Supported",data_block[1],data_block[3],str(data_block[4])+"Email:"+str(data_block[2])])
        elif type == 'moolmore':
            writer.writerow(["service","username","email","password","misc"])
            for data_block in list_obj.UserPasswordsList.passwords_list:
                writer.writerow([data_block[0],data_block[1],data_block[2],data_block[3],data_block[4]])

# Buttons slots block end
# Buttons slots block end
# Buttons slots block end

def main() -> None:
    App = QApplication()
    executeMain()
    sys.exit(App.exec())
    

if __name__ == '__main__':
    main()
    
    












