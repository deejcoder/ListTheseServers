# ListTheseServers
A web application containing a collection of servers around the world. These servers may have tags, and will be filterable and searchable by tags. Want to find a server for your game? Search the tag. This web application will also track downtime of these servers and handle reports. Anyone may add a server.



### Technologies used

* Flask
* Celery
* PostgreSQL
* Redis
* React
* Docker

### Prerequisites

* Ubuntu 16.0.4/Debian 9 (no Windows support)
* Python 3.6.*

### Installation
Please note that in the future, this will be automated using either a simple shell script, or docker. There will be two versions; one for development, and one for production.

To install all dependencies (assure you have **Python 3.6.\***, this project does not support Python 3.7.* since Celery 4 does not, please wait for Celery 5);
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

Pull submodules
```bash
# update submodules: materialize, flag-icon-css etc.
git submodule update --init --recursive
```


### Running the web application

To run the app,
```bash
# start the redis-server
redis-server

# start the flask REST API
export FLASK_APP=run_flask.py
flask run
# or flask run -h 0.0.0.0 -p 8000 for host, port args

# start the celery process and beat workers
celery worker --beat -A run_celery.celery --loglevel=debug # you decide log level

# start React for frontend
cd src/http/web/app
npm run start
```


### Recommended setup for when we grow
- One server to serve the REST API; potentially in the future many Redis nodes. A load balancer could be used here too as well as rate limiting
- One server to serve the frontend (React)
- One server to serve the database