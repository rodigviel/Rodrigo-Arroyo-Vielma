class LibroNoEncontrado(Exception):
    def __init__(self):
        """este mensaje se desplegará si al consultar libro por autor o género, no se identifica ninguno
        que cumpla los criterios"""
        print("Error: El libro no fue encontrado.")

class UsuarioNoRegistrado(Exception):
    def __init__(self):
        """este mensaje se desplegará si al intentar realizar un préstamo, el usuario al que se quiere 
        realizar el préstamo no extiste"""
        print("Error: El usuario no está registrado.")

class PrestamoDuplicado(Exception):
    def __init__(self):
        """este mensaje se desplegará si al intentar realizar un préstamo, el libro no se encuentra 
        disponible"""
        print("Error: El libro ya ha sido prestado.")
