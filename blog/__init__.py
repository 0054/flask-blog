from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# >>> import secrets
# >>> secrets.token_hex(16)
app.config['SECRET_KEY'] = 'fd807ecee9774c7027daed87270b24ed'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from blog import routes
