from neo4j import GraphDatabase
import pandas as pd

# Define a function to create nodes in Neo4j
def create_nodes_f1(tx, data):
    query = (
        f"CREATE (n:PharmaceuticalProductInfo {{"
        "NOMBRE_DEL_PRODUCTO_FARMACEUTICO: $nombre_producto, "
        "TIPO_DE_FARMACO: $tipo_farmaco, "
        "NOMBRE_DEL_LABORATORIO_OFERTANTE: $nombre_laboratorio, "
        "ESTADO: $estado, "
        # "APORTACION_DEL_BENEFICIARIO: $aportacion, "
        "PRINCIPIO_ACTIVO: $principio_activo, "
        "PRECIO_VENTA_CON_IVA_EUROS: $precio_euros, "
        # "NOMBRE_DE_AGRUPACION_HOMOGENEA: $nombre_agrupacion, "
        # "DIAGNOSTICO_HOSPITALARIO: $diagnostico_hospitalario, "
        "TRATAMIENTO_DE_LARGA_DURACION: $tratamiento_largo, "
        # "ESPECIAL_CONTROL_MEDICO: $control_medico, "
        "MEDICAMENTO_HUERFANO: $medicamento_huerfano"
        "})"
    )
    tx.run(query, **data)
    
def create_nodes_f2(tx, data):
    query = (
        f"CREATE (n:MedicationGroup {{"
        "GRUPO: $grupo, "
        "DESCRIPCION: $descripcion"
        "})"
    )

    tx.run(query, **data)
    
def create_nodes_f3(tx, data):
    query = (
        f"CREATE (n:MedicationCode {{"
        "NOMBRE: $nombre, "
        "CODIGO_DE_MEDICAMENTO: $codigo_de_medicamento"
        "})"
    )

    tx.run(query, **data)

def create_nodes_f4(tx, data):
    query = (
        f"CREATE (n:MedicationInfo {{"
        # "ATC: $atc, "
        "DESCRIPCION_PRINCIPIO_ACTIVO: $descripcion_principio_activo, "
        # "FORMA_FARMACEUTICA: $forma_farmaceutica, "
        "NOMBRE_GENERICO: $nombre_generico, "
        # "DETALLES_DEL_PRODUCTO: $detalles_del_producto, "
        "PRESENTACION: $presentacion, "
        # "TAMANO_DE_CAJA_O_PRESENTACION: $tamano_de_caja, "
        "FABRICANTE: $fabricante, "
        "PRECIO_MAXIMO_DE_VENTA: $precio_maximo_de_venta"
        "})"
    )
    
    tx.run(query, **data)
        
def create_nodes_f6(tx, data):
    query = (
        f"CREATE (n:Medication {{"
        # "MES: $mes, "
        # "FECHA: $fecha, "
        "SERVICIO: $servicio, "
        "DESCRIPCION: $descripcion, "
        # "TIPO: $tipo, "
        # "UNIDAD: $unidad, "
        "PIEZAS_SOLICITADAS: $piezas_solicitadas "
        # "PIEZAS_SURTIDAS: $piezas_surtidas, "
        # "PRECIO_UNITARIO: $precio_unitario, "
        # "MARCA: $marca"
        "})"
    )
    tx.run(query, **data)
    
# Connect to your Neo4j database
uri = "bolt://localhost:7687"  # Replace with your Neo4j server URI
username = "neo4j"  # Replace with your Neo4j username
password = "proyecto2"  # Replace with your Neo4j password

def file1(df1):
    # Create nodes in Neo4j
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            for _, row in df1.iterrows():
                data = {
                    "nombre_producto": row["NOMBRE DEL PRODUCTO FARMACEUTICO"],
                    "tipo_farmaco": row["TIPO DE FARMACO"],
                    "nombre_laboratorio": row["NOMBRE DEL LABORATORIO OFERTANTE"],
                    "estado": row["ESTADO"],
                    # "aportacion": row["APORTACION DEL BENEFICIARIO"],
                    "principio_activo": row["PRINCIPIO ACTIVO O ASOCIACION DE PRINCIPIOS ACTIVOS"],
                    "precio_euros": row["PRECIO VENTA CON IVA_EUROS"],
                    # "nombre_agrupacion": row["NOMBRE DE LA AGRUPACION HOMOGENEA DEL PRODUCTO SANITARIO"],
                    # "diagnostico_hospitalario": row["DIAGNOSTICO HOSPITALARIO"],
                    "tratamiento_largo": row["TRATAMIENTO DE LARGA DURACION"],
                    # "control_medico": row["ESPECIAL CONTROL MEDICO"],
                    "medicamento_huerfano": row["MEDICAMENTO HUERFANO"]
                }
                session.write_transaction(create_nodes_f1, data)
                
def file2(df2):
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            for _, row in df2.iterrows():
                data = {
                    "grupo": row["GRUPO"],
                    "descripcion": row["DESCRIPCION"]
                }
                session.write_transaction(create_nodes_f2, data)
                
def file3(df3):
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            for _, row in df3.iterrows():
                data = {
                    "nombre": row["NOMBRE"],
                    "codigo_de_medicamento": row["CODIGO DE MEDICAMENTO"]
                }
                session.write_transaction(create_nodes_f3, data)
def file4(df4):
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            for _, row in df4.iterrows():
                data = {
                    # "atc": row["ATC"],
                    "descripcion_principio_activo": row["DESCRIPCION PRINCIPIO ACTIVO"],
                    # "forma_farmaceutica": row["FORMA FARMACEUTICA"],
                    "nombre_generico": row["NOMBRE GENERICO"],
                    # "detalles_del_producto": row["DETALLES DEL PRODUCTO"],
                    "presentacion": row["PRESENTACION"],
                    # "tamano_de_caja": row["TAMANO DE CAJA O PRESENTACION"],
                    "fabricante": row["FABRICANTE"],
                    "precio_maximo_de_venta": row["PRECIO MAXIMO DE VENTA TRANSACCION FINAL COMERCIAL"]
                }
                session.write_transaction(create_nodes_f4, data)               
def file6(df6):
    # Create nodes in Neo4j
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            for _, row in df6.iterrows():
                data = {
                    # "mes": row["MES"],
                    # "fecha": row["FECHA"],
                    "servicio": row["SERVICIO"],
                    "descripcion": row["DESCRIPCION"],
                    # "tipo": row["TIPO"],
                    # "unidad": row["UNIDAD"],
                    "piezas_solicitadas": row["PIEZAS SOLICITADAS"],
                    # "piezas_surtidas": row["PIEZAS SURTIDAS"]#,
                    # "precio_unitario": row["PRECIO UNITARIO"],
                    # "marca": row["MARCA"]
                }
                session.write_transaction(create_nodes_f6, data)
def execute(path_list):
    print('Cargando datos a Neo4j')
    
    # Load the data from the CSV file
    df1 = pd.read_csv(path_list[0].replace('archivos_csv','archivos_norma_csv'))
    df2 = pd.read_csv(path_list[1].replace('archivos_csv','archivos_norma_csv'))
    df3 = pd.read_csv(path_list[2].replace('archivos_csv','archivos_norma_csv'))
    df4 = pd.read_csv(path_list[3].replace('archivos_csv','archivos_norma_csv'))
    df6 = pd.read_csv(path_list[4].replace('archivos_csv','archivos_norma_csv'))
    
    # 
    print('Primer Archivo')
    file1(df1)
    print('Segundo Archivo')
    file2(df2)
    print('Tercer Archivo')
    file3(df3)
    print('Cuarto Archivo')
    file4(df4)
    print('Sexto Archivo')
    file6(df6)
    
# path_list = ['static/archivos_csv\\1.1_Nombre_de_productos_genéricos_y_Farmaceutica.csv', 'static/archivos_csv\\2._Catálogo_de_Categorías_de_Medicamentos_CCSS.csv', 'static/archivos_csv\\3._muestra_Medicamentos_CCSS_clasificados.csv', 'static/archivos_csv\\4._Principios_Activos_y_Presentación.csv', 'static/archivos_csv\\6-Medicamentos_adquiridos_por_hospital.csv']
# execute(path_list)


#FALTA
def consulta1():
    result = []
    
    # Connect to the Neo4j database
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            # Cypher query
            query = """
                MATCH (m:Medication)
                MATCH (ppi:PharmaceuticalProductInfo)
                WHERE m.DESCRIPCION <> ppi.NOMBRE_DEL_PRODUCTO_FARMACEUTICO

                WITH m, ppi
                MATCH(mi:MedicationInfo)
                WHERE mi.DESCRIPCION_PRINCIPIO_ACTIVO = ppi.PRINCIPIO_ACTIVO

                RETURN ppi.PRINCIPIO_ACTIVO
            """
            result = session.read_transaction(lambda tx: list(tx.run(query)))
    
    return result

# # Print the result
# for record in result:
#     print("PRODUCTO FARMACEUTICO:", record["PRODUCTO_FARMACEUTICO"])
#     print("PRINCIPIO ACTIVO:", record["PRINCIPIO_ACTIVO"])
#     print("NOMBRE GENERIC0:", record["NOMBRE_GENERICO"])
#     print("FABRICANTE:", record["FABRICANTE"])
#     print("TIPO DE FARMACO:", record["TIPO_DE_FARMACO"])
#     print("MEDICAMENTO HUERFANO:", record["MEDICAMENTO_HUERFANO"])
#     print()

#LISTA
# Function to execute the Cypher query and return the result
def consulta2():
    result = []

    # Connect to the Neo4j database
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            query = """
            MATCH (p:PharmaceuticalProductInfo)
            WHERE NOT EXISTS {
                MATCH (m:MedicationCode{DESCRIPCION: p.NOMBRE_DEL_PRODUCTO_FARMACEUTICO})
                }
            RETURN DISTINCT p.NOMBRE_DEL_PRODUCTO_FARMACEUTICO, p.NOMBRE_DEL_LABORATORIO_OFERTANTE;
            """
            result = session.read_transaction(lambda tx: list(tx.run(query)))
    
    return result

#result = consulta2()
#for record in result:

#    print(record["p.NOMBRE_DEL_PRODUCTO_FARMACEUTICO"], " | ", record["p.NOMBRE_DEL_LABORATORIO_OFERTANTE"])

# =============================================================================
# def consulta3(input_value):
#     result = []
# 
#     # Connect to the Neo4j database
#     with GraphDatabase.driver(uri, auth=(username, password)) as driver:
#         with driver.session() as session:
#             query = """
#                 MATCH (m:MedicationInfo)
#                 WHERE m.DESCRIPCION_PRINCIPIO_ACTIVO = $input
#                 WITH m
#                 MATCH (n:MedicationInfo)
#                 WHERE m.NOMBRE_GENERICO = n.DESCRIPCION_PRINCIPIO_ACTIVO
#                 RETURN m.DESCRIPCION_PRINCIPIO_ACTIVO AS DESCRIPCION_PRINCIPIO_ACTIVO, n.NOMBRE_GENERICO AS NOMBRE_GENERICO;
#             """
#             result = session.read_transaction(lambda tx: list(tx.run(query, input=input_value)))
#     
#     return result
# 
# # result = consulta3('EXEMESTANO')
# # for record in result:
# #     print("DESCRIPCION PRINCIPIO ACTIVO:", record["DESCRIPCION_PRINCIPIO_ACTIVO"])
# #     print("NOMBRE GENERIC0:", record["NOMBRE_GENERICO"])
# =============================================================================


#LISTA
#Se le agrego 2 tipos de posibles inputs controlados por la bandera flagConsulta3
#La idea es que si es 0 el input es un principio activo y si es 1 es un nombre genérico
def consulta3(input_value, flagConsulta3):
    result = []
    queryPrinc_activo = '''
        MATCH (m:MedicationInfo)
        WHERE m.DESCRIPCION_PRINCIPIO_ACTIVO = $input
        WITH m
        MATCH (n:MedicationInfo)
        WHERE m.NOMBRE_GENERICO = n.DESCRIPCION_PRINCIPIO_ACTIVO
        RETURN m.DESCRIPCION_PRINCIPIO_ACTIVO AS DESCRIPCION_PRINCIPIO_ACTIVO, n.NOMBRE_GENERICO AS NOMBRE_GENERICO
    '''
    queryGenerico = '''
        MATCH (o:MedicationInfo)
        WHERE o.NOMBRE_GENERICO = $input
        WITH o
        MATCH (m:MedicationInfo)
        WHERE m.DESCRIPCION_PRINCIPIO_ACTIVO = o.DESCRIPCION_PRINCIPIO_ACTIVO
        WITH m
        MATCH (n:MedicationInfo)
        WHERE m.NOMBRE_GENERICO = n.DESCRIPCION_PRINCIPIO_ACTIVO
        RETURN m.DESCRIPCION_PRINCIPIO_ACTIVO AS DESCRIPCION_PRINCIPIO_ACTIVO, n.NOMBRE_GENERICO AS NOMBRE_GENERICO
    '''
    # Connect to the Neo4j database
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            if flagConsulta3 == 0:
                query = queryPrinc_activo
            else:
                query = queryGenerico
            result = session.read_transaction(lambda tx: list(tx.run(query, input=input_value)))
    
    return result


# result = consulta3('IBUPROFENO', 0)
# for record in result:
#     print("DESCRIPCION PRINCIPIO ACTIVO:", record["DESCRIPCION_PRINCIPIO_ACTIVO"])
#     print("NOMBRE GENERIC0:", record["NOMBRE_GENERICO"])


# result = consulta3('BOLTALKEY', 1)
# for record in result:
#     print("DESCRIPCION PRINCIPIO ACTIVO:", record["DESCRIPCION_PRINCIPIO_ACTIVO"])
#     print("NOMBRE GENERIC0:", record["NOMBRE_GENERICO"])


# =============================================================================
# def consulta5(input_value):
#     result = []
# 
#     # Connect to the Neo4j database
#     with GraphDatabase.driver(uri, auth=(username, password)) as driver:
#         with driver.session() as session:
#             query = """
#                 MATCH (ppi:PharmaceuticalProductInfo)
#                 WHERE ppi.PRINCIPIO_ACTIVO = $input
# 
#                 MATCH (mi:MedicationInfo)
#                 WHERE mi.DESCRIPCION_PRINCIPIO_ACTIVO = ppi.PRINCIPIO_ACTIVO
# 
#                 MATCH (mc:MedicationCode)
#                 WHERE mc.NOMBRE = ppi.PRINCIPIO_ACTIVO
# 
#                 MATCH (mg:MedicationGroup)
#                 WHERE mg.GRUPO = toInteger(mc.CODIGO_DE_MEDICAMENTO)
# 
#                 RETURN ppi.PRINCIPIO_ACTIVO AS PRINCIPIO_ACTIVO,
#                         ppi.NOMBRE_DEL_LABORATORIO_OFERTANTE AS OFERTANTE,
#                         mi.FABRICANTE AS FABRICANTE,
#                         mi.PRESENTACION AS PRESENTACION,
#                         mg.DESCRIPCION AS DESCRIPCION;
#             """
#             result = session.read_transaction(lambda tx: list(tx.run(query, input=input_value)))
#     
#     return result
# 
# # result = consulta5('FORMOTEROL')
# # for record in result:
# #     print("DESCRIPCION PRINCIPIO ACTIVO:", record["DESCRIPCION_PRINCIPIO_ACTIVO"])
# #     print("LABORATORIO OFERTANTE:", record["NOMBRE_DEL_LABORATORIO_OFERTANTE"])
# #     print("FABRICANTE:", record["FABRICANTE"])
# #     print("PRESENTACION:", record["PRESENTACION"])
# #     print("DESCRIPCION:", record["DESCRIPCION"])
# =============================================================================

#LISTA
#Lo que se le cambió fue la forma en la que se relaciona el archivo de los meds de la CCSS
#que tienen el código, con los grupos del catálogo 
def consulta5(input_value):
    result = []

    # Connect to the Neo4j database
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            query = """
                MATCH (ppi:PharmaceuticalProductInfo)
                WHERE ppi.PRINCIPIO_ACTIVO = $input
                MATCH (mi:MedicationInfo)
                WHERE mi.DESCRIPCION_PRINCIPIO_ACTIVO = ppi.PRINCIPIO_ACTIVO
                MATCH (mc:MedicationCode)
                WHERE mc.NOMBRE = ppi.PRINCIPIO_ACTIVO
                MATCH (mg:MedicationGroup)
                WHERE mg.GRUPO = toInteger(SUBSTRING(toString(mc.CODIGO_DE_MEDICAMENTO), 0, 2))
                RETURN ppi.PRINCIPIO_ACTIVO AS PRINCIPIO_ACTIVO, 
                        mi.FABRICANTE AS FABRICANTE,
                        ppi.NOMBRE_DEL_LABORATORIO_OFERTANTE AS OFERTANTE,
                        mi.PRESENTACION AS PRESENTACION,
                        mg.DESCRIPCION AS CATEGORIA;
            """
            result = session.read_transaction(lambda tx: list(tx.run(query, input=input_value)))
    
    return result

# result = consulta5('ITRACONAZOL')
# for record in result:
#     print("PRINCIPIO ACTIVO:", record["PRINCIPIO_ACTIVO"])
#     print("LABORATORIO OFERTANTE:", record["OFERTANTE"])
#     print("FABRICANTE:", record["FABRICANTE"])
#     print("PRESENTACION:", record["PRESENTACION"])
#     print("CATEGORIA:", record["CATEGORIA"])

# =============================================================================
# def consulta6():
#     result = []
#     # Connect to the Neo4j database
#     with GraphDatabase.driver(uri, auth=(username, password)) as driver:
#         with driver.session() as session:
#             query = """
#                 MATCH (p:PharmaceuticalProductInfo)
#                 WHERE p.ESTADO = 'SUSPENSION TEMPORAL GENERAL'
# 
#                 MATCH (m:Medication)
#                 WHERE m.DESCRIPCION = p.PRINCIPIO_ACTIVO
# 
#                 RETURN DISTINCT p.PRINCIPIO_ACTIVO AS PRINCIPIO_ACTIVO, COUNT(*) AS occurrence_count
#                 ORDER BY occurrence_count DESC
#                 LIMIT 10
#             """
#             result = session.read_transaction(lambda tx: list(tx.run(query)))
#     
#     return result
# =============================================================================

#LISTA
#Cambiamos la relación del archivo6 del hospital con el 3 muestras de meds de la CCSS
def consulta6():
    result = []
    # Connect to the Neo4j database
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            query = """
                MATCH(n:MedicationCode)
                WHERE n.ESTADO = 'SUSPENSION TEMPORAL GENERAL'
                MATCH (m:PharmaceuticalProductInfo)
                WHERE m.PRINCIPIO_ACTIVO = n.NOMBRE 
                RETURN DISTINCT m.PRINCIPIO_ACTIVO AS PRINCIPIO_ACTIVO, COUNT(*) AS occurrence_count
                ORDER BY occurrence_count DESC
                LIMIT 10
            """
            result = session.read_transaction(lambda tx: list(tx.run(query)))
    
    return result

# result = consulta6()
# for record in result:
#     print("PRINCIPIO ACTIVO:", record["PRINCIPIO_ACTIVO"])
#     print("CANTIDAD:", record["occurrence_count"])

# =============================================================================
# def consulta7():
#     result = []
#     # Connect to the Neo4j database
#     with GraphDatabase.driver(uri, auth=(username, password)) as driver:
#         with driver.session() as session:
#             query = """
#                 MATCH (p:PharmaceuticalProductInfo)
#                 WHERE p.TRATAMIENTO_DE_LARGA_DURACION = 'SI'
#                 WITH p
#                 MATCH (p1:MedicationCode)
#                 WHERE p.PRINCIPIO_ACTIVO = p1.NOMBRE
#                 WITH p1
#                 MATCH (p2:MedicationInfo)
#                 WHERE p2.DESCRIPCION_PRINCIPIO_ACTIVO = p1.NOMBRE
#                 RETURN p1.NOMBRE AS NOMBRE, p2.NOMBRE_GENERICO AS NOMBRE_GENERICO;
#             """
#             result = session.read_transaction(lambda tx: list(tx.run(query)))
#     
#     return result
# =============================================================================

#LISTA
#Se le agrega una columna en la salida, padecimientos que está basado en el catálogo A2
def consulta7():
    result = []
    # Connect to the Neo4j database
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            query = """
                MATCH (p:PharmaceuticalProductInfo)
                WHERE p.TRATAMIENTO_DE_LARGA_DURACION = 'SI'
                MATCH (mc:MedicationCode)
                WHERE p.PRINCIPIO_ACTIVO = mc.NOMBRE
                MATCH (mg:MedicationGroup)
                WHERE mg.GRUPO = toInteger(SUBSTRING(toString(mc.CODIGO_DE_MEDICAMENTO), 0, 2))
                MATCH (mi:MedicationInfo)
                WHERE mi.DESCRIPCION_PRINCIPIO_ACTIVO = mc.NOMBRE
                RETURN mc.NOMBRE AS NOMBRE, mi.NOMBRE_GENERICO AS NOMBRE_GENERICO, mg.DESCRIPCION AS PADECIMIENTO;
            """
            result = session.read_transaction(lambda tx: list(tx.run(query)))
    
    return result

# result = consulta7()
# for record in result:
#     print("NOMBRE:", record["NOMBRE"])
#     print("NOMBRE GENERICO:", record["NOMBRE_GENERICO"])
#     print("PADECIMIENTO:", record["PADECIMIENTO"])


#FALTA
def consulta8():
    result = []

    # Connect to the Neo4j database
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            query = """
                MATCH (p:PharmaceuticalProductInfo)
                WHERE p.TRATAMIENTO_DE_LARGA_DURACION = 'SI'
                WITH p
                MATCH (p1:MedicationCode)
                WHERE p.PRINCIPIO_ACTIVO = p1.NOMBRE
                WITH p1
                MATCH (p2:MedicationInfo)
                WHERE p2.DESCRIPCION_PRINCIPIO_ACTIVO = p1.NOMBRE
                RETURN p1.NOMBRE AS NOMBRE, p2.NOMBRE_GENERICO AS NOMBRE_GENERICO;
            """
            result = session.read_transaction(lambda tx: list(tx.run(query)))
    
    return result


#FALTA
def consulta9():
    result = []

    # Connect to the Neo4j database
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            query = """
                MATCH (mi:MedicationInfo)
                WHERE NOT EXISTS((mi)-[:RELATIONSHIP_NAME]->(:MedicationCode {NOMBRE: mi.DESCRIPCION_PRINCIPIO_ACTIVO}))
                RETURN mi.DESCRIPCION_PRINCIPIO_ACTIVO AS DESCRIPCION_PRINCIPIO_ACTIVO, mi.FABRICANTE AS FABRICANTE;
            """
            result = session.read_transaction(lambda tx: list(tx.run(query)))
    
    return result