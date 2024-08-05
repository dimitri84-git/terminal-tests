echo off
:: Check for Python Installation
python --version 3>NUL
if errorlevel 1 goto errorNoPython

cls
python run.py
goto:eof

:errorNoPython
echo.
echo Error: Python not installed
echo you can download python at python.org