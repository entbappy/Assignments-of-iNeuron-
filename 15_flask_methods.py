# Bappy Ahmed

from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

#1. This is a sum function
@app.route('/sum', methods= ['POST'])
def sum_function():  
    if (request.method=='POST'):
        try:
            num1=int(request.json['num1'])
            num2 = int(request.json['num2'])
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
            return jsonify(result)
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")


# 2. This is a subtract function
@app.route('/subtract', methods= ['POST'])
def subtract_function():  
    if (request.method=='POST'):
        try:
            num1=int(request.json['num1'])
            num2 = int(request.json['num2'])
            r=num1-num2
            result= 'the subtract of '+str(num1)+' and '+str(num2) +' is '+str(r)
            return jsonify(result)
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")


# 3. This is a multiply function
@app.route('/multiply', methods= ['POST'])
def multiply_function():  
    if (request.method=='POST'):
        try:
            num1=int(request.json['num1'])
            num2 = int(request.json['num2'])
            r=num1*num2
            result= 'the multiply of '+str(num1)+' and '+str(num2) +' is '+str(r)
            return jsonify(result)
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")


# 4. This is a divide function
@app.route('/divide', methods= ['POST'])
def divide_function():  
    if (request.method=='POST'):
        try:
            num1=int(request.json['num1'])
            num2 = int(request.json['num2'])
            r=num1/num2
            result= 'the divition of '+str(num1)+' and '+str(num2) +' is '+str(r)
            return jsonify(result)
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")


# 5. This is a square function
@app.route('/square', methods= ['POST'])
def square_function():  
    if (request.method=='POST'):
        try:
            num1=int(request.json['num1'])
            num2 = int(request.json['num2'])
            r=num1**num2
            result= 'the square of '+str(num1)+' and '+str(num2) +' is '+str(r)
            return jsonify(result)
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")



# 6. Flip over your name
@app.route('/flip_name', methods = ['POST'])
def flip_name():
    if (request.method == 'POST'):
        try:
            fname = request.json['fname']  # your first name
            lname = request.json['lname']  # your last name

            nameList = []
            nameList.append(fname)
            nameList.append(lname)

            final_name = []

            for name in nameList:
                name_r = name[-1::-1]
                final_name.append(name_r)

            return jsonify(f"{final_name[0]} {final_name[1]}")

        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")



# 7. find the volume of a sphere
import math
@app.route('/sphere_volume', methods= ['POST'])
def sphere_volume():  
    if (request.method=='POST'):
        try:
            Pi = math.pi
            r = int(request.json['redius'])  # redius
            # formula of volume of a sphare : V=4/3 * π * r 3
            v = 4/3 * Pi * r**3
            return jsonify(f"The volume is {v}")

        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")



# 8. reverse any string
@app.route('/reverse', methods= ['POST'])
def reverse():  
    if (request.method=='POST'):
        try:
            user = request.json['user']  #put any string 
            return jsonify(user[-1::-1])

        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")


# 9.  pattern printing
@app.route('/pattern', methods= ['POST'])
def pattern():  
    if (request.method=='POST'):
        try:
            num = int(request.json['num'])
            for i in range(1, num):
                return jsonify(f"{'#'* i}")
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")


#10. function to convert degree to radian.
@app.route('/convert_degree', methods= ['POST'])
def convert_degree():  
    if (request.method=='POST'):
        try:
            Pi= math.pi
            degree = float(request.json['degree'])  #put the degree
            radian = degree*(Pi/180)
            return jsonify(f"The radian is {radian}")
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")



#11. function to convert radian to degree.
@app.route('/convert_radian', methods= ['POST'])
def convert_radian():  
    if (request.method=='POST'):
        try:
            Pi= math.pi
            radian = float(request.json['radian'])  #put the radian
            degree = radian*(180/Pi)
            return jsonify(f"The degree is {degree}")
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")





# 12. Fuction to calculate the area of a trapezoid.
@app.route('/trapezoid', methods= ['POST'])
def trapezoid():  
    if (request.method=='POST'):
        try:
            height = float(request.json['height'])
            base_1 = float(request.json['base1'])
            base_2 = float(request.json['base2'])
            area = ((base_1 + base_2) / 2) * height

            return jsonify(f"Area is {area}")
           
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")



#13. function to calculate the area of a parallelogram
@app.route('/parallelogram', methods= ['POST'])
def parallelogram():  
    if (request.method=='POST'):
        try:
            base = float(request.json['base'])
            height = float(request.json['height'])
            area = base * height

            return jsonify(f"Area is {area}")
           
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")



# 14. function to calculate area of circle
@app.route('/circle', methods= ['POST'])
def circle():  
    if (request.method=='POST'):
        try:
            Pi = math.pi
            redius = float(request.json['redius'])
            area = Pi*redius**2
            return jsonify(f"Area is {area}")
           
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")




# 15. function of sum of all divisors of a number
@app.route('/divisors_sum', methods= ['POST'])
def divisors_sum():  
    if (request.method=='POST'):
        try:
            sums = 0
            num = int(request.json['num'])
            for i in range(num+1):
                if i%2 == 0:
                    sums += i
           
            return jsonify(f"The sum is {sums}")
           
        except Exception as e:
            return jsonify("Sorry!! there is some issue with your input please check it.")















if __name__ == '__main__':
    app.run(debug= True)


