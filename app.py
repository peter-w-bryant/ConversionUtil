from flask import Flask, render_template, request, redirect, url_for
import os 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

def not_bin(bin_string):
    return ''.join('1' if x == '0' else '0' for x in bin_string)

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal  

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
            hexdecimal = hex(decimal)[2:]
            return render_template('convert.html', decimal=decimal, binary=binary, hexdecimal=hexdecimal, octdecimal=octdecimal)
        elif request.form['bin']:
            binary = request.form['bin']
            decimal = int(binary, 2)
            octdecimal = oct(decimal)[2:]
            hexdecimal = hex(decimal)[2:]
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
            hexdecimal = hex(decimal)[2:]
            return render_template('convert.html',  decimal=decimal, binary=binary, hexdecimal=hexdecimal, octdecimal=octdecimal)
    return render_template('convert.html')

# Binary/Decimal/Hex/Octal Calculator PAGE
@app.route('/calculator', methods=['GET','POST'])
def calculator():
    if request.method == 'POST':
        if request.form['options']:
            if request.form['options'] == 'decimal':
                try:
                    operand_1 = request.form.get('op1')
                    operand_2 = request.form.get('op2')
                    operation = request.form.get('operation')
                    if operation == 'addition':
                        operation = '+'
                        result = int(operand_1, 10) + int(operand_2, 10)
                    elif operation == 'subtraction':
                        operation = '-'
                        result = int(operand_1, 10) - int(operand_2, 10)
                    elif operation == 'multiplication':
                        operation = '*'
                        result = int(operand_1, 10) * int(operand_2, 10)
                    elif operation == 'and':
                        operation = 'AND'
                        result = int(operand_1, 10) & int(operand_2, 10)
                    elif operation == 'or':
                        operation = 'OR'
                        result = int(operand_1, 10) | int(operand_2, 10)
                    elif operation == 'not':
                        operation = 'NOT'
                        op1_int = int(operand_1, 10)
                        op1_bin = bin(op1_int)[2:]
                        result = not_bin(bin(op1_int)[2:])
                        return render_template('calculator.html', result=result, op1_bin=op1_bin, op1=operand_1, op2=operand_2, operation = operation, options = 'Decimal')
                    return render_template('calculator.html', result=result, op1 = operand_1, op2 = operand_2, operation = operation, options = 'Decimal')
                except Exception as e:
                    print(e)
                    error = 'Invalid input, please fill out all fields correctly!'
                    return render_template('calculator.html', error=error)
            elif request.form['options'] == 'binary':
                try:
                    operand_1 = request.form.get('op1')
                    operand_2 = request.form.get('op2')
                    operation = request.form.get('operation')
                    if operation == 'addition':
                        operation = '+'
                        result = bin(int(operand_1, 2) + int(operand_2, 2))
                    elif operation == 'subtraction':
                        print("FLAG")
                        operation = '-'
                        result = bin(int(operand_1, 2) - int(operand_2, 2))
                    elif operation == 'multiplication':
                        operation = '*'
                        result = bin(int(operand_1, 2) * int(operand_2, 2))
                    elif operation == 'and':
                        operation = 'AND'
                        result = bin(int(operand_1, 2) & int(operand_2, 2))
                    elif operation == 'or':
                        operation = 'OR'
                        result = bin(int(operand_1, 2) | int(operand_2, 2))
                    elif operation == 'not':
                        operation = 'NOT'
                        op1_int = int(operand_1, 2)
                        op1_bin = bin(op1_int)[2:]
                        result = not_bin(bin(op1_int)[2:])
                        return render_template('calculator.html', result=result, op1 = operand_1, op1_bin = op1_bin, operation = operation , options = 'Binary')
                    return render_template('calculator.html', result=result, op1 = operand_1, op2 = operand_2, operation = operation , options = 'Binary')
                except Exception as e:
                    print(e)
                    error = 'Invalid input, please fill out all fields correctly!'
                    return render_template('calculator.html', error=error)
            elif request.form['options'] == 'hexadecimal':
                try:
                    operand_1 = request.form.get('op1')
                    operand_2 = request.form.get('op2')
                    operation = request.form.get('operation')
                    if operation == 'addition':
                        operation = '+'
                        result = hex(int(operand_1, 16) + int(operand_2, 16))
                    elif operation == 'subtraction':
                        operation = '-'
                        result = hex(int(operand_1, 16) - int(operand_2, 16))
                    elif operation == 'multiplication':
                        operation = '*'
                        result = hex(int(operand_1, 16) * int(operand_2, 16))
                    elif operation == 'and':
                        operation = 'AND'
                        result = hex(int(operand_1, 16) & int(operand_2, 16))
                    elif operation == 'or':
                        operation = 'OR'
                        result = hex(int(operand_1, 16) | int(operand_2, 16))
                    elif operation == 'not':
                        operation = 'NOT'
                        op1_int = int(operand_1, 16)
                        op1_bin = bin(op1_int)
                        slice_bin = op1_bin[2:]
                        result = not_bin(slice_bin)
                        decimal = binaryToDecimal(int(result))
                        result = hex(decimal)
                        return render_template('calculator.html', result=result, op1 = operand_1, op1_bin = slice_bin, operation = operation , options = 'Hexadecimal')
                    return render_template('calculator.html', result=result, op1 = operand_1, op2 = operand_2, operation = operation , options = 'Hexadecimal')

                except Exception as e:
                    print(e)
                    error = 'Invalid input, please fill out all fields correctly!'
                    return render_template('calculator.html', error=error)
            elif request.form['options'] == 'octal':
                try:
                    operand_1 = request.form.get('op1')
                    operand_2 = request.form.get('op2')
                    operation = request.form.get('operation')
                    if operation == 'addition':
                        operation = '+'
                        result = oct(int(operand_1, 8) + int(operand_2, 8))
                    elif operation == 'subtraction':
                        operation = '-'
                        result = oct(int(operand_1, 8) - int(operand_2, 8))
                    elif operation == 'multiplication':
                        operation = '*'
                        result = oct(int(operand_1, 8) * int(operand_2, 8))
                    elif operation == 'and':
                        operation = 'AND'
                        result = oct(int(operand_1, 8) & int(operand_2, 8))
                    elif operation == 'or':
                        operation = 'OR'
                        result = oct(int(operand_1, 8) | int(operand_2, 8))
                    elif operation == 'not':
                        operation = 'NOT'
                        op1_int = int(operand_1, 8)
                        op1_bin = bin(op1_int)
                        slice_bin = op1_bin[2:]
                        result = not_bin(slice_bin)
                        decimal = binaryToDecimal(int(result))
                        result = oct(decimal)
                        return render_template('calculator.html', result=result, op1 = operand_1, op1_bin = slice_bin, operation = operation , options = 'Octal')
                    return render_template('calculator.html', result=result, op1 = operand_1, op2 = operand_2, operation = operation , options = 'Octal')


                except Exception as e:
                    print(e)
                    error = 'Invalid input, please fill out all fields correctly!'
                    return render_template('calculator.html', error=error)
                

        return render_template('calculator.html')
        
    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
