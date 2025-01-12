import json
from .alerta import alerta
import requests

def eliminarEstudiante(boleta):
	try:
		response=requests.delete("http://127.0.0.1:8000/eliminarAlumno/"+boleta)
	except requests.exceptions.ConnectionError as e:
		alerta("No hay conexión\ndel servidor")
	else:
		alerta(response.text)
