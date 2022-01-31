<strong># This is an introduction to Django teaching from development to advance</strong>

<h4>ACTIVATE THE ENVIRONMENT and INSTALLATIONS</h4>

python -m  venv venv

cd to the project folder and run the command: venv\Scripts\activate

pip install django

django-admin startproject blog dot(.)

pip freeze > requirements.txt

python manage.py startapp blog

python manage.py startapp minecraft

python manage.py runserver //To copy the project url to launch

py manage.py createsuperuser // To create admin login


*whenever you make changes on models.py and you want the changes to occur*

py manage.py makemigrations

py manage.py migrate
