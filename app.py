from flask import Flask, render_template, request, redirect, url_for
import os 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# Login PAGE
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)