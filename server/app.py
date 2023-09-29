#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_route():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_route(text):
    print(text)
    return 'hello'

@app.route('/count/<int:num>')
def count_route(num):
    return '\n'.join(str(i) for i in range(num)) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_route(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        if num2 != 0:
            return str(num1 / num2)
        else:
            return 'Division by zero is not allowed.'
    elif operation == '%':
        if num2 != 0:
            return str(num1 % num2)
        else:
            return 'Modulo by zero is not allowed.'
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
