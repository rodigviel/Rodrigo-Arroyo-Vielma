usuarios = {}    #diccionario de usuarios, tipo de usuario que se agregarán a medida que se ingresen

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def tipo(self):
        return "General"

class Estudiante(Usuario):
    def tipo(self):
        return "Estudiante"

class Instructor(Usuario):
    def tipo(self):
        return "Instructor"

def registrar_usuario(nombre, rol):
    if rol == "estudiante":
        usuarios[nombre] = Estudiante(nombre)
    elif rol == "instructor":
        usuarios[nombre] = Instructor(nombre)
    else:
        print("Rol inválido. Debe ser 'estudiante' o 'instructor'.")
        return
    print("Usuario registrado correctamente.")
