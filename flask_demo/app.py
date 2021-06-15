from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        try:
            operation=request.form['operation']
            num1=int(request.form['num1'])
            num2 = int(request.form['num2'])
            if(operation=='add'):
                r=num1+num2
                result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
            if (operation == 'subtract'):
                r = num1 - num2
                result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'multiply'):
                r = num1 * num2
                result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'divide'):
                r = num1 / num2
                result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            return render_template('results.html',result=result)
        except Exception as e:
            return render_template("error.html", errors = e)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        try:
            operation=request.json['operation']
            num1=int(request.json['num1'])
            num2 = int(request.json['num2'])
            if(operation=='add'):
                r=num1+num2
                result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
            if (operation == 'subtract'):
                r = num1 - num2
                result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'multiply'):
                r = num1 * num2
                result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'divide'):
                r = num1 / num2
                result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            return jsonify(result)
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.",e)


if __name__ == '__main__':
    app.run(debug=True)
