from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello World."

@app.route("/<name>")
def greet(name):
    return name + "さん、こんにちは"

@app.route("/template")
def template():
    py_name = "サワガニ"
    return render_template("index.html", name = py_name)

@app.route("/hello")
def hello():
    return render_template("hello.html")
    
@app.route("/hi")
def hi():
    return render_template("hi.html")

@app.route("/weather")
def whether():
    py_weather = "くもり"
    return render_template("weather.html", weather = py_weather)



if __name__ == "__main__":
    app.run(debug=True)