from flask import Flask, render_template
app = Flask('__name__')


@app.route('/')
def success():
    return 'Success!'


@app.route('/play')
def play():
    return render_template('index.html', title='Playground 1', times=3, color='lightblue')


@app.route('/play/<int:count>')
def play_repeat(count):
    return render_template('index.html', title='Playground 2', times=count, color='lightblue')


@app.route('/play/<int:count>/<string:color>')
def play_repeat_with_color(count, color):
    return render_template('index.html', title='Playground 3', times=count, color=color)


@app.errorhandler(404)
def no_content_error(status):
    status = 200
    return 'Error 404: No content! Enter a valid server route.'


if __name__ == "__main__":
    app.run(debug=True)
