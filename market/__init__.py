'''
We don't need them with the current architecture
export FLASK_APP='market'
export FLASK_DEBUG=1
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #__name__ => local file name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from market import routes