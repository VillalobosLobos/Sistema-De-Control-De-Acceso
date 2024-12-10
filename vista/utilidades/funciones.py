from utilidades import vigilante as v
from utilidades import administrador as a
from utilidades import utilidades as u
import requests
import json

URL="http://127.0.0.1:8000/"

def aux():
	pass

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
		if response.text=="Correcto" and usuario[0]=='V':
			ventana=v.Inicio()
			ventana.configure(fg_color="white")
			ventana.mainloop()
		elif response.text=="Correcto" and usuario[0]=='A':
			ventana=a.Inicio()
			ventana.configure(fg_color="white")
			ventana.mainloop()

		else:
			u.alerta("Error en el usuario \no contraseña")

def buscar(boleta):
	try:
		return json.loads(requests.get(URL+"info/"+boleta).text)
	except json.decoder.JSONDecodeError as e:
		u.alerta("No sé encontro \nel usuario")

def registrar(boleta):
	try:
		datos=buscar(boleta)
	except json.decoder.JSONDecodeError as e:
		u.alerta("No sé pudo registrar \nla entrada o salida")
	else:
		if datos==None:
			pass
		elif datos["estado"]=="true":
			response=requests.get(URL+"registrarAlumno/"+boleta+"/false")
		else:
			response=requests.get(URL+"registrarAlumno/"+boleta+"/true")

def actualizarAlumno(nombre,grupos,turno,especialidad,foto):
	datos={
		"nombre":nombre,
		"grupos":grupos,
		"turno":turno,
		"especialidad":especialidad,
		"foto":foto
	}
	try:
		response=requests.post(URL+"actualizarAlumno",json=datos)
	except requests.exceptions.ConnectionError as e:
		u.alerta("No hay conexión\ndel servidor")
	else:
		pass


