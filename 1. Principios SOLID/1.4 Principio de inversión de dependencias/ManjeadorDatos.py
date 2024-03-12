class ManejadorDatos:
    def procesar(self, base_datos, datos):
        # Guardar datos en la base de datos
        for id, dato in datos.items():
            base_datos.guardar(id, dato)
            print(f"Guardado: {id} -> {dato}")

        # Leer y mostrar los datos guardados
        for id in datos.keys():
            dato_leido = base_datos.leer(id)
            if dato_leido is not None:
                print(f"Leído: {id} -> {dato_leido}")
            else:
                print(f"Error al leer el dato con id {id}")