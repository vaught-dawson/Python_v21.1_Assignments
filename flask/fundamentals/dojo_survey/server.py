from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'development_key'


@app.route('/')
def main_site():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    session['survey'] = request.form
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')


 # This needs to stay at the bottom!
if __name__ == "__main__":
    app.run(debug=True)
