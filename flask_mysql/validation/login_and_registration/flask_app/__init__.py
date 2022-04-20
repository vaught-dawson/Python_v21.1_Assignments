from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "development_key"
app.DATABASE = 'login_registration_db'
bcrypt = Bcrypt(app)
