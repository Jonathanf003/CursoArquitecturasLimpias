from User import User


class UseCase:
    @staticmethod
    def crear_usuario(nombre, correo_electronico, contraseña):
        new_user = User(None, nombre, correo_electronico, contraseña)
        return new_user