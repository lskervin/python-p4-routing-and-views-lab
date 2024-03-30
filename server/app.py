#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    # Generate numbers separated by newline characters
    numbers = '\n'.join(str(i) for i in range(parameter))
    return numbers + '\n' # Return numbers separated by newline characters

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        # Check for division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        raise ValueError("Error: Invalid operation")
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
