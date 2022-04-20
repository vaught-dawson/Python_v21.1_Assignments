from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.model_generic import Generic


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generic')
@app.route('/generic/')
def display_all_generic():
    generic = Generic.get_all()
    return render_template("display_all_generic.html", all_generic=generic)


@app.route('/generic/new')
@app.route('/generic/new/')
def create_generic_page():
    return render_template("create_generic_page.html")


@app.route('/generic/<int:numId>')
@app.route('/generic/<int:numId>/')
def display_one_generic(numId):
    generic = Generic.get_one(numId)
    return render_template("display_one_generic.html", generic=generic)


@app.route('/generic/<int:numId>/edit')
@app.route('/generic/<int:numId>/edit/')
def edit_one_generic(numId):
    generic = Generic.get_one(numId)
    return render_template("edit_one_generic.html", generic=generic)


@app.route('/generic/<int:numId>/destroy')
def delete_generic_in_db(numId):
    Generic.delete(numId)
    return redirect('/generic')


@app.route('/generic/create', methods=['post'])
def create_generic_in_db():
    data = {}
    # data = {
    #     'first_name': request.form['first_name'],
    #     'last_name': request.form['last_name'],
    #     'email': request.form['email']
    # }

    newgenericId = Generic.save(data)
    return redirect(f'/generic/{newgenericId}')


@app.route('/generic/<int:numId>/update', methods=['post'])
def update_generic_in_db(numId):
    data = {}
    # data = {
    #     'first_name': request.form['first_name'],
    #     'last_name': request.form['last_name'],
    #     'email': request.form['email'],
    #     'id': int(numId)
    # }

    Generic.update(data)
    return redirect(f'/generic/{numId}')
