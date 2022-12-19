@echo off

call %~dp0Mysait\2variant\venv\Scripts\activate

cd %~dp0Mysait\2variant

set TOKEN=5720395053:AAGjdbEjwvDzOMHBILY1_uBuL8X7RlFs5gE

python bot_telegram.py

pause