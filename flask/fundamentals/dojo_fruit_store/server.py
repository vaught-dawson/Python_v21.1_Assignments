import datetime
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'development_key'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout/submit', methods=['POST'])
def checkout_submit():
    print(request.form)
    session['checkout_form'] = request.form
    return redirect('/checkout')


@app.route('/checkout')
def checkout():
    count = 0
    count += int(session['checkout_form']['strawberry'])
    count += int(session['checkout_form']['raspberry'])
    count += int(session['checkout_form']['apple'])
    session['count'] = count
    session['date'] = datetime.datetime.now()
    return render_template("checkout.html", session=session)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
