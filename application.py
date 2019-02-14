from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def index():
    headline="Goodbye"
    return render_template("index.html",headline=headline)

@app.route("/<string:name>")
def aki(name):
    name=name.capitalize()
    return f"<h1>Hello, {name}!!!!</h1>"


