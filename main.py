#Imports
from flask import Flask, render_template

#Inits
app = Flask('app')

#Routing
@app.route('/')
def main():
  return render_template('index.html')

#Run
app.run(host='0.0.0.0', port=8080)
