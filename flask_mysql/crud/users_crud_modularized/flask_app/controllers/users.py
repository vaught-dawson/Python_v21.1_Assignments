from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


@app.route('/')
def index():
    return 'Users CRUD Modularization Assignment'


@app.route('/users')
@app.route('/users/')
def display_all_users():
    users = User.get_all()
    return render_template("display_all_users.html", all_users=users)


@app.route('/users/new')
@app.route('/users/new/')
def create_user_page():
    return render_template("create_user_page.html")


@app.route('/users/<int:numId>')
@app.route('/users/<int:numId>/')
def display_one_user(numId):
    user = User.get_one(numId)
    return render_template("display_one_user.html", user=user)


@app.route('/users/<int:numId>/edit')
@app.route('/users/<int:numId>/edit/')
def edit_one_user(numId):
    user = User.get_one(numId)
    return render_template("edit_one_user.html", user=user)


@app.route('/users/<int:numId>/destroy')
def delete_user_in_db(numId):
    User.delete(numId)
    return redirect('/users')


@app.route('/users/create', methods=['post'])
def create_user_in_db():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    newUserId = User.save(data)
    return redirect(f'/users/{newUserId}')


@app.route('/users/<int:numId>/update', methods=['post'])
def update_user_in_db(numId):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': int(numId)
    }

    User.update(data)
    return redirect(f'/users/{numId}')
