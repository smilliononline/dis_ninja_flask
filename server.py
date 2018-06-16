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
        return render_template("ninjacolor.html/#leonardo")
    elif color == 'orange':
        return render_template("ninjacolor.html/#michelangelo")
    elif color == 'red':
        return render_template("ninjacolor.html/#raphael")
    elif color == 'purple':
        return render_template("ninjacolor.html/#donatello")
    else:
        return render_template("ninjacolor.html/#april")


app.run(debug=True)