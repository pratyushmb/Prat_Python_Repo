# Flask API- web app development framework. web app- applications run over internet
# framework - collection of libraries, libraries- collection of methods.
# this can be used to build our own web app
# very important: Flask is following specific structure to maintain other files like html
# it expects the html files to reside inside 'temp' folder. so create that directory.

from flask import Flask, request, jsonify, render_template

calc = Flask(__name__)  # created Flask app

@calc.route('/', methods=['GET'])
def index_page():
    return render_template('index_page.html')  # inbuilt flask method to showcase this web page into browser

@calc.route('/via_postman', methods=['POST'])  # calling the API from POSTMAN
def math_operation_via_postman():
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        result_val = ''

        if operation == 'add':
            r = num1 + num2
            result_val = "the sum of " + str(num1) + ' and ' + str(num2) + ' is ' + str(r)

        if operation == 'subtract':
            r = num1 - num2
            result_val = "the difference of " + str(num1) + ' and ' + str(num2) + ' is ' + str(r)

        if operation == 'multiply':
            r = num1 * num2
            result_val = "the product of " + str(num1) + ' and ' + str(num2) + ' is ' + str(r)

        if operation == 'divide':
            r = num1 % num2
            result_val = "the quotient when " + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)

        return jsonify(result_val)

if __name__ == '__main__':  # executing Flask app
    print("my app is running..")
    calc.run()

