@echo off

cd /d "C:\Users\Aarchie Maggu\Documents\auribises"

git add .

set /p commit_message=Enter the commit message: 


if "%commit_message%"=="" (
    echo Error: Commit message cannot be empty.
    exit /b 1
)

git commit -m "%commit_message%"


git push -u origin master


echo Code pushed to GitHub successfully!
