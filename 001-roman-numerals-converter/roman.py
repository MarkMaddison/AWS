from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def convert_to_Roman(dec): 
    
    
    
    
    numeric = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    symbolic = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    while dec: 
        div = dec // numeric[i] 
        dec %= numeric[i] 
  
        while div: 
            print(symbolic[i], end = "") 
            div -= 1
        i -= 1
  
dec = int(input("Enter a decimal number between 1 - 3999 : "))
if dec > 3999:
    print("Please try again. Number should between 1 - 3999")
else:
    print("Decimal ", dec,"'s Roman numeral is:", end = " ") 
    convert_to_Roman(dec)

if __name__=='__main__':
    app.run('localhost', port=5000, debug=True)
    #app.run(debug=True)
    #app.run('0.0.0.0', port=80)