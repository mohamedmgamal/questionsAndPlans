# Questions And Plans

# Getting Started

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/mohamedmgamal/questionsAndPlans/ \
      --extension=py,md \
      questionsAndPlans


      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
       --template=https://github.com/mohamedmgamal/questionsAndPlans/ \
      --extension=py,md \
      quetionsAndPlans
      
# clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/mohamedmgamal/questionsAndPlans
    $ cd questionsAndPlans
    
Activate the virtualenv for your project.

Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
    
    You can creaate new super user by running :
      
      python manage.py createsuperuser
      
    
You can check api endpoind documentation on postman from :

https://documenter.getpostman.com/view/14601930/UVXerHbD
