from libros import agregar_libro, editar_libro, eliminar_libro, buscar_libro, nada
from reportes import mostrar_libros_prestados, libro_mas_solicitado, generar_reporte

archivo_json = 'biblioteca.json'
reporte_json = 'Reportes_biblioteca_mundo_libro.json'

def nombre_principal():
    while True:
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Editar libro")
        print("3. Eliminar libro")
        print("4. Buscar libro")
        print("5. Mostrar libros prestados a un usuario")
        print("6. Mostrar el libro más solicitado")
        print("7. Generar reporte")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nuevo_libro = {
                "LibroID": int(input("ID del libro: ")),
                "Titulo": input("Título: "),
                "AutorID": int(input("AutorID: ")),
                "CategoriaID": int(input("CategoríaID: ")),
                "AnoPublicacion": int(input("Año de publicación: ")),
                "ISBN": input("ISBN: ")
            }
            agregar_libro(archivo_json, nuevo_libro)
            print("Libro agregado exitosamente.")
        
        elif opcion == "2":
            libro_id = int(input("ID del libro a editar: "))
            nueva_info = {
                "Titulo": input("Nuevo título: "),
                "AutorID": int(input("Nuevo AutorID: ")),
                "CategoriaID": int(input("Nueva CategoríaID: ")),
                "AnoPublicacion": int(input("Nuevo año de publicación: "))
            }
            editar_libro(archivo_json, libro_id, nueva_info)
            print("Libro editado exitosamente.")
        
        elif opcion == "3":
            libro_id = int(input("ID del libro a eliminar: "))
            eliminar_libro(archivo_json, libro_id)
            print("Libro eliminado exitosamente.")
        
        elif opcion == "4":
            libro_id = int(input("ID del libro a buscar: "))
            libro = buscar_libro(archivo_json, libro_id)
            if libro != nada:
                print(libro)
            else:
                print("Libro no encontrado.")
        
        elif opcion == "5":
            usuario_id = int(input("ID del usuario: "))
            prestamos = mostrar_libros_prestados(archivo_json, usuario_id)
            print(prestamos)
        
        elif opcion == "6":
            libro = libro_mas_solicitado(archivo_json)
            print(libro)
        
        elif opcion == "7":
            generar_reporte(archivo_json, reporte_json)
            print(f"Reporte generado en {reporte_json}")
        
        elif opcion == "8":
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    nombre_principal()