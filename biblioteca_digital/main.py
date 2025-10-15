"""Programa principal para gestión de biblioteca."""

import modulos.libros as gl
import modulos.usuarios as gu
import modulos.prestamos as gp

def mostrar_menu():
    print("\n--- Menú Biblioteca Digital ---")
    print("1. Registrar nuevo libro")
    print("2. Registrar nuevo usuario")
    print("3. Consultar libros por autor")
    print("4. Consultar libros por género")
    print("5. Mostrar libros disponibles")
    print("6. Realizar préstamo")
    print("7. Listar préstamos")
    print("8. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        t = input("Título: ")
        a = input("Autor: ")
        g = input("Género: ")
        gl.registrar_libro(t, a, g)

    elif opcion == "2":
        n = input("Nombre: ")
        r = input("Rol (estudiante/instructor): ")
        gu.registrar_usuario(n, r)

    elif opcion == "3":
        a = input("Autor: ")
        try:
            gl.buscar_por_autor(a)
        except Exception:
            pass

    elif opcion == "4":
        g = input("Género: ")
        try:
            gl.buscar_por_genero(g)
        except Exception:
            pass

    elif opcion == "5":
        gl.mostrar_disponibles()

    elif opcion == "6":
        u = input("Nombre del usuario: ")
        t = input("Título del libro: ")
        try:
            gp.prestar_libro(u, t)
        except Exception:
            pass

    elif opcion == "7":
        gp.listar_prestamos()

    elif opcion == "8":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")
