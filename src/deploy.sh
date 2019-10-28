#!/bin/bash
echo
echo "***************************"
echo "**REMOVING UNWANTED FILES**"
echo "***************************"
rm -rf toDeploy/ && echo "$(tput setaf 2)Removed toDeploy files$(tput sgr 0)"
rm -rf __pycache__ && echo "$(tput setaf 2)Removed __pycache__$(tput sgr 0)" 
rm *.pyc && echo "$(tput setaf 2)Removed pyc files$(tput sgr 0)"
rm *.zip && echo "$(tput setaf 2)Removed zip files$(tput sgr 0)"
rsync -a --exclude="./toDeploy/" ./* toDeploy && echo "$(tput setaf 2)Copied files for deploying$(tput sgr 0)"
cd toDeploy
python3 -m pip install --target=./ pytest-json-report --upgrade

echo
echo "***************************"
echo "*****ZIP CONTENT***********"
echo "***************************"
if zip -qr lambdaFunc.zip .
then 
    echo "$(tput setaf 2)LamndaFunc.zip created!$(tput sgr 0)"
else
    echo "$(tput setaf 2)[ERROR] : while creating lambdaFunc.zip$(tput sgr 0)"
fi

echo
echo "***************************"
echo "*******DEPLOY**************"
echo "***************************"
if aws lambda update-function-code --function-name pythonTestingSuite --zip-file fileb://lambdaFunc.zip
then 
    echo
    echo
    echo "$(tput setaf 2)***************************$(tput sgr 0)"
    echo "$(tput setaf 2)***SUCCESSFULLY DEPLOYED***$(tput sgr 0)"
    echo "$(tput setaf 2)***************************$(tput sgr 0)"
else
    echo
    echo
    echo "$(tput setaf 1)***************************$(tput sgr 0)"
    echo "$(tput setaf 1)***------ERROR----------***$(tput sgr 0)"
    echo "$(tput setaf 1)***************************$(tput sgr 0)"
fi

cd ../
rm -rf toDeploy/
