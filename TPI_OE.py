import pandas as pd
from datetime import datetime

# ==========================================
# CARGAR BASE DE DATOS
# ==========================================

try:
    archivo = "STOCK DE AGRO Y CONST DE NEWW HOLLAND.xlsx"

    df = pd.read_excel(archivo, sheet_name=0)

    # Limpiar nombres de columnas
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.upper()
    )

    print("\nBase de datos cargada correctamente.")

except Exception as e:
    print("\nError al cargar Excel:")
    print(e)
    exit()

# ==========================================
# LISTA DE RESERVAS
# ==========================================

reservas = []

# ==========================================
# GUARDAR CAMBIOS EN EXCEL
# ==========================================

def guardar_excel():
    try:
        df.to_excel(archivo, index=False)
        return True
    except Exception as e:
        print("\nNo se pudo guardar el Excel.")
        print("Verifique que el archivo esté cerrado.")
        print("Error:", e)
        return False


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def menu():

    print("\n========== CHATBOT NORDEMAQ ==========")
    print("1 - Ver maquinaria disponible")
    print("2 - Buscar maquinaria por modelo")
    print("3 - Buscar por línea")
    print("4 - Buscar por ubicación")
    print("5 - Buscar por año de fabricación")
    print("6 - Ver máquinas en tránsito")
    print("7 - Simular reserva")
    print("8 - Ver máquinas reservadas")
    print("9 - Ver máquinas vendidas")
    print("10 - Cambio de estado")
    print("11 - Ver stock completo")
    print("12 - Salir")


# ==========================================
# COLUMNAS REALES DEL EXCEL
# ==========================================

COL_MODELO = "MODELO / CONFIGURACION"
COL_LINEA = "LÍNEA"
COL_ESTADO = "ESTADO"
COL_UBICACION = "UBICACION"
COL_CHASIS = "CHASIS N°"
COL_ANIO = "AÑO DE FABRICACION"
COL_ARRIBO = "FECHA ESTIM. DE ARRIBO A PUERTO"


# ==========================================
# 1 - VER MAQUINARIA DISPONIBLE
# ==========================================

def ver_disponibles():

    disponibles = df[
        df[COL_ESTADO]
        .astype(str)
        .str.upper()
        .str.contains("DISPONIBLE", na=False)
    ]

    if disponibles.empty:
        print("\nNo hay maquinaria disponible.")
        return

    print("\n===== MAQUINARIA DISPONIBLE =====")

    for linea, grupo in disponibles.groupby(COL_LINEA):

        print(f"\n===== {linea} =====")
        print(f"Cantidad total: {len(grupo)}")

        modelos = grupo[COL_MODELO].value_counts()

        for modelo, cantidad in modelos.items():

            print(
                f"{modelo} → "
                f"{cantidad} unidad/es"
            )


# ==========================================
# 2 - BUSCAR POR MODELO
# ==========================================

def buscar_modelo():

    busqueda = input(
        "\nIngrese modelo: "
    ).strip().upper()

    palabras = busqueda.split()

    resultados = []

    for _, fila in df.iterrows():

        modelo_excel = str(
            fila[COL_MODELO]
        ).upper()

        coincide = all(
            palabra in modelo_excel
            for palabra in palabras
        )

        if coincide:
            resultados.append(fila)

    if not resultados:

        print("\nModelo no encontrado.")
        return

    print("\n===== RESULTADOS =====")

    for fila in resultados:

        print(f"""
Modelo: {fila[COL_MODELO]}
Línea: {fila[COL_LINEA]}
Ubicación: {fila[COL_UBICACION]}
Estado: {fila[COL_ESTADO]}
Chasis: {fila[COL_CHASIS]}
----------------------------------------
""")
# ==========================================
# 3 - BUSCAR POR LÍNEA
# ==========================================

def buscar_linea():

    linea = input(
        "\nIngrese línea: "
    ).strip().upper()

    resultado = df[
        df[COL_LINEA]
        .astype(str)
        .str.upper()
        .str.contains(linea, na=False)
    ]

    if resultado.empty:

        print("\nNo se encontraron resultados.")
        return

    print("\n===== RESULTADOS =====")

    for _, fila in resultado.iterrows():

        print(f"""
Modelo: {fila[COL_MODELO]}
Línea: {fila[COL_LINEA]}
Ubicación: {fila[COL_UBICACION]}
Estado: {fila[COL_ESTADO]}
Chasis: {fila[COL_CHASIS]}
----------------------------------------
""")


# ==========================================
# 4 - BUSCAR POR UBICACIÓN
# ==========================================

def buscar_ubicacion():

    ubicacion = input(
        "\nIngrese ubicación: "
    ).strip().upper()

    resultado = df[
        df[COL_UBICACION]
        .astype(str)
        .str.upper()
        .str.contains(ubicacion, na=False)
    ]

    if resultado.empty:

        print("\nNo se encontraron resultados.")
        return

    print("\n===== RESULTADOS =====")

    for _, fila in resultado.iterrows():

        print(f"""
Modelo: {fila[COL_MODELO]}
Línea: {fila[COL_LINEA]}
Ubicación: {fila[COL_UBICACION]}
Estado: {fila[COL_ESTADO]}
Chasis: {fila[COL_CHASIS]}
----------------------------------------
""")


# ==========================================
# 5 - BUSCAR POR AÑO DE FABRICACIÓN
# ==========================================

def buscar_anio():

    anio = input(
        "\nIngrese año de fabricación: "
    ).strip()

    resultado = df[
        df[COL_ANIO]
        .astype(str)
        .str.contains(anio, na=False)
    ]

    if resultado.empty:

        print(
            "\nNo se encontraron maquinarias "
            "para ese año."
        )
        return

    print(
        f"\n===== AÑO DE FABRICACIÓN: "
        f"{anio} ====="
    )

    for _, fila in resultado.iterrows():

        print(f"""
Modelo: {fila[COL_MODELO]}
Línea: {fila[COL_LINEA]}
Año: {fila[COL_ANIO]}
Ubicación: {fila[COL_UBICACION]}
Estado: {fila[COL_ESTADO]}
Chasis: {fila[COL_CHASIS]}
----------------------------------------
""")


# ==========================================
# 6 - VER MÁQUINAS EN TRÁNSITO
# ==========================================

def ver_transito():

    transito = df[
        df[COL_ESTADO]
        .astype(str)
        .str.upper()
        .str.contains("TRANSITO", na=False)
    ]

    if transito.empty:

        print(
            "\nNo hay máquinas "
            "en tránsito."
        )
        return

    print(
        "\n===== MÁQUINAS EN TRÁNSITO ====="
    )

    for _, fila in transito.iterrows():

        print(f"""
Modelo: {fila[COL_MODELO]}
Ubicación: {fila[COL_UBICACION]}
Arribo: {fila[COL_ARRIBO]}
Chasis: {fila[COL_CHASIS]}
Estado: {fila[COL_ESTADO]}
----------------------------------------
""")


# ==========================================
# 7 - SIMULAR RESERVA
# ==========================================

def simular_reserva():

    modelo = input(
        "\nIngrese modelo a reservar: "
    ).strip().upper()

    palabras = modelo.split()

    resultados = []

    for _, fila in df.iterrows():

        modelo_excel = str(
            fila[COL_MODELO]
        ).upper()

        estado = str(
            fila[COL_ESTADO]
        ).upper()

        coincide = all(
            palabra in modelo_excel
            for palabra in palabras
        )

        if coincide and "DISPONIBLE" in estado:

            resultados.append(fila)

    if not resultados:

        print(
            "\nNo hay máquinas disponibles "
            "para ese modelo."
        )
        return

    print("\n===== DISPONIBLES =====")

    for i, fila in enumerate(
        resultados,
        start=1
    ):

        print(
            f"{i}) "
            f"{fila[COL_MODELO]} "
            f"| {fila[COL_UBICACION]} "
            f"| Chasis: {fila[COL_CHASIS]}"
        )

    while True:

        opcion = input(
            "\nSeleccione número: "
        )

        if opcion.isdigit():

            opcion = int(opcion)

            if 1 <= opcion <= len(resultados):
                break

        print("Opción inválida.")

    seleccion = resultados[opcion - 1]

    cliente = input(
        "\nNombre del cliente: "
    ).strip().title()

    fecha = datetime.now().strftime(
        "%d/%m/%Y"
    )

    reserva = {
        "modelo": seleccion[COL_MODELO],
        "chasis": seleccion[COL_CHASIS],
        "ubicacion": seleccion[COL_UBICACION],
        "cliente": cliente,
        "fecha": fecha
    }

    reservas.append(reserva)

    df.at[
        seleccion.name,
        COL_ESTADO
    ] = "RESERVADO"

    if guardar_excel():

        print(
            "\nReserva guardada "
            "correctamente."
        )

    print(f"""
===== RESERVA EXITOSA =====
Cliente: {cliente}
Modelo: {reserva['modelo']}
Chasis: {reserva['chasis']}
Ubicación: {reserva['ubicacion']}
Fecha: {fecha}
===========================
""")     

# ==========================================
# 8 - VER MÁQUINAS RESERVADAS
# ==========================================

def ver_reservadas():

    if len(reservas) == 0:

        print("\nNo hay reservas registradas.")
        return

    print("\n===== MÁQUINAS RESERVADAS =====")

    for reserva in reservas:

        print(f"""
Fecha: {reserva['fecha']}
Cliente: {reserva['cliente']}
Modelo: {reserva['modelo']}
Chasis: {reserva['chasis']}
Ubicación: {reserva['ubicacion']}
----------------------------------------
""")


# ==========================================
# 9 - VER MÁQUINAS VENDIDAS
# ==========================================

def ver_vendidas():

    vendidas = df[
        df[COL_ESTADO]
        .astype(str)
        .str.upper()
        .str.contains("VENDIDA|VENDIDO", na=False)
    ]

    if vendidas.empty:

        print("\nNo hay máquinas vendidas.")
        return

    print("\n===== MÁQUINAS VENDIDAS =====")

    for _, fila in vendidas.iterrows():

        print(f"""
Modelo: {fila[COL_MODELO]}
Línea: {fila[COL_LINEA]}
Ubicación: {fila[COL_UBICACION]}
Chasis: {fila[COL_CHASIS]}
Estado: {fila[COL_ESTADO]}
----------------------------------------
""")


# ==========================================
# 10 - CAMBIO DE ESTADO
# ==========================================

def cambio_estado():

    chasis = input(
        "\nIngrese el número de chasis: "
    ).strip()

    resultado = df[
        df[COL_CHASIS]
        .astype(str)
        .str.strip()
        == chasis
    ]

    if resultado.empty:

        print(
            "\nNo se encontró ninguna "
            "máquina con ese chasis."
        )
        return

    indice = resultado.index[0]

    print("\nMáquina encontrada:")

    print(f"""
Modelo: {df.at[indice, COL_MODELO]}
Estado actual: {df.at[indice, COL_ESTADO]}
""")

    nuevo_estado = input(
        "Ingrese nuevo estado: "
    ).strip().upper()

    df.at[
        indice,
        COL_ESTADO
    ] = nuevo_estado

    if guardar_excel():

        print(
            "\nEstado actualizado "
            "correctamente."
        )


# ==========================================
# 11 - VER STOCK COMPLETO
# ==========================================

def ver_stock_completo():

    print("\n===== STOCK COMPLETO =====")

    columnas = [
        COL_MODELO,
        COL_LINEA,
        COL_UBICACION,
        COL_CHASIS,
        COL_ANIO,
        COL_ESTADO
    ]

    existentes = [
        col for col in columnas
        if col in df.columns
    ]

    print(
        df[existentes]
        .to_string(index=False)
    )


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

while True:

    menu()

    opcion = input(
        "\nSeleccione opción: "
    ).strip()

    if not opcion.isdigit():

        print(
            "\nIngrese solamente números."
        )
        continue

    opcion = int(opcion)

    if opcion == 1:

        ver_disponibles()

    elif opcion == 2:

        buscar_modelo()

    elif opcion == 3:

        buscar_linea()

    elif opcion == 4:

        buscar_ubicacion()

    elif opcion == 5:

        buscar_anio()

    elif opcion == 6:

        ver_transito()

    elif opcion == 7:

        simular_reserva()

    elif opcion == 8:

        ver_reservadas()

    elif opcion == 9:

        ver_vendidas()

    elif opcion == 10:

        cambio_estado()

    elif opcion == 11:

        ver_stock_completo()

    elif opcion == 12:

        print(
            "\nSaliendo del Chatbot Nordemaq..."
        )
        print("¡Hasta luego!")
        break

    else:

        print(
            "\nOpción inválida. "
            "Ingrese un número del 1 al 12."
        )       