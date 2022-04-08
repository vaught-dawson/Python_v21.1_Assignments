from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/success')
def success():
    return 'Success!'


@app.route('/hello/<string:banana>/<int:num>')
def hello(banana, num):
    return f'Hello {banana * num}'


@app.route('/lists')
def lists():
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers=[3, 1, 5], students=student_info)


if __name__ == "__main__":
    app.run(debug=True)
