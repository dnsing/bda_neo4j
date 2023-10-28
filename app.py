import webbrowser
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import csv
import os
from normaText import normalized_text
from node_creation import *


app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Cambia esto por una clave secreta segura

UPLOAD_FOLDER = 'static/archivos_csv'  # Carpeta donde se guardarán los archivos CSV cargados
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    carga_exitosa = session.get('carga_exitosa', False)
    return render_template('index.html', carga_exitosa=carga_exitosa)

@app.route('/cargar_csv', methods=['POST'])
def cargar_csv():
    if request.method == 'POST':
        flash('Cargando archivos, por favor espere...', 'info')
        
        # Obtener archivos CSV desde la solicitud
        archivos = request.files.getlist('archivos_csv')
        rutas_archivos = [] 

        for archivo in archivos:
            if archivo.filename == '':
                flash('Selecciona al menos un archivo CSV para cargar', 'error')
                return redirect(request.url)
            
            if archivo.filename.endswith('.csv'):
                ruta = os.path.join(app.config['UPLOAD_FOLDER'], archivo.filename)
                archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], archivo.filename))
                rutas_archivos.append(ruta)
            else:
                flash('Solo se permiten archivos CSV', 'error')

        flash('Archivos CSV cargados exitosamente', 'success')
        
        # Almacena una variable en sesión para indicar que la carga fue exitosa
        session['carga_exitosa'] = True
        
        # normalized_text(rutas_archivos)
        # execute(rutas_archivos)
        
        return redirect(url_for('index'))

txt_file_path = 'static/resultados.txt'  # Ruta del archivo de resultados
# Función para cargar datos desde el archivo .txt
def cargar_datos_desde_txt():
    datos = []
    with open(txt_file_path, 'r') as archivo_txt:
        lineas = archivo_txt.readlines()
        for linea in lineas:
            datos.append(linea.strip())
    return datos

# Función para guardar datos en el archivo .txt
def guardar_datos_en_txt(datos):
    with open(txt_file_path, 'w') as archivo_txt:
        for dato in datos:
            archivo_txt.write(f'{dato}\n')

# @app.route('/consultas', methods=['GET', 'POST'])
# def consultas():
#     if request.method == 'POST':
#         if request.form['consulta'] == '3':
#             parametro1 = request.form['parametro1']
#             parametro2 = request.form['parametro2']
            
#             # Realiza la "Consulta 3" con los parámetros recibidos
#             # Puedes hacer la lógica de la consulta aquí
            
#             # Luego, muestra los resultados en una plantilla o de la manera que desees
            
#     return render_template('consultas.html')


@app.route('/consulta/1', methods=['POST'])
def consulta_1():
    num_consulta = 1
    result = consulta1()
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/2', methods=['POST'])
def consulta_2():
    num_consulta = 2
    result = consulta2()
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/3', methods=['POST'])
def consulta_3():
    if request.method == 'POST':
        producto_principio = request.form['parametro1']
        isMed = (1 if request.form['parametro2'] == 'principio' else 0)
    num_consulta = 3
    result = consulta3(producto_principio, isMed)
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/4', methods=['POST'])
def consulta_4():
    num_consulta = 4
    result = consulta4()
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/5', methods=['POST'])
def consulta_5():
    if request.method == 'POST':
        principioActivo = request.form['parametro3']
    num_consulta = 5
    result = consulta5(principioActivo)
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/6', methods=['POST'])
def consulta_6():
    num_consulta = 6
    result = consulta6()
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/7', methods=['POST'])
def consulta_7():
    num_consulta = 7
    result = consulta7()
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/8', methods=['POST'])
def consulta_8():
    num_consulta = 8
    result = consulta8()
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/9', methods=['POST'])
def consulta_9():
    if request.method == 'POST':
        fabricante = request.form['parametro4']
    num_consulta = 9
    result = consulta9(fabricante)
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/crud_operations', methods=['GET', 'POST'])
def crud_operations():
    return render_template('crud_operations.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    operation = request.form.get('operation')  # Leer el valor del campo oculto "operation"

    if operation == 'create':
        # Leer los campos del formulario
        campo1 = request.form.get('campo1')
        campo2 = request.form.get('campo2')
        campo3 = request.form.get('campo3')
        campo4 = request.form.get('campo4')

        # Si se selecciona "Archivo 1," se leen los campos adicionales
        if request.form.get('fileSelector') == 'file1.csv':
            campo5 = request.form.get('campo5')
            campo6 = request.form.get('campo6')
            campo7 = request.form.get('campo7')
            campo8 = request.form.get('campo8')
        else:
            # Establece campos adicionales en None o valores predeterminados
            campo5 = None
            campo6 = None
            campo7 = None
            campo8 = None

        # Realiza las operaciones CRUD con los datos recibidos

        # Puedes imprimir o procesar los datos aquí
        print(f"Campo 1: {campo1}")
        print(f"Campo 2: {campo2}")
        print(f"Campo 3: {campo3}")
        print(f"Campo 4: {campo4}")
        if campo5 is not None:
            print(f"Campo 5: {campo5}")
            print(f"Campo 6: {campo6}")
            print(f"Campo 7: {campo7}")
            print(f"Campo 8: {campo8}")

        return "Operación CRUD completada"
    
    elif operation == 'read':
        # Realiza la operación de Leer con el campoLeer
        campoLeer = request.form.get('campoLeer')
        result = read_file1(campoLeer)
        print(result)
        print(campoLeer)
        
        return "Operación CRUD completadaREAD"

if __name__ == '__main__':
    # webbrowser.open('http://localhost:5000')
    app.run(debug=True)

