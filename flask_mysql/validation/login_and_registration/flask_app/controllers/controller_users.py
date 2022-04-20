from flask_app import app, bcrypt
from flask import render_template, redirect, request, session
from flask_app.models.model_user import User


@app.route('/')
def index():
    if session.get('id'):
        return redirect('/dashboard')
    return render_template('index.html')


@app.route('/dashboard')
@app.route('/dashboard/')
def display_dashboard():
    if not session.get('id'):
        return redirect('/')
    user = User.get_one_from_id(session['id'])
    return render_template('dashboard.html', user=user)


@app.route('/users/logout')
def log_user_out():
    session['id'] = None
    return redirect('/')


@app.route('/users/create', methods=['post'])
def create_users_in_db():
    if not User.validate_new_user(request.form):
        return redirect('/')

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }

    newUserId = User.save(data)
    session['id'] = newUserId

    return redirect('/dashboard')


@app.route('/users/login', methods=['post'])
def user_login():
    if not User.validate_user_login(request.form):
        return redirect('/')

    user = User.get_one_from_email(request.form['email'])
    print(user.id)
    session['id'] = user.id
    return redirect('/dashboard')
