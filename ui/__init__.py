darwin_list = ['main_menu_darwin', 'add_password_darwin', 'edit_password_darwin', 'new_file_darwin', 'open_file_darwin']

win32_list = ['main_menu_win64', 'open_file_win64', 'new_file_win64']
__all__ = darwin_list.append(win32_list)

from . import main_menu_darwin, add_password_darwin, edit_password_darwin, new_file_darwin, open_file_darwin
from . import main_menu_win64, open_file_win64, new_file_win64
