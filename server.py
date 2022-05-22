from flask import Flask, render_template, request, url_for, flash, redirect
import cmath 

app = Flask(__name__)
#python -m flask run
#set FLASK_APP=server.py

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/mayor', methods=('GET', 'POST')) #Formulario para ingresar los 10 numeros
def numMayor():
    return render_template('numMayor.html')

@app.route('/mayor/resultado', methods=('GET', 'POST')) #Obtiene los 10 numeros ingresados y retorna el numero mayor
def resultado():
    num1 = request.form['num1']
    num2 = request.form['num2']
    num3 = request.form['num3']
    num4 = request.form['num4']
    num5 = request.form['num5']
    num6 = request.form['num6']
    num7 = request.form['num7']
    num8 = request.form['num8']
    num9 = request.form['num9']
    num10 = request.form['num10']
    numeros = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
    mayor = 0
    for i in range(10):
        if (int(numeros[i]) > int(mayor)):
            mayor = numeros[i]
    return "El numero mayor es " + mayor + "<a href='/'> <button>Regresar al Inicio</button>"
    
@app.route('/palabra', methods=('GET', 'POST')) #Se ingresa la frase y la palabra a buscar
def cuentaPalabra():
    return render_template('cuentaPalabra.html')

@app.route('/palabra/respuesta', methods=('GET', 'POST')) #Retorna el numero de veces que se repite la palabra
def palabrasContadas():
    texto = request.form['texto']
    palabra = request.form['word']
    respuesta = texto.count(palabra)
    return " El numero de veces que se repite la palabra es: " + str(respuesta) + "<a href='/'> <button>Regresar al Inicio</button>"

@app.route('/cuadratica', methods=('GET', 'POST')) #Se ingresan los 3 numeros para realizar la ecuacion
def ecuacionC():
     return render_template('cuadratica.html')
    
@app.route('/cuadratica/producto', methods=('GET', 'POST')) #Ejecuta la formula y retorna 2 raices
def ecuacionCuadratica():
    a = float(request.form['valor1'])
    b = float(request.form['valor2'])
    c = float(request.form['valor3'])
    dis = (b**2) - (4 * a*c)
    respuesta1 = (-b-cmath.sqrt(dis))/(2 * a) 
    respuesta2 = (-b + cmath.sqrt(dis))/(2 * a) 
    return "Las raices son: " + str(respuesta1) + " y " + str(respuesta2) + "<a href='/'> <button>Regresar al Inicio</button>"

 


