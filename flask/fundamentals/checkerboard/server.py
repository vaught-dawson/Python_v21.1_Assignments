from flask import Flask, render_template
app = Flask(__name__)

# This changes locations in the future!


@app.route('/')
def initial_checkerboard():
    return render_template('index.html', color1='red', color2='black', width=8, height=8)


@app.route('/<int:height>')
def height_restricted_checkerboard(height):
    return render_template('index.html', color1='red', color2='black', width=8, height=height)


@app.route('/<int:height>/<int:width>')
def custom_size_checkerboard(height, width):
    return render_template('index.html', color1='red', color2='black', width=width, height=height)


@app.route('/<int:height>/<int:width>/<string:color1>')
def custom_size_one_color_checkerboard(height, width, color1):
    return render_template('index.html', color1=color1, color2='black', width=width, height=height)


@app.route('/<int:height>/<int:width>/<string:color1>/<string:color2>')
def custom_size_two_color_checkerboard(height, width, color1, color2):
    return render_template('index.html', color1=color1, color2=color2, width=width, height=height)

 # This needs to stay at the bottom!
if __name__ == "__main__":
    app.run(debug=True)
