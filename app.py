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
        
        normalized_text(rutas_archivos)
        execute(rutas_archivos)
        
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
        if request.form['consulta'] == '3':
            parametro1 = request.form['parametro1']
            parametro2 = request.form['parametro2']
            
            # Realiza la "Consulta 3" con los parámetros recibidos
            # Puedes hacer la lógica de la consulta aquí
            
            # Luego, muestra los resultados en una plantilla o de la manera que desees
            
    return render_template('consultas.html')


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

@app.route('/index_exe', methods=['GET', 'POST'])
def index_exe():
    result = index
    print('Ejecutando indices')
    return '', 204 

@app.route('/process_form', methods=['POST'])
def process_form():
    operation = request.form.get('operation')
    file = request.form.get('fileSelector') 

    if operation == 'create':
        if file == 'file1.csv':
            # nombre_producto = request.form.get('campo1')
            # tipo_farmaco = request.form.get('campo2')
            # nombre_laboratorio = request.form.get('campo3')
            # estado = request.form.get('campo4')
            # principio_activo = request.form.get('campo5')
            # precio_euros = request.form.get('campo6')
            # tratamiento_largo = request.form.get('campo7')
            # medicamento_huerfano = request.form.get('campo8')
            input_values = [
                {
                    "nombre_producto": request.form.get('campo1'),
                    "tipo_farmaco": request.form.get('campo2'),
                    "nombre_laboratorio": request.form.get('campo3'),
                    "estado": request.form.get('campo4'),
                    "principio_activo": request.form.get('campo5'),
                    "precio_euros": request.form.get('campo6'),
                    "tratamiento_largo": request.form.get('campo7'),
                    "medicamento_huerfano": request.form.get('campo8')
                }
            ]
            result = create_file1(input_values)
            print(result)
            
        
        elif file == 'file2.csv':        
            # grupo = = request.form.get('campo1')
            # descripcion = request.form.get('campo2')
            input_values = [
                {
                    "grupo": request.form.get('campo1'),
                    "descripcion": request.form.get('campo2')
                }
            ]
            result = create_file2(input_values)
            print(result)
            
        elif file == 'file3.csv':        
            # nombre = = request.form.get('campo1')
            # codigo_de_medicamento = request.form.get('campo2')
            input_values = [
                {
                    "nombre": request.form.get('campo1'),
                    "codigo_de_medicamento": request.form.get('campo2')
                }
            ]
            result = create_file3(input_values)
            print(result)
            
        elif file == 'file4.csv':        
            # descripcion_principio_activo = request.form.get('campo1')
            # nombre_generico = request.form.get('campo2')
            # presentacion = request.form.get('campo3')
            # fabricante = request.form.get('campo4')
            # precio_maximo_de_venta = request.form.get('campo5')
            input_values = [
                {
                    "descripcion_principio_activo": request.form.get('campo1'),
                    "nombre_generico": request.form.get('campo2'),
                    "presentacion": request.form.get('campo3'),
                    "fabricante": request.form.get('campo4'),
                    "precio_maximo_de_venta": request.form.get('campo5')
                }
            ]
            result = create_file4(input_values)
            print(result)
        
        elif file == 'file5.csv':        
            # servicio = request.form.get('campo1')
            # descripcion = request.form.get('campo2')
            # piezas_solicitadas = request.form.get('campo3')
            input_values = [
                {
                    "servicio": request.form.get('campo1'),
                    "descripcion": request.form.get('campo2'),
                    "piezas_solicitadas": request.form.get('campo3')
                }
            ]
            result = create_file5(input_values)
            print(result)
            
        else:
            print('Algo salió mal')
    
        return "Operación CRUD completada"
    
    elif operation == 'update':
        if file == 'file1.csv':
            input_values = [
                {
                    "nombre_producto": request.form.get('campo1'),
                    "nuevo_tipo_farmaco": request.form.get('campo2'),
                    "nuevo_nombre_laboratorio": request.form.get('campo3'),
                    "nuevo_estado": request.form.get('campo4'),
                    "nuevo_principio_activo": request.form.get('campo5'),
                    "nuevo_precio_euros": request.form.get('campo6'),
                    "nuevo_tratamiento_largo": request.form.get('campo7'),
                    "nuevo_medicamento_huerfano": request.form.get('campo8')                
                }
            ]
            result = update_file1(input_values)
            print(result)
            
        elif file == 'file2.csv':
            input_values = [
                {
                    "grupo": request.form.get('campo1'),
                    "nueva_descripcion": request.form.get('campo2')
                }
            ]
            result = update_file2(input_values)
            print(result)
            
        elif file == 'file3.csv':
            input_values = [
                {
                    "nombre": request.form.get('campo1'),
                    "nuevo_codigo_de_medicamento": request.form.get('campo2')
                }
            ]
            result = update_file3(input_values)
            print(result)
            
        elif file == 'file4.csv':
            input_values = [
                {
                    "descripcion_principio_activo": request.form.get('campo1'),
                    "nuevo_nombre_generico": request.form.get('campo2'),
                    "nueva_presentacion": request.form.get('campo3'),
                    "nuevo_fabricante": request.form.get('campo4'),
                    "nuevo_precio_maximo_de_venta": request.form.get('campo5')
                }
            ]
            result = update_file4(input_values)
            print(result)
            
        elif file == 'file5.csv':
            input_values = [
                {
                    "descripcion": request.form.get('campo1'),
                    "nuevo_servicio": request.form.get('campo2'),
                    "nuevas_piezas_solicitadas": request.form.get('campo3')
                }
            ]
            result = update_file5(input_values)
            print(result)   
        else:
            print('Algo salió mal')
            
        return 'UPDATED'
         
            
    elif operation == 'read':
        if file == 'file1.csv':
            num_consulta = 1
            campoLeer = request.form.get('campoLeer')
            result = read_file1(campoLeer)      
        elif file == 'file2.csv':
            num_consulta = 2
            campoLeer = request.form.get('campoLeer')
            result = read_file2(int(campoLeer))         
        elif file == 'file3.csv':
            num_consulta = 3
            campoLeer = request.form.get('campoLeer')
            result = read_file3(campoLeer)
        elif file == 'file4.csv':
            num_consulta = 4
            campoLeer = request.form.get('campoLeer')
            result = read_file4(campoLeer)
        elif file == 'file5.csv':
            num_consulta = 5
            campoLeer = request.form.get('campoLeer')
            result = read_file6(campoLeer)
        else:
            return 'Algo salió mal'
        

        tabla_html = result.to_html(classes='table table-bordered', index=False, escape=False)
            
        return render_template('resultado_consulta.html', consulta=num_consulta, tabla_html=tabla_html)
    
    elif operation == "delete":
        if file == 'file1.csv':
            campoDelete = request.form.get('campoDelete')
            result = delete_file1(campoDelete)
        elif file == 'file2.csv':
            campoDelete = request.form.get('campoDelete')
            result = delete_file2(campoDelete)
        elif file == 'file3.csv':
            campoDelete = request.form.get('campoDelete')
            result = delete_file3(campoDelete)
        elif file == 'file4.csv':
            campoDelete = request.form.get('campoDelete')
            result = delete_file4(campoDelete)
        elif file == 'file5.csv':
            campoDelete = request.form.get('campoDelete')
            result = delete_file5(campoDelete)
        else:
            print('Algo salió mal')
        
        return 'DELETED'
    
if __name__ == '__main__':
    # webbrowser.open('http://localhost:5000')
    app.run(debug=True)

