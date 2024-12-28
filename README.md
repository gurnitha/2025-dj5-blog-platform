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

#### 3.3 Block super for page title

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/blog/home.html


## 4. Static Files (CSS)

#### 4.1 Adding CSS stylesheets

        modified:   .gitignore
        modified:   README.md
        new file:   static/css/base.css

#### 4.2 Configuration

        modified:   README.md
        modified:   config/settings.py

#### 4.3 Load static file in template

        modified:   README.md
        modified:   templates/base.html

#### 4.4 Highlighting active links

        modified:   README.md
        modified:   apps/blog/views.py
        modified:   templates/base.html

#### 4.5 Create about page

        modified:   README.md
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        modified:   templates/base.html
        new file:   templates/blog/about.html


## 5. Models

#### 5.1 Creating models

        (venv312513) λ python manage.py makemigrations
        Migrations for 'blog':
          apps\blog\migrations\0001_initial.py
            + Create model Post

        (venv312513) λ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, blog, contenttypes, sessions
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying auth.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying blog.0001_initial... OK
          Applying sessions.0001_initial... OK

        C:\Users\ING\Desktop\workspace\2025\ex-ebook\django-the-easy-way\blogging-platform(master)
        (venv312513) λ python manage.py createsuperuser
        Username (leave blank to use 'ing'): admin
        Email address: admin@mail.com
        Password:
        Password (again):
        The password is too similar to the email address.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.

        modified:   README.md
        modified:   apps/blog/admin.py
        new file:   apps/blog/migrations/0001_initial.py
        modified:   apps/blog/models.py

#### 5.2 Listing blog posts

        modified:   README.md
        modified:   apps/blog/views.py
        modified:   templates/blog/home.html

#### 5.3 Creating a blog detail page

        new file:   apps/blog/migrations/0002_post_slug.py
        modified:   apps/blog/models.py
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        new file:   templates/blog/detail.html
        modified:   templates/blog/home.html

        Note about post detail link:

        <a href="{{ post.get_absolute_url }}">
        {{ post.title }}
        </a>

        <a href="{% url 'blog:detail' post.slug %}">
        {{ post.title }}
        </a>

        Both links has the same results.


## 6. ForeignKey And Dates