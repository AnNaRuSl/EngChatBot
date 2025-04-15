@echo off
chcp 65001 > nul

REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    :: Запуск PowerShell скрипта с обходом ограничений Execution Policy
	echo Python не установлен! Загружаем и устанавливаем Python...
	powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "& {Start-Process powershell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%~dp0Setup\Setup.ps1""' -Verb RunAs}"
	pause
) ELSE (

	echo Python установлен! Нажмите Start.bat чтобы начать пользоваться чат ботом.
	pause

)
