# how to use css in python_ flask
# flask render_template example
 
from flask import Flask, render_template
 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page.html')
 
if __name__=='__main__':
    app.run(debug = True)