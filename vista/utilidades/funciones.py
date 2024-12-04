import requests

url="http://127.0.0.1:8000/login"

def ingresar(usuario,contraseña):
	datos={
		"usuario":usuario,
		"contraseña":contraseña
	}
	response=requests.post(url,json=datos)
	
	if response.text=="Correcto" and usuario[0]=='V':
		print(response.text)
	elif response.text=="Correcto" and usuario[0]=='A':
		print(response.text)



