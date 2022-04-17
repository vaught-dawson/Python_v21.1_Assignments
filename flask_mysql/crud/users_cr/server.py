from flask import Flask, redirect, render_template, request
from models.user import User
app = Flask(__name__)


@app.route('/users')
@app.route('/users/')
def display_all_users():
    users = User.get_all()
    return render_template("display_all_users.html", all_users=users)


@app.route('/users/new')
@app.route('/users/new/')
def create_user_page():
    return render_template("create_user_page.html")


@app.route('/users/create', methods=['post'])
def create_user_in_db():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.save(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
