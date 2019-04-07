# ListTheseServers
This simple web application presents a list of (game or regular) servers which are filterable. Clients may add servers, which are to be approved by site moderators. The web application will automatically ping the servers to determine their connectivity. These pings will occur periodically in the background every 20 seconds and broadcast to any existing clients; updating the server list.



## Technologies used

* Flask
* Celery
* PostgreSQL
* Redis
* React


## Installation

To install all dependencies (assure you have **Python 3.6.\***, this project does not support Python 3.7.* since Celery does not);
```bash
# create a virtual environment & activate it
sudo apt-get install virtualenv
virtualenv -p python3.6 ./venv
source venv/bin/activate

# install python dependencies
pip install -r requirements.txt

# install redis
sudo apt-get install redis-server
sudo apt-get install redis-cli
```

**NOTE** Database information is in settings.py. You will require a local postgressql server.
To setup the database (variables in curly brackets should be substitued with values from settings.py)
```bash
# install postgres
sudo apt-get install postgresql postgresql-contrib

# create the database and user
sudo su - postgres
psql
create database {db name};
create user {db user} with password '{db user password}';
grant all privileges on database nitrox to nitrox;
\q
exit

# migrate and update the database schema
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

```


## Running the web application

To run the app,
```bash
# start the redis-server
redis-server

# start the flask app
export FLASK_APP=run_flask.py
flask run
# or flask run -h 0.0.0.0 -p 8000 for host, port args

# start the celery process and beat workers
celery worker --beat -A run_celery.celery --loglevel=debug # you decide log level
```
