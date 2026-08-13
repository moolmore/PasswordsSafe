@echo off
rem Define configuration variables
set APP_NAME=PasswordsSafe
set ICON_PATH=./ON_REALEASE/windows_icon.ico
set MAIN_SCRIPT=main.py

rem Clean up previous build artifacts
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist %APP_NAME%.spec del /f /q %APP_NAME%.spec

rem Run PyInstaller with optimizations
rem --noconsole: Hides the command prompt window
rem --onefile: Packages everything into a single executable
rem --exclude-module: Removes unused heavy PySide6 modules to reduce size
pyinstaller --noconsole --onefile ^
    --name="%APP_NAME%" ^
    --icon="%ICON_PATH%" ^
    --hidden-import=pyside6 ^
    --hidden-import=cryptography ^
    --hidden-import=pyperclip ^
    --exclude-module=PySide6.QtWebEngineCore ^
    --exclude-module=PySide6.QtWebEngineWidgets ^
    --exclude-module=PySide6.QtQuick ^
    --exclude-module=PySide6.QtQml ^
    --exclude-module=PySide6.Qt3DCore ^
    --exclude-module=PySide6.QtMultimedia ^
    --exclude-module=PySide6.QtCharts ^
    --exclude-module=PySide6.QtDataVisualization ^
    "%MAIN_SCRIPT%"

rem Check if the build was successful
if %ERRORLEVEL% equ 0 (
    echo [SUCCESS] Build completed successfully. Check the "dist" folder.
) else (
    echo [ERROR] Build failed. Please check the logs above.
)

pause
