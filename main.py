#Imports
from flask import Flask, render_template
from waitress import serve
import os
from flask_mail import Mail, Message


#Inits
app = Flask('app')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = '@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('psw')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

#Routing
@app.route('/')
def main():
  return render_template('index.html')
@app.route('/login')
def login():
  return render_template('login.html')
@app.route('/signup')
def signup():
  return render_template('signup.html')

#Requests
#Run
serve(app, host="0.0.0.0", port=8080)
