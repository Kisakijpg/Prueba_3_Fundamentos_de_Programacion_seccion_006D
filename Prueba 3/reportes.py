import json
from libros import cargar_datos, buscar_libro

def mostrar_libros_prestados(archivo, usuario_id):
    datos = cargar_datos(archivo)
    prestamos = [prestamo for prestamo in datos['Prestamo'] if prestamo['UsuarioID'] == usuario_id]
    if prestamos:
        libros_prestados = [buscar_libro(archivo, prestamo['LibroID']) for prestamo in prestamos]
        return libros_prestados
    else:
        return "Usuario sin préstamos"

def libro_mas_solicitado(archivo):
    datos = cargar_datos(archivo)
    conteo_prestamos = {}
    for prestamo in datos['Prestamo']:
        libro_id = prestamo['LibroID']
        if libro_id in conteo_prestamos:
            conteo_prestamos[libro_id] += 1
        else:
            conteo_prestamos[libro_id] = 1
    libro_mas_solicitado_id = max(conteo_prestamos, key=conteo_prestamos.get)
    return buscar_libro(archivo, libro_mas_solicitado_id)

def generar_reporte(archivo, reporte_archivo):
    datos = cargar_datos(archivo)
    reporte = {
        "LibrosPrestadosPorUsuario": {},
        "LibroMasSolicitado": libro_mas_solicitado(archivo)
    }
    for usuario in datos['Usuario']:
        reporte["LibrosPrestadosPorUsuario"][usuario['UsuarioID']] = mostrar_libros_prestados(archivo, usuario['UsuarioID'])
    with open(reporte_archivo, 'w') as file:
        json.dump(reporte, file, ensure_ascii=False, indent=4)