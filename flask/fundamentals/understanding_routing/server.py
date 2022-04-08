from os import stat
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<string:name>')
def say_my_name(name):
    return f'Hi {name}!'


@app.route('/repeat/<string:word>/<int:num>')
def repeat_after_me(word, num):
    return f'{word * num}'


@app.errorhandler(404)
def no_content_error(status):
    status = 200
    return 'Sorry! No response. Try again.'


# This needs to stay at the bottom!
if __name__ == "__main__":
    app.run(debug=True)
