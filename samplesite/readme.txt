Prerequisites:
# MySQL
# Python 2.7.*

To start this project:

1. Create a virtual environment in any directory in your computer
$virtualenv venv

2. Activate this virtual environment
$source venv/bin/activate

3. Install the required packages from requirements.txt using pip
$venv/bin/pip install -r requirements.txt

4. create a new mysql database in your computer using any name you want

5. go to the "samplesite" directory from terminal
cd samplesite

6. open the settings.py file. edit the database settings and provide your database settings. you need to change the following lines
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # no need to change it if you are using mysql
        'NAME': 'django_test', # give the name of your database here
        'USER': 'root', # name of the database user
        'PASSWORD': '1234', # password of the database user. keep "" if user have to no password set
    }
}

here, set your database name to NAME, username to USER and password to PASSWORD

7. go to the project root directory i.e where manage.py exists from terminal. sync the database with the following command
$ python manage.py syncdb

you should see the database table creation messages. create a super user when prompted.

8. run the development server using this command from terminal
$ python manage.py runserver

this will say that development server is running. also you'll see the server url of the development server. 
by default, it should be http://localhost:8000/ if 8000 port is available

9. open your browser and go to the url of the development server. you should see the application running!

