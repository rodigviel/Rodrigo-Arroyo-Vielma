"""Módulo para gestionar préstamos de libros."""

from modulos.libros import libros
from modulos.usuarios import usuarios
from excepciones.errores import UsuarioNoRegistrado, PrestamoDuplicado

prestamos = []

def prestar_libro(nombre_usuario, titulo_libro):
    usuario = usuarios.get(nombre_usuario)
    if not usuario:
        raise UsuarioNoRegistrado()

    libro = next((l for l in libros if l.titulo == titulo_libro), None)
    if not libro:
        from excepciones.errores import LibroNoEncontrado
        raise LibroNoEncontrado()

    if not libro.disponible:
        raise PrestamoDuplicado()

    libro.disponible = False
    prestamos.append((usuario, libro))
    print(f"El libro {libro.titulo} no está diisponible")

def listar_prestamos():
    for usuario, libro in prestamos:
        print(f"{usuario.nombre} ({usuario.tipo()}) tiene '{libro.titulo}'")
