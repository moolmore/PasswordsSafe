#!/bin/bash

# Переходим в директорию, где находится сам скрипт
cd "$(dirname "$0")"

# Имя вашего главного скрипта (измените main.py, если у вас другое имя)
SCRIPT_NAME="main.py"
APP_NAME="PasswordsSafe"
ICON_PATH="./ON_REALEASE/macos_icon.icns"

echo "=== Начало сборки $APP_NAME для macOS ==="

# Проверяем наличие необходимых утилит
if ! command -v pyinstaller &> /dev/null; then
    echo "Ошибка: PyInstaller не установлен. Установите его через: pip install pyinstaller"
    exit 1
fi

# Собираем команду PyInstaller с жестким исключением (exclude) тяжелых модулей PySide6
pyinstaller --noconfirm --onedir --windowed \
    --name "$APP_NAME" \
    --icon "$ICON_PATH" \
    --clean \
    --hidden-import="pyperclip" \
    --hidden-import="PySide6.QtCore" \
    --hidden-import="PySide6.QtGui" \
    --hidden-import="PySide6.QtWidgets" \
    --exclude-module="PySide6.QtNetwork" \
    --exclude-module="PySide6.QtQml" \
    --exclude-module="PySide6.QtQuick" \
    --exclude-module="PySide6.QtWebEngine" \
    --exclude-module="PySide6.QtWebEngineCore" \
    --exclude-module="PySide6.QtWebEngineWidgets" \
    --exclude-module="PySide6.QtMultimedia" \
    --exclude-module="PySide6.QtMultimediaWidgets" \
    --exclude-module="PySide6.Qt3DCore" \
    --exclude-module="PySide6.Qt3DRender" \
    --exclude-module="PySide6.QtCharts" \
    --exclude-module="PySide6.QtDataVisualization" \
    --exclude-module="PySide6.QtSql" \
    --exclude-module="PySide6.QtTest" \
    --exclude-module="PySide6.QtXml" \
    --exclude-module="tkinter" \
    "$SCRIPT_NAME"

echo "=== Сборка успешно завершена! ==="
echo "Готовое приложение .app находится в папке dist/"

# Оставляем окно терминала открытым, чтобы увидеть результат
bash
