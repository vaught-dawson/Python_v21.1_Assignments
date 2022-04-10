from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'development_key'


@app.route('/')
def init_count():
    if not 'visits' in session:
        session['visits'] = 0
        session['count'] = 0
    session['visits'] += 1
    return render_template('index.html', count=session['visits'])


@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')


@app.route('/count', methods=['POST'])
def add_to_count():
    print(request.form)
    if 'num' in request.form:
        num = int(request.form['num'])
    session['count'] += num
    session['visits'] -= 1
    return redirect('/')

 # This needs to stay at the bottom!
if __name__ == "__main__":
    app.run(debug=True)
