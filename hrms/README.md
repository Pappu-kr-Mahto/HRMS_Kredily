
-----------Setup and Running of App (only for windows)--------------

1. Open  command prompt / vs terminal / terminal on the root folder.
    (root folder -  the main folder in which you placed the unzipped file 'hrms' say('projectKredily'))

    or create a folder say('projectKredily') then extract this zip file.
    i>go to E:\projectKredily 

2. E:\projectKredily\python -m venv django_env   -used to create a virtual environment

3. E:\projectKredily\cd django_env       - move to the created enviroment file

4. E:\projectKredily\cd django_env\scripts\activate  -this will activate your environment

5. E:\projectKredily\cd django_env\cd..  --came to root folder

6. E:\projectKredily\cd hrms             -go to the project folder

7. E:\projectKredily\hrms\pip install -r requirements.txt  -- this will install the          requirements module/libraries

8. E:\projectKredily\hrms\python manage.py makemigrations

9. E:\projectKredily\hrms\python manage.py migrate

10. E:\projectKredily\hrms\python manage.py ruserver   -- project will start running on its default port.
    


--------- Modal Schema ------------------
    name =      Full name of the employee
    email= Email
    department= On Which department he/she works
    designation =  designation of the employee
    doj=         Date of joining
    attendance=  store attendance in the form of list of objects.
    isactive=   default =1 , 
    createdAt=  date and time of the entry of the employee record


