# Jean-Marc Romain _ 05-18-2022
django_TheWalkingDead
lean to build a simple web application using the django framework

source used for intsructions : 
Matthes, Eric. Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming. 2nd ed., No Starch Press, 2019, p. 379

STEPS 1 : create a project

1. create a virtual environment and activate the virtual environment
2. install django: <pip install django>
3. create a project : <django-admin startproject The_Walking_dead>
4. each time we modify the database we call migrate : <python manage.py migrate>
5. run the server: <python manage.py runserver>
6. open a web browser and type the following URL : http://localhost:8000/

STEP 2: Starting an App

1. let the server opened in step1 1 running,  and open another terminal window,
2. go to the virtiual environment directory that contain manage.py, and activate the virtual environment for that new session (<source ll_env/bin/activate> for linux or in windows <source ll_env/scripts/activate>)
3. I have used git bash that emulates linux commands line  
4. at the terminal enter command : <python manage.py startapp theWalkingDead> (you have to find other name than the project name or error)

STEP 3: Defining Model

1. open the file models.py that is located on the app folder created at step 2
2. see code entered



