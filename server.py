from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

@app.route('/ninjacolor/<color>')
def ninja_color(color):
    if color == 'blue':
        return render_template("ninjacolor.html", image_src='static/leonardo.jpg')
    elif color == 'orange':
        return render_template("ninjacolor.html", image_src='static/michelangelo.jpg')
    elif color == 'red':
        return render_template("ninjacolor.html", image_src='static/raphael.jpg')
    elif color == 'purple':
        return render_template("ninjacolor.html", image_src='static/donatello.jpg')
    else:
        return render_template("ninjacolor.html", image_src='static/april.jpg')


app.run(debug=True)