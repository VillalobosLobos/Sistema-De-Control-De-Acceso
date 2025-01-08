from .alerta import alerta
import requests
import json

URL="http://127.0.0.1:8000/"

def  buscar(boleta):
	try:
		return json.loads(requests.get(URL+"info/"+boleta).text)
	except json.decoder.JSONDecodeError as e:
		alerta("No sé encontro \nel usuario")
	else:
		alerta("No se ingreso una\n boleta válida")
