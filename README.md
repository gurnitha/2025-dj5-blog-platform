## BLOGGING PLATFORM USING DJANGO 5


## 1. Creating A Django Project

#### 1.1 Creating virtual environments

        λ python -m venv venv312513

#### 1.2 Installing Django

        λ venv312513\Scripts\activate.bat
        (venv312513) λ pip install django==5.1.3
        (venv312513) λ python.exe -m pip install --upgrade pip

#### 1.3 Creating a new Django project

        (venv312513) λ django-admin --version
        5.1.3

        (venv312513) λ django-admin startproject config .

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

#### 1.4 Run Django development server

        (venv312513) λ ls
        config/  manage.py*  README.md

        C:\Users\ING\Desktop\workspace\2025\ex-ebook\django-the-easy-way\blogging-platform(master)
        (venv312513) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        December 28, 2024 - 08:16:30
        Django version 5.1.3, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.