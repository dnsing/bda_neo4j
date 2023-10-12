import webbrowser

from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Cambia esto por una clave secreta segura

UPLOAD_FOLDER = 'static/archivos_csv'  # Carpeta donde se guardarán los archivos CSV cargados
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cargar_csv', methods=['POST'])
def cargar_csv():
    if request.method == 'POST':
        # Obtener archivos CSV desde la solicitud
        archivos = request.files.getlist('archivos_csv')

        for archivo in archivos:
            if archivo.filename == '':
                flash('Selecciona al menos un archivo CSV para cargar', 'error')
                return redirect(request.url)
            
            if archivo.filename.endswith('.csv'):
                archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], archivo.filename))
            else:
                flash('Solo se permiten archivos CSV', 'error')

        flash('Archivos CSV cargados exitosamente', 'success')
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
    webbrowser.open('http://localhost:5000')
    app.run(debug=True)
