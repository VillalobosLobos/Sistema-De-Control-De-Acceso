from .etiqueta import agregarEtiqueta as etiqueta
from .botonImagen import botonImagen as btimg
from .imagenes import agregarImagen as img
from paquete import configuraciones as c
from .campo import agregarCampo as campo
from .boton import agregarBoton as boton
from paquete.campoC import campoC
from .registrar import registrar
import customtkinter as ctk
from .buscar import buscar
from .alerta import alerta
from .foto import foto
from io import BytesIO
from PIL import Image
import requests
import json

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		#Para el botón de regreso
		btimg(self,"paquete/img/atras.png",0,0,30,30,"e")

		#Para las etiquetas de texto
		etiqueta(self,"Actualizar usuario","white",50,-1,-1,330,20,"w")
		
		etiqueta(self,"Usuario","white",35,-1,-1,110,130,"w")
		etiqueta(self,"Contraseña","white",35,-1,-1,110,190,"w")

		#Campos de texto
		self.campoUsuario = campo(self,"Ingrese su usuario",c.altura,610,35,-1,-1,235,132,"w")
		self.campoContraseña = campoC(self,"Ingrese su contraseña",c.altura,558,35,-1,-1,290,192,"w")

		#Combobox para el rol
		rol=ctk.CTkComboBox(
			self,
			values=["Administrador","Vigilante"],
			command=self.comboboxRol,
			font=("Impact",25),
			dropdown_font=("Impact",25),
			width=230)

		rol.set("Administrador")
		rol.place(x=150,y=300)

		#Combobox para el turno
		turno=ctk.CTkComboBox(
			self,
			values=["Matutino","Vespertino"],
			command=self.comboboxTurno,
			font=("Impact",25),
			dropdown_font=("Impact",25),
			width=230)

		turno.set("Matutino")
		turno.place(x=550,y=300)


		self.rolUsuario="Administrador"
		self.turnoUsuario="Matutino"

		#Botones
		boton(self,"Buscar",40,c.verdeFuerte,c.verdeClaro,100,10,self.buscar,-1,-1,250,400,-1)
		boton(self,"Actualizar",40,c.verdeFuerte,c.verdeClaro,100,10,self.actualizar,-1,-1,550,400,-1)

	def cerrar(self):
		self.master.destroy()
		self.master.master.deiconify()

	def comboboxRol(self,op):
		self.rolUsuario=op

	def comboboxTurno(self,op):
		self.turnoUsuario=op

	def buscar(self):
		try:
			informacion=json.loads(requests.get("http://127.0.0.1:8000/infoUsuario/"+self.campoUsuario.get()).text)

			self.campoUsuario.delete(0,"end")
			self.campoUsuario.insert(0,informacion["usuario"])
			self.campoContraseña.delete(0,"end")
			self.campoContraseña.insert(0,informacion["contraseña"])
			self.turnoUsuario=informacion["turno"]
			self.rolUsuario=informacion["rol"]

		except json.decoder.JSONDecodeError as e:
			alerta("No sé encontro \nel usuario")

	def actualizar(self):
		datos={
			"usuario":self.campoUsuario.get(),
			"contraseña":self.campoContraseña.get(),
			"turno":self.turnoUsuario,
			"rol":self.rolUsuario
		}

		try:
			response=requests.post("http://127.0.0.1:8000/actualizarUsuario",json=datos)
		except requests.exceptions.ConnectionError as e:
			alerta("No hay conexión\ndel servidor")
		else:
			alerta(response.text)

class Inicio(ctk.CTkToplevel):
	def __init__(self):
		super().__init__()
		self.geometry(c.dimensiones)
		self.title("Agregar usuario")

		#Agregando nuestro frame
		self.mi_frame=MiFrame(master=self)
		self.mi_frame.configure(fg_color=c.verde)
		self.mi_frame.grid(row=0,column=0,padx=20,pady=20,sticky="nsew")

		self.grid_rowconfigure(0,weight=1) #Fila 0 ocupara más espacio
		self.grid_columnconfigure(0,weight=1) #Columna 0 ocupara más espacio

		self.protocol("WM_DELETE_WINDOW", self.cerrar)

	def cerrar(self):
		self.destroy()
		self.master.deiconify()

'''
inicio=Inicio()
inicio.configure(fg_color="white")
#inicio.resizable(False,False)
inicio.mainloop()
'''

