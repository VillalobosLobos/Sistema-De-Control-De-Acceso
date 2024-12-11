from utilidades import vigilante as v
from utilidades import administrador as a
from utilidades import utilidades as u
from utilidades import actualizarAlumnos as aa
from utilidades import eliminarAlumnos as ea
import requests
import json

URL="http://127.0.0.1:8000/"

def aux():
	pass

def ingresar(usuario,contraseña,root):
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
			root.withdraw()
			ventana=v.Inicio()
			ventana.configure(fg_color="white")
			ventana.protocol("WM_DELETE_WINDOW", lambda: aparecer(root,ventana))
			ventana.mainloop()
		elif response.text=="Correcto" and usuario[0]=='A':
			root.withdraw()
			ventana=a.Inicio()
			ventana.configure(fg_color="white")
			ventana.protocol("WM_DELETE_WINDOW", lambda: aparecer(root,ventana))
			ventana.mainloop()

		else:
			u.alerta("Error en el usuario \no contraseña")

def ventanaActualizarAlumno(root):
	root.withdraw()
	ventana=aa.Inicio()
	ventana.configure(fg_color="white")
	ventana.protocol("WM_DELETE_WINDOW", lambda: aparecer(root,ventana))
	ventana.mainloop()

def ventanaEliminarAlumno(root):
	root.withdraw()
	ventana=ea.Inicio()
	ventana.configure(fg_color="white")
	ventana.protocol("WM_DELETE_WINDOW", lambda: aparecer(root,ventana))
	ventana.mainloop()

def aparecer(root,v):
	v.destroy()
	root.deiconify()

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
			u.alerta("Registro de entrada\ny salida éxitoso")
		else:
			response=requests.get(URL+"registrarAlumno/"+boleta+"/true")
			u.alerta("Registro de entrada\ny salida éxitoso")

def actualizarAlumno(boleta,nombre,grupos,turno,especialidad,foto):
	datos={
		"boleta":boleta,
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
		u.alerta(response.text)

def eliminarAlumno(boleta):
	print(boleta)
	try:
		response=requests.delete(URL+"eliminarAlumno/"+boleta)
	except requests.exceptions.ConnectionError as e:
		u.alerta("No hay conexión\ndel servidor")
	else:
		u.alerta(response.text)



	


