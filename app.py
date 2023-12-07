#app.py

from flask import Flask
from views import index

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bampeepmab'

app.register_blueprint(index)
