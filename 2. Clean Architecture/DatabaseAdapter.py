import sqlite3

class DatabaseAdapter:
    def __init__(self, db_file):
        self.db_file = db_file

    def conectar(self):
        self.conexion = sqlite3.connect(self.db_file)
        self.cursor = self.conexion.cursor()

    def desconectar(self):
        self.conexion.close()

    def crear_tabla_usuarios(self):
        self.conectar()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY,
                                nombre TEXT NOT NULL,
                                correo_electronico TEXT NOT NULL,
                                contraseña TEXT NOT NULL
                                )''')
        self.conexion.commit()

    def guardar_usuario(self, usuario):
        self.conectar()
        self.cursor.execute('''INSERT INTO usuarios (nombre, correo_electronico, contraseña)
                                VALUES (?, ?, ?)''', (usuario.nombre, usuario.correo_electronico, usuario.contraseña))
        self.conexion.commit()