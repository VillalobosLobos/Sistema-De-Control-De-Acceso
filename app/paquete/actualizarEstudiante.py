import json
from .alerta import alerta
import requests

def actualizarEstudiante(boleta,nombre,grupos,turno,especialidad):
	datos={
		"boleta":boleta,
		"nombre":nombre,
		"grupos":grupos,
		"turno":turno,
		"especialidad":especialidad,
		"foto":"fotos/"+boleta+".png"
	}
	try:
		response=requests.post("http://127.0.0.1:8000/actualizarAlumno",json=datos)
	except requests.exceptions.ConnectionError as e:
		alerta("No hay conexión\ndel servidor")
	else:
		alerta(response.text)


