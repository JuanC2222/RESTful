import requests

url = "http://localhost:8000/"

# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante1 = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingenieria Agronomica",
}

nuevo_estudiante2 = {
    "nombre": "María",
    "apellido": "Gómez",
    "carrera": "Arquitectura",
}

nuevo_estudiante3 = {
    "nombre": "Pedro",
    "apellido": "Rodríguez",
    "carrera": "Medicina",
}
nuevo_estudiante4 = {
    "nombre": "Jose",
    "apellido": "Rodríguez",
    "carrera": "Economia",
}
nuevo_estudiante5 = {
    "nombre": "Luis",
    "apellido": "Rodríguez",
    "carrera": "Economia",
}


post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante1)

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante2)

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante3)

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante4)

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante5)
print(post_response.text)
#Agrega una ruta para mostrar todas las carreras
ruta_get_mostrar_carreras = url + "mostrar_carreras"
get_response_mostrar_carreras = requests.get(ruta_get_mostrar_carreras)

if get_response_mostrar_carreras.status_code == 200:
    data = get_response_mostrar_carreras.json()
    print("Carreras:", data['carreras'])
else:
    print("Error al mostrar carreras:", get_response_mostrar_carreras.status_code, get_response_mostrar_carreras.text)
    
# GET para mostrar estudiantes de la carrera de Economía
ruta_get_estudiantes_economia = url + "estudiantes_economia"
get_response_estudiantes_economia = requests.get(ruta_get_estudiantes_economia)
if get_response_estudiantes_economia.status_code == 200:
    estudiantes_economia = get_response_estudiantes_economia.json()
    print("Estudiantes de Economía:", estudiantes_economia)
else:
    print("Error al mostrar estudiantes de Economía:", get_response_estudiantes_economia.status_code, get_response_estudiantes_economia.text)    