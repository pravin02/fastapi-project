# fastapi-project
This repo demonstrates the features of FastAPI lib to develop APIs in python

## Description
This application connects with postgres database for CRUD (Create, Read, Update and Delete) operations.

## Dependencies
to install dependencies look for pyproject.toml file which has listed all the required dependencies to run this application successfully.

`uv pip install -r .\pyproject.toml`

## How to run
This application created using uv package manager and fastapi standard dependency.
To run this application use below commands.

`fastapi dev ./main.py`

Above command run application in developer mode default on 8000 port number.

`fastapi run ./main.py`

Above command run application in production mode default on 8000 port number.

