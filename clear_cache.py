#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Скрипт для автоматической очистки кэша скомпилированных файлов Python.
Удаляет все директории __pycache__ в текущей папке и всех её подкаталогах.

Created by: AI Assistant (Large Language Model trained by Google)
Date: 2026
"""

import os
import shutil



def clear_pycache_directories():
    """Рекурсивно находит и удаляет все папки __pycache__."""
    # Получаем путь к директории, откуда запущен скрипт
    target_dir = os.getcwd()
    print(f"[-] Запуск очистки в директории: {target_dir}")
    
    counter = 0

    # Флаг topdown=False критически важен, чтобы сначала обрабатывать глубокие вложенные папки
    for root, dirs, _ in os.walk(target_dir, topdown=False):
        for directory in dirs:
            if directory == '__pycache__':
                full_path = os.path.join(root, directory)
                try:
                    shutil.rmtree(full_path)
                    print(f"[Удалено] {full_path}")
                    counter += 1
                except Exception as error:
                    print(f"[Ошибка] Не удалось удалить {full_path}: {error}")

    print(f"\n[Готово] Операция завершена. Удалено директорий: {counter}")


if __name__ == "__main__":
    clear_pycache_directories()