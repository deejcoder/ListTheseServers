# export FLASK_APP=run_flask.py; flask run
from factory import Factory


factory = Factory('app')
app = factory.get_app()
app.run()
