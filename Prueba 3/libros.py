import json

nada = None

def cargar_datos(archivo):
    with open(archivo, 'r') as file:
        return json.load(file)

def guardar_datos(archivo, datos):
    with open(archivo, 'w') as file:
        json.dump(datos, file, ensure_ascii=False, indent=4)

def agregar_libro(archivo, nuevo_libro):
    datos = cargar_datos(archivo)
    datos['Libro'].append(nuevo_libro)
    guardar_datos(archivo, datos)

def editar_libro(archivo, libro_id, nueva_info):
    datos = cargar_datos(archivo)
    for libro in datos['Libro']:
        if libro['LibroID'] == libro_id:
            libro.update(nueva_info)
            break
    guardar_datos(archivo, datos)

def eliminar_libro(archivo, libro_id):
    datos = cargar_datos(archivo)
    datos['Libro'] = [libro for libro in datos['Libro'] if libro['LibroID'] != libro_id]
    guardar_datos(archivo, datos)

def buscar_libro(archivo, libro_id):
    datos = cargar_datos(archivo)
    for libro in datos['Libro']:
        if libro['LibroID'] == libro_id:
            return libro
    return nada