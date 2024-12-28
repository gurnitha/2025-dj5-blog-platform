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


## 2. Creating Apps

#### 2.1 Creating Apps part 1: Adding features with apps 

        modified:   README.md
        new file:   apps/blog/__init__.py
        new file:   apps/blog/admin.py
        new file:   apps/blog/apps.py
        new file:   apps/blog/migrations/__init__.py
        new file:   apps/blog/models.py
        new file:   apps/blog/tests.py
        new file:   apps/blog/views.py

#### 2.1 Creating Apps part 2: Register the blog app to the project

        modified:   README.md
        modified:   config/settings.py

        Note error:

        ModuleNotFoundError: No module named 'blog'

        Solution:

        Creating path for apps in settings.py

#### 2.1 Creating Apps part 3: Creating path for the apps

        ModuleNotFoundError: No module named 'blog'

        C:\Users\ING\Desktop\workspace\2025\ex-ebook\django-the-easy-way\blogging-platform\config\settings.py changed, reloading.
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        December 28, 2024 - 08:26:53
        Django version 5.1.3, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

        modified:   README.md
        modified:   config/settings.py

        Note error fixed:

        Error fixed.

#### 2.2 Configuring URLs

        modified:   README.md
        new file:   apps/blog/urls.py
        modified:   config/urls.py

#### 2.3 Creating views

        modified:   README.md
        modified:   apps/blog/views.py

#### 2.4 Creating templates

        modified:   README.md
        modified:   config/settings.py
        new file:   templates/blog/home.html


## 3. Templates

#### 3.1 Templates

        modified:   README.md
        modified:   templates/blog/home.html

#### 3.2 Template inheritance

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/blog/home.html