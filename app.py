from flask import Flask

from entity.calculator import Calculator

app = Flask(__name__)
calc = Calculator()


@app.route('/')
def hello_world():
    return f"Hello, world"


@app.route("/add/<int:a>&<int:b>")
def add(a, b):
    return f"Add {a} and {b}. Got {calc.add(a, b)}!"


@app.route("/multiply/<int:a>&<int:b>")
def multiply(a, b):
    return f"Multiply {a} and {b}. Got {calc.multiply(a, b)}!"


@app.route("/subtract/<int:a>&<int:b>")
def subtract(a, b):
    return f"Subtract {a} and {b}. Got {calc.subtract(a, b)}!"


@app.route("/divide/<int:a>&<int:b>")
def divide(a, b):
    return f"Divide {a} and {b}. Got {calc.divide(a, b)}!"


if __name__ == '__main__':
    app.run()
