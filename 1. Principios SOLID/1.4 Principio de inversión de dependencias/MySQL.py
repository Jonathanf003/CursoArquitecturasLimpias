import mysql.connector
from mysql.connector import Error
from BaseDatos import BaseDatos, leer
from BaseDatos import guardar

class MySQL(BaseDatos):
    def __init__(self, host, database, user, password):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print(f"Conectado a MySQL Server versión {db_info}")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            self.connection = None

    def guardar(self, id, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"INSERT INTO tabla (id, data) VALUES (%s, %s) ON DUPLICATE KEY UPDATE data=%s", (id, data, data))
            self.connection.commit()
            print(f"Dato guardado con éxito: {id}")
        except Error as e:
            print(f"Error al guardar dato: {e}")

    def leer(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT data FROM tabla WHERE id = %s", (id,))
            row = cursor.fetchone()
            if row:
                return row[0]
            else:
                print(f"No se encontró el dato con el id {id}")
                return None
        except Error as e:
            print(f"Error al leer dato: {e}")
            return None

    def __del__(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión a MySQL cerrada")
