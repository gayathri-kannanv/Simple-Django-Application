# Simple Django Application - Login, Form with HTTPResponse, SQL

### Quick bullets on Django,

- Popular high level backend server side Python Web framwork
- Free and Opensource
- Build websites and RestAPIs
- Follows the MVT (Model View Template) design pattern.
- Comes with inbuilt Database Backend.
- Supports database systems including SQL, MySQL, Oracle, Postgres, etc.
- Supports multilingual websites.
- Provides a ready-to-use Administration GUI.
- Popular Django applications include Instagram, Mozilla, Spotify, Pinterest.

### Installation and configuration is quite easy and here are the steps:

#### Windows

1) Select a path in the commandline where you'll need your django application.
2) Create a project directory.
> mkdir django_auth
3) > cd django_auth
4) Create virtual envvironment.
> python -m venv .venv
5) > .venv\Scripts\Activate.ps1
6) Install Django. 
(.venv) > python -m pip install django
7) (.venv) > django-admin startproject django_project .
8) (.venv) > python manage.py migrate
9) (.venv) > python manage.py runserver

Navigate to http://127.0.0.1:8000, you'll see the Django default screen.

#### Here in this simple application, there's a login page and after login, taken three inputs from an html frontend home page, and taken the request, produced a http response along with storing them into an external database.
