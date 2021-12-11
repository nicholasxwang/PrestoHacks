#Imports
from flask import Flask, render_template, request
from waitress import serve
import os
from flask_mail import Mail, Message


#Inits
app = Flask('app')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'virtualholidaysmidnighthacks@gmail.com'
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

@app.route('/search')
def search():
  return render_template("search.html")
#Requests
@app.route("/sendEmail",methods=["POST"])
def send_email(head, body):
  return

@app.route('/checkBetaKey', methods=['POST'])
def check():
  l = open("codes.txt").readlines()
  for i in range(0,len(l)):
    l[i] = l[i][0:5]
  val = request.form.get('v')
  print(val)
  boolean = (val in l)
  print(str(val) + " is: "+str(boolean))
  if val not in l:
    return 'f'
    
  return 't'
#Run
serve(app, host="0.0.0.0", port=8080)
