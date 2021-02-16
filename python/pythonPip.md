# PIP installation

>python3 -m pip install --user --upgrade pip
>python3 -m pip --version

download virtual environment

> python3 -m pip install --user virtualenv

## Creating a virtual environment
> python3 -m venv env

## Activating a virtual environment

> source env/bin/activate

where this environment is installed

> which python

## Leaving the virtual environment

> deactivate

## upgrade PIP

> pip3 install --upgrade pip

## listing

> pip3 list

## requirement

> pip install -r requirements.txt

## freeze

> pip freeze

> pip freeze --local > requirements.txt

## deleting virtual environment

> rm -rf foldername/

## specific environment
virtualenv -p /usr/bin/python2.6 projectName

## uninstall all packets
> pip freeze | xargs pip uninstall -y

# Version run python
goto website for specific version
download and install manually

Reference
https://medium.com/swlh/how-to-run-a-different-version-of-python-from-your-terminal-fe744276ff22

pip uninstall virtualenv
ln -s /usr/bin/python3 /usr/local/bin/python37
pip3 install virtualenv

virtualenv venv -p python37
source venv/bin/activate


# corey

python3 -m venv customSpacy
which python
pip3 list

install all system packages
python3 -m venv venv --system-site-packages

pip3 list --local #only local packages
