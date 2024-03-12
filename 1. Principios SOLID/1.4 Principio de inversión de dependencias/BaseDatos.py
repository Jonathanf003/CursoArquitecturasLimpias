class BaseDatos:

    def guardar(self, id, data):
        self.datos[id] = data
        print(f"Dato guardado con el id {id}")

    def leer(self, id):
        if id in self.datos:
            return self.datos[id]
        else:
            print(f"No se encontró el dato con el id {id}")
            return None