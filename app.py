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

@app.route('/consulta/2')
def consulta_2():
    num_consulta = 2
    result = consulta2()
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/3')
def consulta_3():
    num_consulta = 3
    result = consulta3('EXEMESTANO')
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/4')
def consulta_4():
    num_consulta = 4
    result = consulta4()
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/5')
def consulta_5():
    num_consulta = 5
    result = consulta5('FORMOTEROL')
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/6')
def consulta_6():
    num_consulta = 6
    result = consulta6()
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/7')
def consulta_7():
    num_consulta = 7
    result = consulta7()
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/8')
def consulta_8():
    num_consulta = 8
    result = consulta8()
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consulta/9')
def consulta_9():
    num_consulta = 9
    result = consulta9()
    df = pd.DataFrame([record.values() for record in result], columns=result[0].keys())
    tabla_html = df.to_html(classes='table table-bordered', index=False, escape=False)

    return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)

@app.route('/consultas', methods=['GET', 'POST'])
def consultas():
    if request.method == 'POST':
        operacion = request.form.get('operacion')
        datos = cargar_datos_desde_txt()

        if operacion == 'crear':
            nuevo_dato = request.form.get('nuevo_dato')
            datos.append(nuevo_dato)
            guardar_datos_en_txt(datos)
            flash('Dato creado exitosamente', 'success')
        elif operacion == 'leer':
            pass  # Puedes implementar la lectura de datos aquí
        elif operacion == 'actualizar':
            pass  # Puedes implementar la actualización de datos aquí
        elif operacion == 'eliminar':
            pass  # Puedes implementar la eliminación de datos aquí

    datos = cargar_datos_desde_txt()
    return render_template('consultas.html', datos=datos)


if __name__ == '__main__':
    # webbrowser.open('http://localhost:5000')
    app.run(debug=True)
