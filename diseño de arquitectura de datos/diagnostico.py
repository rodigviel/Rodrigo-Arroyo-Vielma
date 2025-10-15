import pandas as pd
import sqlite3

def analizar_dataset(nombre, df):
    print(f"\n===== Análisis de {nombre} =====")

    # Porcentaje de completitud
    completitud = df.notnull().mean() * 100
    print("\nPorcentaje de completitud (%):")
    print(completitud)

    # Valores nulos por columna
    print("\nValores nulos por columna:")
    print(df.isnull().sum())

    # Duplicados
    duplicados = df.duplicated().sum()
    print(f"\nCantidad de registros duplicados: {duplicados}")
    print("Registros duplicados:", duplicados)  

if __name__ == "__main__":
    # Carga de archivos
    clientes = pd.read_csv("clientes.csv")
    productos = pd.read_csv("productos.csv")
    ventas = pd.read_csv("ventas.csv")

    # Análisis de calidad
    analizar_dataset("Clientes", clientes)
    analizar_dataset("Productos", productos)
    analizar_dataset("Ventas", ventas)

    # Eliminar duplicados antes de cargar a SQLite
    clientes = clientes.drop_duplicates()
    productos = productos.drop_duplicates()
    ventas = ventas.drop_duplicates()

    # ETL: Cargar ventas a SQLite
    conn = sqlite3.connect("modelo_dw.sqlite")
    ventas.to_sql("ventas", conn, if_exists="replace", index=False)
    productos.to_sql("productos", conn, if_exists="replace", index=False)
    clientes.to_sql("clientes", conn, if_exists="replace", index=False)
    conn.close()
    print("\nDatos cargados exitosamente en modelo_dw.sqlite.")