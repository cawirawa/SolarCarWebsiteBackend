* Initialize virtual environment:
1.  command:
    'python3 -m venv NAME'
    NAME - any name for the virtual environment
    normally venv

* Activate virtuaal environment:
1.  command:
    'source NAME/Scripts/activate'

* Install dependencies:
1.  command:
    'pip install django djangorestframework django-cors-headers pillow django-image-cropping'

* Start Project:
1.  command:
    'django-admin startproject NAME'
    NAME - Project name

* Start App:
1.  command:
    'django-admin startapp NAME'
    NAME - App name

* Start virtual server:
1.  command:
    'python manage.py startserver'

* Create super user:
1.  command:
    'python3 manage.py createsuperuser'

* Migrate:
1.  command: 
    'python manage.py makemigrations'
2.  command:
    'python manage.py migrate' or 
    'python manage.py migrate --run-syncdb'