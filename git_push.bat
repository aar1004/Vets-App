@echo off
REM Change the working directory to the location of your local Git repository
cd /d "C:\Users\Aarchie Maggu\Documents\my_project"

REM Add all changes to the staging area
git add .

REM Prompt the user to enter the commit message
set /p commit_message=Enter the commit message: 

REM Check if the commit message is empty
if "%commit_message%"=="" (
    echo Error: Commit message cannot be empty.
    exit /b 1
)

REM Commit the changes with the provided commit message
git commit -m "%commit_message%"

REM Push the committed changes to the remote repository (assuming the remote is named 'origin' and the branch is 'main')
git push -u origin master

REM Optional: Display a message indicating the push was successful
echo Code pushed to GitHub successfully!
