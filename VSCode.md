# VSCode

cmd+ shift + p > color preferences > install color themes > Predawn Theme Kit > file icon > ayu > dark + change the predawn again

# userSettings

left buttom settings > right up change to json

cmd+shift + p > default settigns find change them and paste to settings
"workbench.settings.editor": "json",
"workbench.settings.openDefaultSettings": true,
"workbench.settings.useSplitJSON": true

changing the default python settings...

settings > search python.pythonPath
change what you want....

# open terminal

ctr + `

python -m venv venv

# automatica corrections

shift+opt+F

goto settings
"ctrl+space" editor.fortmat onsave > true.... will correct by saving

# sorting imports

cmd+shift+p > search for sort imports
cmd+shift+p > run linting

install code runner in extension
"code-runner.executorMap": {
"python": "$pythonPath -u $fullFileName",
},
"code-runner.clearPreviousOutput": true,
"code-runner.showExecutionMessage": false
now I can run the code  
ctr+option+N

# github settings

open a repository in github... without any presettings
copy git remote add origin <https://github.com/serdarkuyuk/vsCode-deployment.git>
run in terminal in vscode
git remote add origin <https://github.com/serdarkuyuk/vsCode-deployment.git>
then go to source control ... push to .... select origin and push
