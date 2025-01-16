from .administrador import Inicio as a
from .vigilante import Inicio as v
from .alerta import alerta
import requests
import json

URL="http://127.0.0.1:8000/"

def ingresar(usuario,contraseña,root):
	datos={
		"usuario":usuario,
		"contraseña":contraseña
	}
	try:
		response=requests.post(URL+"login",json=datos)
	except requests.exceptions.ConnectionError as e:
		alerta("No hay conexión\ndel servidor")
	else:
		if response.text=="Vigilante":
			root.withdraw()
			ventana=v()
			ventana.configure(fg_color="white")
		elif response.text=="Administrador":
			root.withdraw()
			ventana=a()
			ventana.configure(fg_color="white")
		else:
			alerta("Error en el usuario \no contraseña")
