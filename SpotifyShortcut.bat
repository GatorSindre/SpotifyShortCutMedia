@echo off
:: Batch to run Python script as admin using venv, window stays open

:: Full path to this folder
set "SCRIPT_DIR=%~dp0"

:: Paths to venv activate and Python script
set "ACTIVATE_BAT=%SCRIPT_DIR%venv\Scripts\activate.bat"
set "PY_FILE=%SCRIPT_DIR%spotifyshortcutmedia.py"

:: Powershell elevated cmd
powershell -NoProfile -Command "Start-Process cmd.exe -ArgumentList '/k call \"%ACTIVATE_BAT%\" && python \"%PY_FILE%\" && echo. && echo Script finished with exit code %ERRORLEVEL% && pause' -Verb RunAs"