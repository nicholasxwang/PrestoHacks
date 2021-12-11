#Imports
from flask import Flask, render_template
from waitress import serve

#Inits
app = Flask('app')

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
app.run(host='0.0.0.0', port=8080)
