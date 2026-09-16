import os
import shutil

def clean_project():
    # Текущая директория, где запущен скрипт
    current_dir = os.getcwd()
    print(f"Начало очистки в директории: {current_dir}\n")
    
    # Счётчики для статистики
    pycache_count = 0
    folders_removed = 0
    files_removed = 0

    # 1. Обход дерева каталогов для удаления __pycache__, build и dist
    # Используем topdown=False, чтобы сначала удалять файлы/папки внутри, 
    # а затем саму родительскую папку (актуально для вложенных структур)
    for root, dirs, files in os.walk(current_dir, topdown=False):
        for dirname in dirs:
            dir_path = os.path.join(root, dirname)
            
            # Проверяем целевые папки
            if dirname in ['__pycache__', 'build', 'dist']:
                try:
                    shutil.rmtree(dir_path)
                    print(f"Удалена папка: {dir_path}")
                    if dirname == '__pycache__':
                        pycache_count += 1
                    else:
                        folders_removed += 1
                except Exception as e:
                    print(f"Ошибка при удалении папки {dir_path}: {e}")

    # 2. Удаление конкретного файла PasswordsSafe.spec
    spec_file = "PasswordsSafe.spec"
    # Ищем его в текущей папке (или можно использовать полный путь, если он в корне)
    spec_path = os.path.join(current_dir, spec_file)
    if os.path.exists(spec_path):
        try:
            os.remove(spec_path)
            print(f"Удален файл: {spec_path}")
            files_removed += 1
        except Exception as e:
            print(f"Ошибка при удалении файла {spec_path}: {e}")

    print(f"\nОчистка завершена!")
    print(f"Удалено папок __pycache__: {pycache_count}")
    print(f"Удалено папок build/dist: {folders_removed}")
    print(f"Удалено файлов .spec: {files_removed}")

if __name__ == "__main__":
    clean_project()
