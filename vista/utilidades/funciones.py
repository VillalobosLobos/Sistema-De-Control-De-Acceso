from utilidades import vigilante as v
import requests

URL="http://127.0.0.1:8000/"

def ingresar(usuario,contraseña,raiz):
	datos={
		"usuario":usuario,
		"contraseña":contraseña
	}
	response=requests.post(URL+"login",json=datos)
	
	if response.text=="Correcto":
		if usuario[0]=='V':
			ventana=v.Inicio()
			ventana.configure(fg_color="white")
			ventana.mainloop()



