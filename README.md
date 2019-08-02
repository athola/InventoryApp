# InventoryApp
Python application which searches for and updates inventory items in a database

Use:

Running pipenv:

If checking out the repository, this application uses pipenv to run a virtual environment on Windows.

To use pipenv, type the following in cmd while in the root directory:
<b>python -m pipenv shell</b>

To update pipenv if installing new pip package while in pipenv shell, type:
<b>pipenv update</b>

To run python scripts in pipenv, type:
<b>pipenv run filename.py</b>

Running app:

This app can be viewed via webserver hosted on heroku at the following addresses:
Staging:
https://inventory-app-stage.herokuapp.com/

Production:
https://inventory-app-pro.herokuapp.com/

To run locally, enter the pipenv shell environment and type:
<b>pipenv run manage.py runserver</b>

If running outside of virtual environment, you need to be sure that your environment variables are set correctly.
These are set in the .env file, and this application also makes use of a Procfile.

The app will run on http://127.0.0.1:5000/

Database:
This database was created using Postgres and the Flask interface for passing SQL statements is SQLAlchemy

The database's __init__ located in models.py can be updated by the following command:
<b>pipenv run manage.py db init</b>

The database's migrate used by Flask-Migrate uses the following command:
<b>pipenv run manage.py db migrate</b>

The database can be upgraded by the following command:
<b>pipenv run manage.py db upgrade</b>

To connect to the database use psql and type:
<b>\c inventory_dev</b>

To list relations type:
<b>\dt</b>

To list columns, types, and modifiers type:
<b>\d grocery_items</b>

Remote migration:
To stage heroku app and check if database is running type:
<b>heroku config --app inventory-app-stage</b>

If database environment variable isn't set up, type:
<b>heroku addons:create heroku-postgresql:hobby-dev --app inventory-app-stage</b>

Then do a push to the stage environment:
<b>git push stage master</b>

Run migrations created to migrate staging database using:
<b>pipenv run heroku run python manage.py db upgrade --app inventory-app-stage</b>

Do same for production server:
<b>heroku config --app inventory-app-pro</b>

<b>heroku addons:create heroku-postgresql:hobby-dev --app inventory-app-pro</b>

<b>git push pro master</b>

<b>pipenv run heroku run python manage.py db upgrade --app inventory-app-pro</b>
