"""Módulo para la gestión de libros."""

libros = []    #lista que irá agregando los libros que sean registrados

class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({self.genero}) [{estado}]"

def registrar_libro(titulo, autor, genero):
    libro = Libro(titulo, autor, genero)
    libros.append(libro)
    print("Libro registrado correctamente.")

def buscar_por_autor(autor):
    encontrados = [l for l in libros if l.autor == autor]
    if encontrados:
        for l in encontrados:
            print(l)
    else:
        from excepciones.errores import LibroNoEncontrado
        raise LibroNoEncontrado()

def buscar_por_genero(genero):
    encontrados = [l for l in libros if l.genero == genero]
    if encontrados:
        for l in encontrados:
            print(l)
    else:
        from excepciones.errores import LibroNoEncontrado
        raise LibroNoEncontrado()

def mostrar_disponibles():
    disponibles = [l for l in libros if l.disponible]
    for l in disponibles:
        print(l)
