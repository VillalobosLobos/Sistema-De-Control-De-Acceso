import json
from .alerta import alerta
import requests

def agregarEstudiante(boleta,nombre,grupos,turno,especialidad,foto):
	datos={
		"boleta":boleta,
		"nombre":nombre,
		"grupos":grupos,
		"turno":turno,
		"especialidad":especialidad,
		"foto":"fotos/"+boleta+".png"
	}
	try:
		response=requests.post("http://127.0.0.1:8000/altaAlumno",json=datos)
	except requests.exceptions.ConnectionError as e:
		alerta("No hay conexión\ndel servidor")
	else:
		alerta(response.text)
