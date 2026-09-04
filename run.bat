@echo off
:: Устанавливаем кодировку UTF-8, чтобы не ломался русский текст
chcp 65001 > nul

:: Включаем поддержку ANSI-цветов (\033[...) в консоли Windows
reg add "HKCU\Console" /v VirtualTerminalLevel /t REG_DWORD /d 1 /f > nul

:: Запускаем ваш Python скрипт
python main.py

:: Не дает окну закрыться сразу после завершения скрипта
pause
