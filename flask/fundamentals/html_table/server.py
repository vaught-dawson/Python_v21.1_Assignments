from flask import Flask, render_template
app = Flask(__name__)

# This changes locations in the future!


@app.route('/')
def table():
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template('index.html', users=users)

 # This needs to stay at the bottom!
if __name__ == "__main__":
    app.run(debug=True)
