import requests

url = "http://localhost:8000/"

# GET para mostrar estudiantes de la carrera de Economía
ruta_get_estudiantes_economia = url + "estudiantes_economia"
get_response_estudiantes_economia = requests.get(ruta_get_estudiantes_economia)
