@echo off
title Automatic GIT Uploader

echo POZOR vybrany disk je ten na kterym je umisten tento soubor
choice /C YN /M "Chcete zmenit disk"
if errorlevel 2 goto :disk

set /p drive=Zadejte disk:
cd /d %drive%:\

:disk
set loc=D:\!Patrik\!Programovani\Python\Skola
echo Default location is D:\!Patrik\!Programovani\Python\Skola
choice /C YN /M "Chcete tuto lokaci repozitare pouzit"
if errorlevel 2 goto :vyber
if errorlevel 1 cd /d d:\ & goto zmena

:vyber
choice /c 1234 /n /m "Vyberte z nasledujicich moznosti: (1=D:\!Patrik\!Programovani\Python\Skola, 2=D:\!Patrik\!Programovani\Python\Skola_1C_2026-27\Treti, 3=Dokumenty\lokace_pro_skolni_komp, 4=Zadat vlastni lokaci)"

if %errorlevel%==3 set loc=%USERPROFILE%\Documents\lokace_pro_skolni_komp & cd /d c:\ &goto zmena
if %errorlevel%==2 set loc=D:\!Patrik\!Programovani\Python\Skola_1C_2026-27\Treti & cd /d d:\ & goto zmena
if %errorlevel%==1 set loc=D:\!Patrik\!Programovani\Python\Skola & cd /d d:\ & goto zmena



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