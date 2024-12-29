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

        new file:   apps/blog/migrations/0003_post_author_post_date_post_updated_alter_post_slug.py
        modified:   apps/blog/models.py
        modified:   templates/blog/detail.html
        modified:   templates/blog/home.html


## 7. Forms With ModelForm

#### 7.1 Creating posts

        modified:   README.md
        new file:   apps/blog/forms.py
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        modified:   templates/base.html
        new file:   templates/blog/create.html

        Note of success: 

        Successfully created new posts.

        :)

#### 7.2 Editing posts

        modified:   README.md
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        modified:   templates/blog/detail.html
        new file:   templates/blog/edit.html
        modified:   templates/blog/home.html

        Note of success: 

        Successfully edited posts.

        :)

#### 7.3 Deleting posts

        modified:   README.md
        modified:   apps/blog/forms.py
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        new file:   templates/blog/delete.html
        modified:   templates/blog/home.html


## 8. Authentication

#### 8.1 Implementing authentication

        (venv312513) λ  pip install django-allauth
        Collecting django-allauth
          Downloading django_allauth-65.3.1.tar.gz (1.5 MB)
             ---------------------------------------- 1.5/1.5 MB 5.9 MB/s eta 0:00:00
          Installing build dependencies ... done
          Getting requirements to build wheel ... done
          Preparing metadata (pyproject.toml) ... done
        Requirement already satisfied: Django>=4.2.16 in c:\users\ing\desktop\workspace\2025\ex-ebook\django-the-easy-way\venv312513\lib\site-packages (from django-allauth) (5.1.3)
        Requirement already satisfied: asgiref>=3.8.1 in c:\users\ing\desktop\workspace\2025\ex-ebook\django-the-easy-way\venv312513\lib\site-packages (from django-allauth) (3.8.1)
        Requirement already satisfied: sqlparse>=0.3.1 in c:\users\ing\desktop\workspace\2025\ex-ebook\django-the-easy-way\venv312513\lib\site-packages (from Django>=4.2.16->django-allauth) (0.5.3) Requirement already satisfied: tzdata in c:\users\ing\desktop\workspace\2025\ex-ebook\django-the-easy-way\venv312513\lib\site-packages (from Django>=4.2.16->django-allauth) (2024.2)
        Building wheels for collected packages: django-allauth
          Building wheel for django-allauth (pyproject.toml) ... done
          Created wheel for django-allauth: filename=django_allauth-65.3.1-py3-none-any.whl size=1659109 sha256=3a41f62a513f9e0998cea45e5062dac3fcaa16d1ced5508d3ae425942242291d
          Stored in directory: c:\users\ing\appdata\local\pip\cache\wheels\d6\8e\1a\7385ffbef015e4ba18bd9075ac93344f4d3d4d4a6deecf8803
        Successfully built django-allauth
        Installing collected packages: django-allauth
        Successfully installed django-allauth-65.3.1

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/base.html

        Note of success:

        1. First time using django-allauth.
        2. Sign in, Sign out, Sign up success.

        :)

#### 8.2 Overriding templates

        modified:   README.md
        new file:   templates/account/login.html

        Note:

        It uses allauth in the venv312513.


## 9. Authorization

#### 9.1 Assigning permissions with groups

        modified:   README.md

        # Login to admin panel as superuser
        1. Create a new group: Editor
        2. Add permissions:
        - Can add post
        - Can change post
        - Can delete post
        3. Create a new user: test + Staff status + Chosen group: Editor
        4. Try to login

        :)

#### 9.2 Checking permissions in templates

        modified:   README.md
        modified:   templates/blog/home.html

        :)

#### 9.3 Restricting access to views

        modified:   README.md
        # Added required decoreator to create, edit, delete views
        modified:   apps/blog/views.py
        # Hide the 'Add new post' menu to un-authorized user
        modified:   templates/base.html

        :)


## 10. Tagging

#### 10.1 Tagging blog posts

        # 1. Install django_taggit
        (venv312513) λ pip install django_taggit
        ...
        Successfully installed django_taggit-6.1.0

        # 2. Register django_taggit
        modified:   config/settings.py

        # 3. Add tagable manager
        modified:   apps/blog/models.py

        # 4. Add tags field to form
        modified:   apps/blog/forms.py

        # 5. Run migration
        new file:   apps/blog/migrations/0004_post_tags.py
        
        # 6. Testing
        - Tags added to post
        - Tags save to admin panel
        - But tags not added to Post filed in admin panel

        modified:   README.md

        :)?

#### 10.2 Filtering blog posts by a tag

        modified:   README.md
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        modified:   templates/base.html
        modified:   templates/blog/detail.html
        modified:   templates/blog/home.html

        :)


## 11. Pagination

#### 11.1 Paginator class

        modified:   README.md
        modified:   apps/blog/views.py
        new file:   templates/inc/_pagination.html

#### 11.2 Including templates

        modified:   README.md
        modified:   templates/blog/home.html

        :)