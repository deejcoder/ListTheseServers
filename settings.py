from flask import Flask


app = Flask(__name__, static_url_path='/static')

POSTGRES = {
    'user': 'nitrox',
    'pw': 'nitroxserverlistpass',
    'db': 'nitrox',
    'host': 'localhost',
    'port': 5432,
}
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{pw}@{host}:{port}/{db}'.format(**POSTGRES)