from flask import Flask
app = Flask(__name__)
app.secret_key = "development_key"
app.DATABASE = 'dojos_and_ninjas_db'
