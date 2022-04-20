from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo


@app.route('/ninjas')
@app.route('/ninjas/')
def create_ninja_page():
    dojos = Dojo.get_all()
    return render_template("ninjas_create.html", all_dojos=dojos)


@app.route('/ninjas/create', methods=['post'])
def create_ninjas_in_db():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_selection']
    }
    print(data)

    Ninja.save(data)
    return redirect('/dojos/' + data['dojo_id'])
