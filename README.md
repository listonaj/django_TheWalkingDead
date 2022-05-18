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
7. tells you that there are no issues - close windows

STEP 2: Starting an App

1. let the server opened in step1 1 running,  and open another terminal window,
2. go to the virtiual environment directory that contain manage.py, and activate the virtual environment for that new session (<source ll_env/bin/activate> for linux or in windows <source ll_env/scripts/activate>)
3. if you use vs code to open terminal, the virtual environment should already been activate and you don't have to do it manually
4. I have used git bash that emulates linux commands line  
5. at the terminal enter command : <python manage.py startapp theWalkingDead> (you have to find other name than the project name or error)

STEP 3: Defining Model

1. open the file <models.py> that is located on the app folder created at step 2
2. see code entered
3. activate your model in the <settings.py> file
4. in the field installed apps add your app between single quote 'theWalkingDead' - character sensitive(use same name)
5. it is recommended to insert your app in the list before all the others 

STEP 4: Make django modify data base and migrate

1. at the terminal <python manage.py makemigrations theWalkingDead>
2. <python manage.py migrate>

STEP 5: The Django Admin Site

Allow the user to add some toppic through the topic model in the web page. Create a superuser
who have admin privilege to administrate the web page and modify.
1. <python manage.py createsuperuser>
2. the terminal prompt your username:<your_user_name>
3. the terminal prompt your email address: <your_email_address>
4. the terminal prompt for a password: <your_password>

Note : Django create a hash based on your password. Each time you enter your password, Django hash it and compared that hash with the original hash created when you configured your credentials.

STEP 6: Registering the Model with the admin site.

1. go to the file <admin.py>
2. see code 
3. go to http://localhost:8000/admin/ to check your work
4. enter your username and password to make sure it works.
5. Ta daaa!

STEP 6: Adding Topics

1. on the admin page fron django, click on Topics
2. click on the <+> sign to add a topic
3. enter a topi in the text box 
4. click on save when its done
5. add another subject and save it








