from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')                                             
def anually() -> 'html':
    return render_template('annually.html')
                                
@app.route('/monthly')                    
def monthly() -> 'html':
    return render_template('monthly.html')      
    
if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

