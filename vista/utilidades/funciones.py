from utilidades import vigilante as v
from utilidades import utilidades as u
import requests
import json

URL="http://127.0.0.1:8000/"

def ingresar(usuario,contraseña,raiz):
	datos={
		"usuario":usuario,
		"contraseña":contraseña
	}
	try:
		response=requests.post(URL+"login",json=datos)
	except requests.exceptions.ConnectionError as e:
		u.alerta("No hay conexión\ndel servidor")
	else:
		if response.text=="Correcto":
			if usuario[0]=='V':
				ventana=v.Inicio()
				ventana.configure(fg_color="white")
				ventana.mainloop()
		else:
			u.alerta("Error en el usuario \no contraseña")

def buscar(boleta):
	try:
		return json.loads(requests.get(URL+"info/"+boleta).text)
	except json.decoder.JSONDecodeError as e:
		u.alerta("No sé encontro el usuario")

def registrar(boleta):
	try:
		datos=json.loads(requests.get(URL+"info/"+boleta).text)
	except json.decoder.JSONDecodeError as e:
		u.alerta("No sé pudo registrar \nla entrada o salida")
	else:
		if datos.get('estado')=="true":
			response=requests.get(URL+"registrar/"+boleta+"/false")
		else:
			response=requests.get(URL+"registrar/"+boleta+"/true")

