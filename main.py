#TI3032-U3-EVALUACIÓN-SUMATIVA-PYTHON-MONGODB-AlexanderCortés-AngeloZamora
import os
import subprocess
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client: MongoClient = MongoClient(MONGO_URI)

try:
    print("Estableciendo conexión ⌛")
    client.admin.command("ping")
    print(" Conexión establecida 😁 👌")
except:
    print(" ❌ Error de conexión 🤣 🤣")
    exit(code=1)

db = client["TI3032_U3_EF"]  # Elijo la base de datos
coleccion_invitados = db["invitados"]
coleccion_eventos = db["eventos"]

# ==================== CARGA INICIAL ====================


def cargar_datos():
    """Limpia las colecciones y las vuelve a poblar con los datos embebidos."""
    print("Limpiando colecciones...")
    coleccion_invitados.drop()
    coleccion_eventos.drop()
    print("Insertando invitados...")
    coleccion_invitados.insert_many(
        [
            {
                "rut": "11.009.876-3",
                "nombre": "Camila Herrera",
                "correo": "camila.herrera@empresa.cl",
                "empresa": "EmpresaX",
                "estado": "bloqueado",
            },
            {
                "rut": "11.019.752-6",
                "nombre": "Carla Rojas",
                "correo": "carla.rojas@empresa.cl",
                "empresa": "BlueCom",
                "estado": "activo",
            },
            {
                "rut": "11.029.628-9",
                "nombre": "Luis Fernández",
                "correo": "luis.fernandez@contratista.cl",
                "empresa": "DataShield",
                "estado": "activo",
            },
            {
                "rut": "11.039.504-2",
                "nombre": "Ana Martínez",
                "correo": "ana.martinez@empresa.cl",
                "empresa": "Inacap",
                "estado": "activo",
            },
            {
                "rut": "11.049.380-5",
                "nombre": "Diego López",
                "correo": "diego.lopez@empresa.cl",
                "empresa": "EmpresaX",
                "estado": "activo",
            },
            {
                "rut": "11.059.256-8",
                "nombre": "María González",
                "correo": "maria.gonzalez@inacap.cl",
                "empresa": "DataShield",
                "estado": "bloqueado",
            },
            {
                "rut": "11.069.132-1",
                "nombre": "José Pérez",
                "correo": "jose.perez@contratista.cl",
                "empresa": "EmpresaX",
                "estado": "activo",
            },
            {
                "rut": "11.079.008-4",
                "nombre": "Felipe Castro",
                "correo": "felipe.castro@contratista.cl",
                "empresa": "DataShield",
                "estado": "activo",
            },
            {
                "rut": "11.088.884-7",
                "nombre": "Valentina Soto",
                "correo": "valentina.soto@empresa.cl",
                "empresa": "AndesLog",
                "estado": "activo",
            },
            {
                "rut": "11.098.760-0",
                "nombre": "Ricardo Núñez",
                "correo": "ricardo.nunez@empresa.cl",
                "empresa": "AndesLog",
                "estado": "activo",
            },
            {
                "rut": "11.108.636-3",
                "nombre": "Tomás Vergara",
                "correo": "tomas.vergara@contratista.cl",
                "empresa": "Inacap",
                "estado": "activo",
            },
            {
                "rut": "11.118.512-6",
                "nombre": "Daniela Salinas",
                "correo": "daniela.salinas@contratista.cl",
                "empresa": "BlueCom",
                "estado": "activo",
            },
            {
                "rut": "11.128.388-9",
                "nombre": "Andrés Muñoz",
                "correo": "andres.munoz@empresa.cl",
                "empresa": "EmpresaX",
                "estado": "activo",
            },
            {
                "rut": "11.138.264-2",
                "nombre": "Fernanda Campos",
                "correo": "fernanda.campos@contratista.cl",
                "empresa": "CyberLab",
                "estado": "activo",
            },
            {
                "rut": "11.148.140-5",
                "nombre": "Javier Ortiz",
                "correo": "javier.ortiz@contratista.cl",
                "empresa": "NorteDigital",
                "estado": "activo",
            },
            {
                "rut": "11.158.016-8",
                "nombre": "Paula Rivera",
                "correo": "paula.rivera@empresa.cl",
                "empresa": "TechNova",
                "estado": "activo",
            },
            {
                "rut": "11.167.892-1",
                "nombre": "Cristóbal Sáez",
                "correo": "cristobal.saez@contratista.cl",
                "empresa": "AndesLog",
                "estado": "activo",
            },
            {
                "rut": "11.177.768-4",
                "nombre": "Ignacia Torres",
                "correo": "ignacia.torres@empresa.cl",
                "empresa": "NorteDigital",
                "estado": "activo",
            },
            {
                "rut": "11.187.644-7",
                "nombre": "Matías Castillo",
                "correo": "matias.castillo@empresa.cl",
                "empresa": "Inacap",
                "estado": "activo",
            },
            {
                "rut": "11.197.520-0",
                "nombre": "Rocío Paredes",
                "correo": "rocio.paredes@empresa.cl",
                "empresa": "BlueCom",
                "estado": "bloqueado",
            },
            {
                "rut": "11.207.396-3",
                "nombre": "Sebastián Fuentes",
                "correo": "sebastian.fuentes@empresa.cl",
                "empresa": "EmpresaX",
                "estado": "activo",
            },
            {
                "rut": "11.217.272-6",
                "nombre": "Gabriela Vega",
                "correo": "gabriela.vega@inacap.cl",
                "empresa": "BlueCom",
                "estado": "bloqueado",
            },
            {
                "rut": "11.227.148-9",
                "nombre": "Nicolás Araya",
                "correo": "nicolas.araya@empresa.cl",
                "empresa": "NorteDigital",
                "estado": "activo",
            },
            {
                "rut": "11.237.024-2",
                "nombre": "Catalina Contreras",
                "correo": "catalina.contreras@contratista.cl",
                "empresa": "Inacap",
                "estado": "activo",
            },
            {
                "rut": "11.246.900-5",
                "nombre": "Joaquín Reyes",
                "correo": "joaquin.reyes@inacap.cl",
                "empresa": "Inacap",
                "estado": "activo",
            },
        ]
    )
    print("Insertando eventos...")
    coleccion_eventos.insert_many(
        [
            {
                "codigo": "EVT-2025-001",
                "nombre": "Evento 1 - Datos",
                "fecha": "2025-12-25T20:00:00Z",
                "lugar": "Auditorio B",
                "categoria": "charla",
                "invitados": [
                    {"rut": "11.118.512-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.098.760-0", "estado": "confirmado", "checkin": False},
                    {"rut": "11.079.008-4", "estado": "confirmado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.059.256-8", "estado": "confirmado", "checkin": False},
                    {"rut": "11.029.628-9", "estado": "pendiente", "checkin": False},
                    {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.148.140-5", "estado": "confirmado", "checkin": False},
                    {"rut": "11.197.520-0", "estado": "confirmado", "checkin": False},
                    {"rut": "11.187.644-7", "estado": "confirmado", "checkin": False},
                    {"rut": "11.019.752-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.246.900-5", "estado": "confirmado", "checkin": False},
                    {"rut": "11.177.768-4", "estado": "pendiente", "checkin": False},
                    {"rut": "11.207.396-3", "estado": "pendiente", "checkin": False},
                    {"rut": "11.237.024-2", "estado": "rechazado", "checkin": False},
                    {"rut": "11.217.272-6", "estado": "pendiente", "checkin": False},
                    {"rut": "11.227.148-9", "estado": "pendiente", "checkin": False},
                    {"rut": "11.128.388-9", "estado": "pendiente", "checkin": False},
                ],
            },
            {
                "codigo": "EVT-2025-002",
                "nombre": "Evento 2 - Seguridad",
                "fecha": "2025-12-27T20:00:00Z",
                "lugar": "Auditorio A",
                "categoria": "charla",
                "invitados": [
                    {"rut": "11.158.016-8", "estado": "pendiente", "checkin": False},
                    {"rut": "11.187.644-7", "estado": "pendiente", "checkin": False},
                    {"rut": "11.059.256-8", "estado": "confirmado", "checkin": False},
                    {"rut": "11.088.884-7", "estado": "rechazado", "checkin": False},
                    {"rut": "11.098.760-0", "estado": "rechazado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "pendiente", "checkin": False},
                    {"rut": "11.049.380-5", "estado": "pendiente", "checkin": False},
                    {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.118.512-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.108.636-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.029.628-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.167.892-1", "estado": "confirmado", "checkin": False},
                    {"rut": "11.217.272-6", "estado": "rechazado", "checkin": False},
                    {"rut": "11.207.396-3", "estado": "confirmado", "checkin": False},
                ],
            },
            {
                "codigo": "EVT-2025-003",
                "nombre": "Evento 3 - MongoDB",
                "fecha": "2025-12-27T20:00:00Z",
                "lugar": "Auditorio B",
                "categoria": "workshop",
                "invitados": [
                    {"rut": "11.039.504-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.049.380-5", "estado": "confirmado", "checkin": False},
                    {"rut": "11.237.024-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.197.520-0", "estado": "confirmado", "checkin": False},
                    {"rut": "11.128.388-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.069.132-1", "estado": "confirmado", "checkin": False},
                    {"rut": "11.177.768-4", "estado": "confirmado", "checkin": False},
                    {"rut": "11.029.628-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.019.752-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.207.396-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.108.636-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.187.644-7", "estado": "confirmado", "checkin": False},
                    {"rut": "11.098.760-0", "estado": "confirmado", "checkin": False},
                    {"rut": "11.158.016-8", "estado": "confirmado", "checkin": False},
                    {"rut": "11.246.900-5", "estado": "confirmado", "checkin": False},
                    {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.217.272-6", "estado": "pendiente", "checkin": False},
                    {"rut": "11.227.148-9", "estado": "pendiente", "checkin": False},
                    {"rut": "11.079.008-4", "estado": "pendiente", "checkin": False},
                    {"rut": "11.059.256-8", "estado": "pendiente", "checkin": False},
                    {"rut": "11.118.512-6", "estado": "pendiente", "checkin": False},
                ],
            },
            {
                "codigo": "EVT-2025-004",
                "nombre": "Evento 4 - DevOps",
                "fecha": "2025-12-25T19:00:00Z",
                "lugar": "Auditorio B",
                "categoria": "meetup",
                "invitados": [
                    {"rut": "11.079.008-4", "estado": "confirmado", "checkin": False},
                    {"rut": "11.128.388-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.246.900-5", "estado": "pendiente", "checkin": False},
                    {"rut": "11.069.132-1", "estado": "confirmado", "checkin": False},
                    {"rut": "11.167.892-1", "estado": "pendiente", "checkin": False},
                    {"rut": "11.158.016-8", "estado": "pendiente", "checkin": False},
                    {"rut": "11.118.512-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "rechazado", "checkin": False},
                    {"rut": "11.177.768-4", "estado": "confirmado", "checkin": False},
                    {"rut": "11.088.884-7", "estado": "confirmado", "checkin": False},
                ],
            },
            {
                "codigo": "EVT-2025-005",
                "nombre": "Evento 5 - MongoDB",
                "fecha": "2025-12-30T18:00:00Z",
                "lugar": "Auditorio A",
                "categoria": "charla",
                "invitados": [
                    {"rut": "11.197.520-0", "estado": "pendiente", "checkin": False},
                    {"rut": "11.246.900-5", "estado": "rechazado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.158.016-8", "estado": "confirmado", "checkin": False},
                    {"rut": "11.207.396-3", "estado": "rechazado", "checkin": False},
                    {"rut": "11.118.512-6", "estado": "pendiente", "checkin": False},
                    {"rut": "11.029.628-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.039.504-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.128.388-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.069.132-1", "estado": "rechazado", "checkin": False},
                    {"rut": "11.079.008-4", "estado": "pendiente", "checkin": False},
                    {"rut": "11.187.644-7", "estado": "confirmado", "checkin": False},
                    {"rut": "11.217.272-6", "estado": "pendiente", "checkin": False},
                    {"rut": "11.108.636-3", "estado": "rechazado", "checkin": False},
                    {"rut": "11.059.256-8", "estado": "pendiente", "checkin": False},
                    {"rut": "11.019.752-6", "estado": "confirmado", "checkin": False},
                ],
            },
            {
                "codigo": "EVT-2025-006",
                "nombre": "Evento 6 - MongoDB",
                "fecha": "2025-12-24T20:00:00Z",
                "lugar": "Auditorio B",
                "categoria": "charla",
                "invitados": [
                    {"rut": "11.237.024-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.207.396-3", "estado": "pendiente", "checkin": False},
                    {"rut": "11.039.504-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.167.892-1", "estado": "confirmado", "checkin": False},
                    {"rut": "11.049.380-5", "estado": "pendiente", "checkin": False},
                    {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.069.132-1", "estado": "pendiente", "checkin": False},
                    {"rut": "11.187.644-7", "estado": "rechazado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "pendiente", "checkin": False},
                    {"rut": "11.088.884-7", "estado": "pendiente", "checkin": False},
                    {"rut": "11.227.148-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.246.900-5", "estado": "pendiente", "checkin": False},
                ],
            },
            {
                "codigo": "EVT-2025-007",
                "nombre": "Evento 7 - Datos",
                "fecha": "2025-12-29T18:00:00Z",
                "lugar": "Sala 204",
                "categoria": "charla",
                "invitados": [
                    {"rut": "11.217.272-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.108.636-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.019.752-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.148.140-5", "estado": "confirmado", "checkin": False},
                    {"rut": "11.079.008-4", "estado": "confirmado", "checkin": False},
                    {"rut": "11.177.768-4", "estado": "confirmado", "checkin": False},
                    {"rut": "11.158.016-8", "estado": "confirmado", "checkin": False},
                    {"rut": "11.128.388-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.118.512-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.049.380-5", "estado": "confirmado", "checkin": False},
                    {"rut": "11.227.148-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.207.396-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.197.520-0", "estado": "confirmado", "checkin": False},
                    {"rut": "11.088.884-7", "estado": "confirmado", "checkin": False},
                    {"rut": "11.138.264-2", "estado": "rechazado", "checkin": False},
                    {"rut": "11.237.024-2", "estado": "pendiente", "checkin": False},
                    {"rut": "11.059.256-8", "estado": "rechazado", "checkin": False},
                    {"rut": "11.069.132-1", "estado": "pendiente", "checkin": False},
                    {"rut": "11.039.504-2", "estado": "pendiente", "checkin": False},
                ],
            },
            {
                "codigo": "EVT-2025-008",
                "nombre": "Evento 8 - Seguridad",
                "fecha": "2025-12-28T19:00:00Z",
                "lugar": "Auditorio B",
                "categoria": "workshop",
                "invitados": [
                    {"rut": "11.128.388-9", "estado": "pendiente", "checkin": False},
                    {"rut": "11.148.140-5", "estado": "rechazado", "checkin": False},
                    {"rut": "11.108.636-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.029.628-9", "estado": "pendiente", "checkin": False},
                    {"rut": "11.079.008-4", "estado": "pendiente", "checkin": False},
                    {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.217.272-6", "estado": "rechazado", "checkin": False},
                    {"rut": "11.069.132-1", "estado": "rechazado", "checkin": False},
                    {"rut": "11.098.760-0", "estado": "confirmado", "checkin": False},
                ],
            },
        ]
    )
    print("✅ Datos cargados exitosamente.\n")


# ==================== FUNCIONES DE CONSULTA ====================


def listar_eventos():
    """Muestra todos los eventos con código, nombre, fecha, lugar y categoría."""
    print("\n--- LISTADO DE EVENTOS ---")
    eventos = coleccion_eventos.find(
        {}, {"codigo": 1, "nombre": 1, "fecha": 1, "lugar": 1, "categoria": 1}
    )
    for ev in eventos:
        print(f"Código: {ev['codigo']}")
        print(f"Nombre: {ev['nombre']}")
        print(f"Fecha: {ev['fecha']}")
        print(f"Lugar: {ev['lugar']}")
        print(f"Categoría: {ev['categoria']}")
        print("-" * 40)


def filtrar_eventos_por_categoria():
    """Filtra eventos por la categoría que ingrese el usuario."""
    cat = input("Ingrese la categoría a buscar: ").strip()
    if not cat:
        print("No se ingresó una categoría.")
        return

    eventos = coleccion_eventos.find(
        {"categoria": cat},
        {"codigo": 1, "nombre": 1, "fecha": 1, "lugar": 1, "categoria": 1},
    )
    encontrados = False
    for ev in eventos:
        encontrados = True
        print(f"Código: {ev['codigo']}")
        print(f"Nombre: {ev['nombre']}")
        print(f"Fecha: {ev['fecha']}")
        print(f"Lugar: {ev['lugar']}")
        print(f"Categoría: {ev['categoria']}")
        print("-" * 40)
    if not encontrados:
        print(f"No hay eventos en la categoría '{cat}'.")


def buscar_invitados_regex():
    """Busca invitados por nombre o correo usando expresiones regulares (Ignora Mayusculas)"""
    patron = input("Ingresa el patrón a buscar (nombre o correo): ").strip()
    if not patron:
        print("Patrón vacío. Cancelando búsqueda.")
        return

    query = {
        "$or": [
            {"nombre": {"$regex": patron, "$options": "i"}},
            {"correo": {"$regex": patron, "$options": "i"}},
        ]
    }
    try:
        resultados = list(coleccion_invitados.find(query))
        print("\n--- RESULTADOS DE BÚSQUEDA ---")
        for inv in resultados:
            print(
                f"RUT: {inv['rut']}, Nombre: {inv['nombre']}, Correo: {inv['correo']}, Empresa: {inv['empresa']}, Estado: {inv['estado']}"
            )
    except Exception:
        print("Patrón de expresión regular no válido. Intente con otro patrón.")
    print("-" * 40)


def validar_acceso_evento():
    """
    Valida el acceso de un invitado a eventos.
    El invitado debe estar 'activo' y en el evento su estado debe ser 'confirmado'.
    Utiliza $lookup para cruzar las colecciones.
    """
    rut = input("Ingresa el RUT del invitado (ej: 11.009.876-3): ").strip()
    if not rut:
        print("RUT no ingresado.")
        return

    pipeline = [
        {"$match": {"invitados.rut": rut}},
        {"$unwind": "$invitados"},
        {"$match": {"invitados.rut": rut, "invitados.estado": "confirmado"}},
        {
            "$lookup": {
                "from": "invitados",
                "localField": "invitados.rut",
                "foreignField": "rut",
                "as": "invitado_info",
            }
        },
        {"$unwind": "$invitado_info"},
        {"$match": {"invitado_info.estado": "activo"}},
        {
            "$project": {
                "codigo": 1,
                "nombre": 1,
                "fecha": 1,
                "lugar": 1,
                "categoria": 1,
                "invitado_info.nombre": 1,
            }
        },
    ]

    eventos = coleccion_eventos.aggregate(pipeline)
    eventos_list = list(eventos)

    if not eventos_list:
        print(
            f"No se encontraron eventos para el RUT {rut} con estado 'confirmado' y el invitado activo."
        )
    else:
        nombre_invitado = (
            eventos_list[0].get("invitado_info", {}).get("nombre", "Invitado")
        )
        print(f"\n--- EVENTOS A LOS QUE {nombre_invitado} TIENE ACCESO ---")
        for ev in eventos_list:
            print(
                f"Código: {ev['codigo']}, Nombre: {ev['nombre']}, Fecha: {ev['fecha']}, Lugar: {ev['lugar']}, Categoría: {ev['categoria']}"
            )
    print("-" * 40)


def top_3_eventos_confirmados():
    """Muestra los tres eventos con mayor cantidad de invitados confirmados."""
    print("\n--- TOP 3 EVENTOS CON MÁS INVITADOS CONFIRMADOS ---")
    pipeline = [
        {
            "$project": {
                "codigo": 1,
                "nombre": 1,
                "confirmados": {
                    "$size": {
                        "$filter": {
                            "input": "$invitados",
                            "as": "inv",
                            "cond": {"$eq": ["$$inv.estado", "confirmado"]},
                        }
                    }
                },
            }
        },
        {"$sort": {"confirmados": -1}},
        {"$limit": 3},
    ]
    resultados = coleccion_eventos.aggregate(pipeline)
    for idx, ev in enumerate(resultados, 1):
        print(
            f"{idx}. Código: {ev['codigo']}, Nombre: {ev['nombre']}, Confirmados: {ev['confirmados']}"
        )
    print("-" * 40)


# ==================== MENÚ PRINCIPAL ====================


def limpiar_pantalla():
    """Limpia la consola"""
    subprocess.run("cls", shell=True, check=True)


def menu():
    """Bucle principal del programa."""
    while True:
        limpiar_pantalla()
        print("""
            ======================================
            |   GESTOR DE EVENTOS E INVITADOS   |
            ======================================
            1. Listar todos los eventos
            2. Filtrar eventos por categoría
            3. Buscar invitados por patrón (regex)
            4. Validar acceso de un invitado a eventos (con $lookup)
            5. Top 3 eventos con más invitados confirmados
            6. Salir
            """)
        opcion = input("Selecciona una opción [1-6]: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            print("\n=== LISTADO DE EVENTOS ===\n")
            listar_eventos()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "2":
            limpiar_pantalla()
            print("\n=== FILTRAR EVENTOS POR CATEGORÍA ===\n")
            filtrar_eventos_por_categoria()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "3":
            limpiar_pantalla()
            print("\n=== BÚSQUEDA DE INVITADOS ===\n")
            buscar_invitados_regex()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "4":
            limpiar_pantalla()
            print("\n=== VALIDACIÓN DE ACCESO CON $lookup ===\n")
            validar_acceso_evento()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "5":
            limpiar_pantalla()
            print("\n=== TOP 3 EVENTOS ===\n")
            top_3_eventos_confirmados()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "6":
            limpiar_pantalla()
            print("Saliendo del programa...")
            break
        else:
            input("Opción inválida. Presiona ENTER para continuar...")


# ==================== EJECUCIÓN ====================

if __name__ == "__main__":
    cargar_datos()
    menu()
