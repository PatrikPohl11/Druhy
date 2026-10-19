@echo off
title Automatic GIT Uploader

echo POZOR vybrany disk je ten na kterym je umisten tento soubor
choice /C YN /M "Chcete zmenit disk"
if errorlevel 2 goto :disk

set /p drive=Zadejte disk:
cd /d %drive%:\

:disk
set loc=%USERPROFILE%\Documents\Python\GIT Uploader\
echo Default location is Documents\!!!!!\!!AAA chcere ji zmenit?
choice /C YN /M "Chcete zmenit lokaci repozitare"
if errorlevel 2 goto zmena

set /p loc=Zadejte lokaci repozitare (umisteni ktere chcete nahrat): 

:zmena
cd %loc%

:loop

git add .
git status
set /p Koment=Zadejte komentar k nahrani: 
timeout /t 1
git commit -m "%Koment%"
timeout /t 1
git push
timeout /t 1
git status

echo pro dalsi nahrani stisknete ENTR
pause
cls
goto loop