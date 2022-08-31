from flask import Flask, render_template, request, redirect, url_for
import os 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# Home PAGE
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

# Binary/Decimal/Hex/Octal Converter PAGE
@app.route('/convert', methods=['GET','POST'])
def convert():
    if request.method == 'POST':
        if request.form['dec']:
            decimal = int(request.form['dec'], 10)
            binary = bin(decimal)[2:] 
            octdecimal = oct(decimal)[2:]
            hexdecimal = hex(decimal)[2:].upper()
            return render_template('convert.html', decimal=decimal, binary=binary, hexdecimal=hexdecimal, octdecimal=octdecimal)
        elif request.form['bin']:
            binary = request.form['bin']
            decimal = int(binary, 2)
            octdecimal = oct(decimal)[2:]
            hexdecimal = hex(decimal)[2:].upper()
            return render_template('convert.html',  decimal=decimal, binary=binary, hexdecimal=hexdecimal, octdecimal=octdecimal)
        elif request.form['hex']:
            hexdecimal = request.form['hex']
            decimal = int(hexdecimal, 16)
            octdecimal = oct(decimal)[2:]
            binary = bin(decimal)[2:]
            return render_template('convert.html',  decimal=decimal, binary=binary, hexdecimal=hexdecimal, octdecimal=octdecimal)
        elif request.form['oct']:
            octdecimal = request.form['oct']
            decimal = int(octdecimal, 8)
            binary = bin(decimal)[2:]
            hexdecimal = hex(decimal)[2:].upper()
            return render_template('convert.html',  decimal=decimal, binary=binary, hexdecimal=hexdecimal, octdecimal=octdecimal)
    return render_template('convert.html')

if __name__ == '__main__':
    app.run(debug=True)
