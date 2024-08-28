from flask import Flask, render_template, request
from analizador_lexico import prueba as analizar_lexico


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    lexico_result = ""
    

    if request.method == 'POST':
        codigo_fuente = request.form['ingreso']
        
        if 'lexico_button' in request.form:
            resultado_lexico = analizar_lexico(codigo_fuente)
            lexico_result = '\n'.join(resultado_lexico)
        

    return render_template('index.html', lexico_result=lexico_result)

if __name__ == '__main__':
    app.run(debug=True)
