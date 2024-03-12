from BaseDatos import BaseDatos
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDB(BaseDatos):
    def __init__(self, uri, database_name, collection_name):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[database_name]
            self.collection = self.db[collection_name]
            # Intento de comprobar la conexión
            self.client.admin.command('ismaster')
            print("Conectado exitosamente a MongoDB")
        except ConnectionFailure as e:
            print(f"No se pudo conectar a MongoDB: {e}")
            self.client = None

    def guardar(self, id, data):
        if self.client:
            try:
                result = self.collection.update_one({"id": id}, {"$set": data}, upsert=True)
                if result.upserted_id or result.matched_count > 0:
                    print(f"Dato con id {id} guardado con éxito.")
                else:
                    print(f"No se pudo guardar el dato con id {id}.")
            except Exception as e:
                print(f"Error al guardar el dato: {e}")

    def leer(self, id):
        if self.client:
            try:
                data = self.collection.find_one({"id": id})
                if data:
                    return data
                else:
                    print(f"No se encontró el dato con id {id}.")
                    return None
            except Exception as e:
                print(f"Error al leer el dato: {e}")
                return None

    def __del__(self):
        if self.client:
            self.client.close()
            print("Conexión a MongoDB cerrada")
