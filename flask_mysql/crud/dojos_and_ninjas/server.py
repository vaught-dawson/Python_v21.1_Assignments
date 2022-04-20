from flask import render_template
from flask_app import app

from flask_app.controllers import controller_dojos
from flask_app.controllers import controller_ninjas


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
