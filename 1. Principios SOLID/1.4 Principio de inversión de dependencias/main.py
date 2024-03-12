from BaseDatos import BaseDatos
from ManjeadorDatos import ManejadorDatos
from MongoDB import MongoDB
from MySQL import MySQL


db = BaseDatos()
manejador = ManejadorDatos()
# Diccionario de datos a procesar
datos_a_procesar = {1: "Dato 1", 2: "Dato 2", 3: "Dato 3"}
# Procesar los datos con el manejador
manejador.procesar(db, datos_a_procesar)


mysql_db = MySQL(host="localhost", database="nombre_base_datos", user="tu_usuario", password="tu_contraseña")
mysql_db.guardar(1, "Este es un dato de prueba")
print(mysql_db.leer(1))


uri = "tu_uri_de_conexion_a_mongodb"
database_name = "tu_base_de_datos"
collection_name = "tu_coleccion"
mongodb = MongoDB(uri, database_name, collection_name)
    # Guardar un dato
mongodb.guardar("1", {"id": "1", "dato": "Este es un dato de prueba"})
    # Leer y mostrar el dato guardado
print(mongodb.leer("1"))