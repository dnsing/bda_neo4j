# importing libraries
import pandas as pd
import unicodedata
import csv

files_path = ['1.1_Nombre_de_productos_genéricos_y_Farmaceutica.csv','2._Catálogo_de_Categorías_de_Medicamentos_CCSS.csv','3._muestra_Medicamentos_CCSS_clasificados.csv','4._Principios_Activos_y_Presentación.csv','6-Medicamentos_adquiridos_por_hospital.csv']
compress_columns = [['NOMBRE DEL PRODUCTO FARMACEUTICO','PRINCIPIO ACTIVO O ASOCIACION DE PRINCIPIOS ACTIVOS','NOMBRE DE LA AGRUPACION HOMOGENEA DEL PRODUCTO SANITARIO'],[],[],['DESCRIPCION PRINCIPIO ACTIVO'],['DESCRIPCION']]

def eliminar_tildes(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join([caracter for caracter in texto_normalizado if not unicodedata.combining(caracter)])

    # Reemplazar la palabra "ácido" por una cadena vacía (eliminarla)
    if 'ACIDO' in texto_sin_tildes:
        texto_sin_tildes = texto_sin_tildes.replace("ACIDO", "").replace("Acido", "")
    elif ',' in texto_sin_tildes:
        texto_sin_tildes = texto_sin_tildes.replace(",", "")
        
    return texto_sin_tildes

# Para limitar el string de la columna a una sola palabra
def compress(df, column_name_list=[]):
    for column in column_name_list:
        df[column] = df[column].str.split().str[0]
    return df

for i, file in enumerate(files_path):

    # Nombre del archivo de entrada y salida
    nombre_archivo_entrada = 'Fuentes para proyecto 2\\'+file
    nombre_archivo_salida = 'Fuentes para proyecto 2 normalizado\\'+file

    # Abrir el archivo de entrada y crear un archivo de salida
    with open(nombre_archivo_entrada, 'r', newline='', encoding='utf-8') as archivo_entrada, open(nombre_archivo_salida, 'w', newline='', encoding='utf-8') as archivo_salida:
        lector_csv = csv.reader(archivo_entrada)
        escritor_csv = csv.writer(archivo_salida)

        for fila in lector_csv:
            fila_sin_tildes_mayusculas = [eliminar_tildes(columna.upper()) for columna in fila]
            escritor_csv.writerow(fila_sin_tildes_mayusculas)

    print(f'Las tildes han sido eliminadas y el contenido se ha guardado en {nombre_archivo_salida} en mayúsculas.')

    df_norma = pd.read_csv(nombre_archivo_salida)
    df_norma = compress(df_norma, compress_columns[i])
    if i == 0:
        df_norma['TIPO DE FARMACO'] = df_norma['TIPO DE FARMACO'].apply(lambda x: 'ORIGINAL' if 'ETICA' in x else 'GENERICO')
        df_norma = df_norma[['NOMBRE DEL PRODUCTO FARMACEUTICO','NOMBRE DEL LABORATORIO OFERTANTE']]
    # print(df_norma)
    elif i == 4:
        df_norma['DESCRIPCION'] = df_norma['DESCRIPCION'].map(lambda x: x.strip(','))
        df_norma = df_norma[['DESCRIPCION']]

    df_norma = df_norma.drop_duplicates()
    df_norma.to_csv(nombre_archivo_salida, index=False)

