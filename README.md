# Django 3.x Api Boilerplate

This template has boilerplate code to create a django api service from scratch. Just clone the template and start writing your app logics.

## Supports
1. Django 3.3
2. Django rest framework
3. ipython
4. ipdb
5. pre-commit
6. pipenv

## PreComit Hooks
This template has a inbuilt precommit hooks support that will lint, format and do security checks on the staged files. To setup precommit hook run `precommit install`. The hooks present in the project can be found at .pre-commit-config.yaml file.

## How to setup?
1. Create a new project directory and change to project directory
2. `git clone https://github.com/satheesh1997/django-3.x-api-boilerplate.git . `.
3. `rm -rf .git`, once removed create a repo on your github.
4. `git init`
5. `git remote add origin <your new repos clone url>`
6. `git add .`
7. `git commit -m 'Initial commit'`
8. `git push -u origin master`

## How to start the server?
This template uses pipenv for python dependency management. So to start the server do `pipenv install` to install all the packages. Once done, do `pipenv shell` to activate the python environment and run `./manage.py runserver`.

To know more about pipenv refer https://realpython.com/pipenv-guide/.

## Project Structure
This is the structure on how the files and folders are structures in this template.

[![Folder tree](https://i.ibb.co/WtMpknr/Screenshot-from-2020-12-25-12-52-36.png "Folder tree")](https://i.ibb.co/WtMpknr/Screenshot-from-2020-12-25-12-52-36.png "Folder tree")
