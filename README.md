# Fraud Detection and Analysis System
This is a machine learning and Django-based system 

This is a web-based fraud detection and sales analysing system for an insurance company that has three main modules which are Client, Sales support and manager,i developed this system while I was doing my final year at the university. First of all, before I train and test algorithm models to detect fraud, I analyze the datasets following CRISP-DM techniques.

## project is live and running on heroku
This system was hosted and running on Amazon Elastic Compute Cloud (EC2) instances and later on, Amazon removed it because I failed to pay my bills. For now, the system is live and running on Heroku and on 28 November Heroku will remove it because other free resources such as postgresql which are used by this system will be no longer supported.
### Project Link
- username: test
- password: 1111
#### Please note that the test user is a super user of the system after login with this creditials you will be granted all system privilages
- client site of the system
  
  https://boiling-earth-35730.herokuapp.com/
  
- sales support site
  
  https://boiling-earth-35730.herokuapp.com/secret

- manager site
  
  https://boiling-earth-35730.herokuapp.com/manager
  

## System Description for Visualization of Data

While working with the dataset, I used  Matplotlib, tabulate and Seaborn to visualize particular information from the dataset. The System has a manager site, where I analyze insurance sales and visualize them in form of graphs such as bar charts and piecharts. The managers are enabled to download the charts in many different forms such as images and Microsoft Excel.  It has a sales support site where the sales support is enabled to import and export the data in different formats such as CSV, SQL and Microsoft Excel

## Transparency of Data

The fraud detection part of the system is specifically detecting whether the claim is fraudulent or legitimate while the client claiming for their benefits during an incident. So far the system is enabled to detect whether the claim is fraudulent or legitimate and report or revealed it to the sales support team of the insurance. 

## Main Working Functionality of the System

- Registering of clients using social apps google
- Two-factor authentication using Google authenticator and Twillio
- Subscribing for policy and payments with Stripe
- Make claims online 
- fraud Detection
- policy sales analysis and visualisation of them in bar charts and piecharts



## Goals of the System
My goal is to build a fully functioning system that will allow clients to subscribe to policy online.The system is supposed to verify whether the clients are who they claim they are while registering and claiming their benefits using deep learning algorithms. To build the system that will predict what will be the sales of policy in the coming weeks, months or even years. The system will have recommendations for functionality

## Recommendations

My recommendation to everyone in the field of analysing data from large Datasets is to follow CRISP-DM  Techniques while working with large and complicated datasets.

## How to Run Project locally

To get started please ensure that Python 3.8 or above is installed in your system

- Create a project directory
  ```
  mkdir project folder
  ```

- go to the project folder
  ```
  cd projectfolder
  ```

- Create a virtual environment
  ```
  python -m venv env
  ```
- Activate the virtual environment
  ```
  source env/bin/activate
  ```
- Then clone the project
  ```
  git clone https://github.com/LomNtetha/fraudDetection.git
  ```
- go to the project directory
  ```
  cd fraudDetection
  ```

- Install requirements file
  ```
  pip install -r requirements.txt
  ```
- Apply any migrations mistakenly unapplied
  ```
  python manage.py makemigrations
  ```
- migrate Database
  ```
  python manage.py migrate
  ```

- Create super user
  ```
  python manage.py createsuperuser
  ```

- Collect static folder
  ```
  python manage.py collectstatic
  ```
- Compress the static folder for betterment of website perfotmance
  ```
  python manage.py compress --force
  ```
- run the project
  ```
  python manage.py runserver
  ```
## How to run  jupyter nootebook script
- You can install anaconda on your system that has both jupyter notebook and jupyter lab environments
- you can use jupyter nootebook python shell with django by run this command
 ```
 python manage.py shell_plus --notebook
 ```
## How to push the project on cloud Heroku PAAS

Ensure that  heroku cli and git are installed on your system

on project directory
- Run The following command and Heroku will automatically create a project name for you
  ```
  Heroku create
  ```

- add all files you need to post to Heroku
  ```
  git add .
  ```

- commit changes with some comments
 ```
 git commit -m "My comments"
 ```
     
- Ensure that new Heroku projet repository link  are listed (they will be 4 links including of GitHub)
  ```
  git remote -v
  ```

- push the project to Heroku
  ```
  git push heroku master
  ```

- Create migrations and super-user
  ```
  heroku run python manage.py migrate
  ```

  ```
  heroku run python manage.py createsuperuser
  ```

- open the project
  ```
  Heroku open
  ```
In this stage the project will fail to open because the configuration process is not yet done,so let's continue.

 To use Postgresql on Heroku we must ensure that Postgresql is available on our Heroku oddons 

 - run the command below, it will list addons available including heroku-postgresql
  ```
   heroku addons
  ```
- open postgresql oddons
  ```
  heroku addons:open heroku-postgresql
  ```

- check configarion variables. we must configure our secret keys so that they can not be exposed to hackers
- this command will list all secret keys and our variables that are configured
  ```
  heroku config
  ```
- then set all of your variables' secret keys like this:
 ```
  heroku config:set DJANGO_SECRET_KEY="pleaseenteryourowndjangosecretkey"
  ```
- Then set for debug to false
  ```
  heroku config:set DJANGO_DEBUG=False
  ```
- go to your settings and change allow the host to something like this please use your own heroku app name
ALLOWED_HOSTS = ['https://boiling-earth-35730.herokuapp.com/','boiling-earth-35730.herokuapp.com', '127.0.0.1']

-Then save your settings and commit them to your GitHub repository and to Heroku:




