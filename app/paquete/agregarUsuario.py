import customtkinter as ctk
from paquete import configuraciones as c
from .etiqueta import agregarEtiqueta as etiqueta
from .imagenes import agregarImagen as img
from .botonImagen import botonImagen as btimg
from .campo import agregarCampo as campo
from .boton import agregarBoton as boton
from .foto import foto
from .buscar import buscar
from .alerta import alerta
from .registrar import registrar
import requests
from PIL import Image
from io import BytesIO
from .campoC import campoC

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		#Para el botón de regreso
		btimg(self,"paquete/img/atras.png",0,0,30,30,"e")

		#Para las etiquetas de texto
		etiqueta(self,"Agregar usuario","white",50,-1,-1,330,20,"w")
		
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
		boton(self,"Agregar",40,c.verdeFuerte,c.verdeClaro,100,10,self.agregar,-1,-1,400,400,-1)

	def cerrar(self):
		self.master.destroy()
		self.master.master.deiconify()

	def comboboxRol(self,op):
		self.rolUsuario=op

	def comboboxTurno(self,op):
		self.turnoUsuario=op

	def agregar(self):
		datos={
			"usuario":self.campoUsuario.get(),
			"contraseña":self.campoContraseña.get(),
			"turno":self.turnoUsuario,
			"rol":self.rolUsuario
		}

		try:
			response=requests.post("http://127.0.0.1:8000/altaUsuario",json=datos)
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

