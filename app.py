from flask import Flask, render_template, request
import time
import array as arr

app = Flask(__name__)

validaciones = {
    "INPUT_VACIO" : "Por favor, ingrese un número.",
    "INPUT_NUMERICO" : "Por favor, ingrese un valor numérico.",
    "INPUT_RANGO_MINIMO" : "Por favor, ingrese un número mayor o igual a 2"
}
       
@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")

def limpiarCampos():
    return render_template("index.html", reiniciarVerificador = True)


@app.route('/', methods=["POST"])
def mostrarNombre():
    numero = request.form["numero"]
    if (numero == ""):     
        return render_template("index.html", msj = validaciones["INPUT_VACIO"], reiniciarVerificador = False)
    elif(numero.isdigit() is False):    
         return render_template("index.html", msj = validaciones["INPUT_NUMERICO"], reiniciarVerificador = False)         
    elif (int(numero) < 2):
         return render_template("index.html", msj = validaciones["INPUT_RANGO_MINIMO"], reiniciarVerificador = False)
    else:
        inicio = time.time()       
        divisores = []
        esPrimo = True
        for num in range(2, int(numero)):
            if int(numero) % num == 0:
                divisores.append(num)            
                esPrimo = False         
        fin = time.time()  
        tiempoEjecucion = fin - inicio    
        return render_template("index.html", numero = numero, esPrimo = esPrimo, tiempoEjecucion = tiempoEjecucion, divisores = divisores, reiniciarVerificador = False)
    


def validarEntrada(numero):
    if (numero == ""):
        print("entra")
        msj = "Por favor, ingrese un número."
        return render_template("index.html", msj = msj)
    else:
        print("#######")
        return True


if __name__ == "__main__":
    app.run(debug=True, port=5000)