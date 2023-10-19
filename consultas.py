import pandas as pd


def consulta1():
    caja_meds_df = pd.read_csv('Fuentes para proyecto 2 normalizado\\6-Medicamentos_adquiridos_por_hospital.csv')
    general_meds_df = pd.read_csv('Fuentes para proyecto 2 normalizado\\1.1_Nombre_de_productos_genéricos_y_Farmaceutica.csv')

    simplify_caja_meds_df = caja_meds_df[['DESCRIPCION']].drop_duplicates()
    simplify_general_meds_df = general_meds_df[['NOMBRE DEL PRODUCTO FARMACEUTICO']].drop_duplicates()

    # reducir las columnas, hacer drop duplicates 

    # indices_iguales = caja_meds_df[~caja_meds_df['DESCRIPCION'].isin(general_meds_df['NOMBRE DEL PRODUCTO FARMACEUTICO'])].index
    to_buy_meds_df = simplify_general_meds_df[~simplify_general_meds_df['NOMBRE DEL PRODUCTO FARMACEUTICO'].isin(simplify_caja_meds_df['DESCRIPCION'])]

    print(to_buy_meds_df)

consulta1()