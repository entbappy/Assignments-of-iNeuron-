#Bappy Ahmed

from flask import Flask, request, jsonify, render_template
import pymongo


DB_NAME = "login_system" # Specifiy a Database Name


# Connection URL
CONNECTION_URL = "mongodb+srv://entbappy:entbappy73@cluster0.bc4o5.mongodb.net/userinfo?retryWrites=true&w=majority"

# Establish a connection with mongoDB
client = pymongo.MongoClient(CONNECTION_URL)

# Create a DB
dataBase = client[DB_NAME]

# Create a Collection Name
COLLECTION_NAME = "info"
collection = dataBase[COLLECTION_NAME]



app = Flask(__name__)


@app.route('/', methods=['GET']) # Rendering hompage
def login():
    return render_template('login.html')



@app.route('/welcome', methods=['POST'])  #For calling the API from webapp
def welcome():
    if (request.method == 'POST'):
        email = request.form['email']
        passw = request.form['password']

        email_list = []
        pass_list = []
        
        all_record = collection.find()

        for record in all_record:
            emails = record['email']
            email_list.append(emails)
            passes = record['password']
            pass_list.append(passes)
        
        if email in email_list and passw in pass_list:
            return render_template('welcome.html')
        
        else:
            return render_template('error.html')



@app.route('/registration', methods=['POST'])  #For calling the API from webapp
def registration():
    if (request.method == 'POST'):
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        list_of_records = {'name': name,
                            'email': email,
                            'phone': phone,
                            'password':password}
                           

        collection.insert_one(list_of_records)


        return render_template('done.html')



if __name__ == '__main__':
    app.run(debug=True)

