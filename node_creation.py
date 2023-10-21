from neo4j import GraphDatabase
import pandas as pd

# Define a function to create nodes in Neo4j
def create_nodes_f1(tx, data):
    query = (
        f"CREATE (n:PharmaceuticalProductInfo {{"
        "NOMBRE_DEL_PRODUCTO_FARMACEUTICO: $nombre_producto, "
        "TIPO_DE_FARMACO: $tipo_farmaco, "
        "NOMBRE_DEL_LABORATORIO_OFERTANTE: $nombre_laboratorio, "
        # "ESTADO: $estado, "
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
        "FABRICANTE: $fabricante "
        # "PRECIO_MAXIMO_DE_VENTA: $precio_maximo_de_venta"
        "})"
    )

    tx.run(query, **data)
        
def create_nodes_f6(tx, data):
    query = (
        f"CREATE (n:Medication {{"
        # "MES: $mes, "
        # "FECHA: $fecha, "
        # "SERVICIO: $servicio, "
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

# Load the data from the CSV file
df1 = pd.read_csv("Fuentes para proyecto 2 normalizado\\1.1_Nombre_de_productos_genéricos_y_Farmaceutica.csv")
df2 = pd.read_csv("Fuentes para proyecto 2 normalizado\\2._Catálogo_de_Categorías_de_Medicamentos_CCSS.csv")
df3 = pd.read_csv("Fuentes para proyecto 2 normalizado\\3._muestra_Medicamentos_CCSS_clasificados.csv")
df4 = pd.read_csv("Fuentes para proyecto 2 normalizado\\4._Principios_Activos_y_Presentación.csv")
df6 = pd.read_csv("Fuentes para proyecto 2 normalizado\\6-Medicamentos_adquiridos_por_hospital.csv")


# Connect to your Neo4j database
uri = "bolt://localhost:7687"  # Replace with your Neo4j server URI
username = "neo4j"  # Replace with your Neo4j username
password = "proyecto2"  # Replace with your Neo4j password

def file1():
    # Create nodes in Neo4j
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            for _, row in df1.iterrows():
                data = {
                    "nombre_producto": row["NOMBRE DEL PRODUCTO FARMACEUTICO"],
                    "tipo_farmaco": row["TIPO DE FARMACO"],
                    "nombre_laboratorio": row["NOMBRE DEL LABORATORIO OFERTANTE"],
                    # "estado": row["ESTADO"],
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
                
def file2():
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            for _, row in df2.iterrows():
                data = {
                    "grupo": row["GRUPO"],
                    "descripcion": row["DESCRIPCION"]
                }
                session.write_transaction(create_nodes_f2, data)
                
def file3():
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            for _, row in df3.iterrows():
                data = {
                    "nombre": row["NOMBRE"],
                    "codigo_de_medicamento": row["CODIGO DE MEDICAMENTO"]
                }
                session.write_transaction(create_nodes_f3, data)
def file4():
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
                    "fabricante": row["FABRICANTE"]
                    # "precio_maximo_de_venta": row["PRECIO MAXIMO DE VENTA TRANSACCION FINAL COMERCIAL"]
                }
                session.write_transaction(create_nodes_f4, data)               
def file6():
    # Create nodes in Neo4j
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            for _, row in df6.iterrows():
                data = {
                    # "mes": row["MES"],
                    # "fecha": row["FECHA"],
                    # "servicio": row["SERVICIO"],
                    "descripcion": row["DESCRIPCION"],
                    # "tipo": row["TIPO"],
                    # "unidad": row["UNIDAD"],
                    "piezas_solicitadas": row["PIEZAS SOLICITADAS"],
                    # "piezas_surtidas": row["PIEZAS SURTIDAS"]#,
                    # "precio_unitario": row["PRECIO UNITARIO"],
                    # "marca": row["MARCA"]
                }
                session.write_transaction(create_nodes_f6, data)

# file1()
# file2()
# file3()
# file4()
# file6()

def consulta1():
    result = []
    
    # Connect to the Neo4j database
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            # Cypher query
            query = """
            MATCH (m:Medication), (p:PharmaceuticalProductInfo)
            WHERE m.DESCRIPCION <> p.NOMBRE_DEL_PRODUCTO_FARMACEUTICO
            CREATE (m)-[:MISMATCH]->(p);

            MATCH (m:Medication), (p:PharmaceuticalProductInfo)
            WHERE m.PRINCIPIO_ACTIVO_O_ASOCIACION_DE_PRINCIPIOS_ACTIVOS = p.DESCRIPCION_PRINCIPIO_ACTIVO
            CREATE (m)-[:MATCH]->(p);

            RETURN p.NOMBRE_DEL_PRODUCTO_FARMACEUTICO AS PRODUCTO_FARMACEUTICO,
                   m.PRINCIPIO_ACTIVO_O_ASOCIACION_DE_PRINCIPIOS_ACTIVOS AS PRINCIPIO_ACTIVO,
                   p.NOMBRE_GENERICO AS NOMBRE_GENERICO,
                   p.FABRICANTE AS FABRICANTE,
                   p.TIPO_DE_FARMACO AS TIPO_DE_FARMACO,
                   p.MEDICAMENTO_HUERFANO AS MEDICAMENTO_HUERFANO;
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


# Function to execute the Cypher query and return the result
def consulta2():
    result = []

    # Connect to the Neo4j database
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            query = """
            MATCH (p:PharmaceuticalProductInfo)
            WHERE NOT EXISTS {
              MATCH (m:Medication {DESCRIPCION: p.NOMBRE_DEL_PRODUCTO_FARMACEUTICO})
            }
            RETURN DISTINCT p.NOMBRE_DEL_LABORATORIO_OFERTANTE;
            """
            result = session.read_transaction(lambda tx: list(tx.run(query)))
    
    return result

# result = consulta2()
# for record in result:
#     print(record["p.NOMBRE_DEL_LABORATORIO_OFERTANTE"])

def consulta3(input_value):
    result = []

    # Connect to the Neo4j database
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            query = """
                MATCH (m:MedicationInfo)
                WHERE m.DESCRIPCION_PRINCIPIO_ACTIVO = $input
                WITH m
                MATCH (n:MedicationInfo)
                WHERE m.NOMBRE_GENERICO = n.DESCRIPCION_PRINCIPIO_ACTIVO
                RETURN m.DESCRIPCION_PRINCIPIO_ACTIVO AS DESCRIPCION_PRINCIPIO_ACTIVO, n.NOMBRE_GENERICO AS NOMBRE_GENERICO;
            """
            result = session.read_transaction(lambda tx: list(tx.run(query, input=input_value)))
    
    return result

# result = consulta3('EXEMESTANO')
# for record in result:
#     print("DESCRIPCION PRINCIPIO ACTIVO:", record["DESCRIPCION_PRINCIPIO_ACTIVO"])
#     print("NOMBRE GENERIC0:", record["NOMBRE_GENERICO"])

def consulta7():
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