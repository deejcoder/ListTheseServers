# NitroxServerList
Server list in Flask

**NOTE** Database information is in settings.py. You will require a local postgressql server.

To initalize the database, execute
```bash
python manage.py db init
```

To update the database execute
```bash
python manage.py db migrate
python manage.py db upgrade
```

To run the app,
```bash
export FLASK_APP=app.py
flask run
```
