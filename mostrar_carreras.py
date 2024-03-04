import requests

url = "http://localhost:8000/mostrar_carreras"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Carreras:", data['carreras'])
else:
    print("Error:", response.status_code, response.text)
