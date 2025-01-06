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
		print("No hay conexión\ndel servidor")
	else:
		if response.text=="Correcto" and usuario[0]=='V':
			print("vigilante")
			'''
			root.withdraw()
			ventana=v.Inicio()
			ventana.configure(fg_color="white")
			ventana.protocol("WM_DELETE_WINDOW", lambda: aparecer(root,ventana))
			ventana.mainloop()
			'''
		elif response.text=="Correcto" and usuario[0]=='A':
			print("administrador")
			'''
			root.withdraw()
			ventana=a.Inicio()
			ventana.configure(fg_color="white")
			ventana.protocol("WM_DELETE_WINDOW", lambda: aparecer(root,ventana))
			ventana.mainloop()
			'''
		else:
			print("Error en el usuario \no contraseña")
