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
