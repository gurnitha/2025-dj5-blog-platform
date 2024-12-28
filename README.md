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