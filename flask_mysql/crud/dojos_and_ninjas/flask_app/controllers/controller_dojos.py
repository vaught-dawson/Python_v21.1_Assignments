import re
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.model_dojo import Dojo


@app.route('/dojos')
@app.route('/dojos/')
def display_all_dojos():
    dojos = Dojo.get_all()
    return render_template("dojos_create.html", all_dojos=dojos)


@app.route('/dojos/<int:numId>')
@app.route('/dojos/<int:numId>/')
def display_one_dojo(numId):
    dojo = Dojo.get_dojo_with_ninjas(numId)
    return render_template("dojos_display_one.html", dojo=dojo)


@app.route('/dojos/create', methods=['post'])
def create_dojos_in_db():
    data = {
        'name': request.form['dojo_name']
    }

    new_dojo_id = Dojo.save(data)
    return redirect('/dojos')
