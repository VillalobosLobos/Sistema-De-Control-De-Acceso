import customtkinter as ctk
import configuraciones as c
from .etiqueta import agregarEtiqueta as etiqueta
from .imagenes import agregarImagen as img
from .botonImagen import botonImagen as btimg
from .campo import agregarCampo as campo
from .boton import agregarBoton as boton
from .foto import foto
import configuraciones as c
from .buscar import buscar
from .alerta import alerta
from .registrar import registrar
import requests
from PIL import Image
from io import BytesIO
from .etiquetaImagen import etiquetaImagen

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		#Para el botón de regreso
		btimg(self,"paquete/img/atras.png",0,0,30,30,"e")

		#Para las etiquetas de texto
		etiqueta(self,"Eliminar usuario","white",50,-1,-1,300,20,"w")
		
		etiqueta(self,"Usuario","white",35,-1,-1,110,130,"w")

		#Campos de texto
		self.campoUsuario = campo(self,"Usuario",c.altura,610,35,-1,-1,235,132,"w")

		etiquetaImagen(self,"paquete/img/basura.png",370,200,180,180)

		#Botones
		boton(self,"Eliminar",40,c.verdeFuerte,c.verdeClaro,100,10,self.eliminar,-1,-1,400,400,-1)

	def cerrar(self):
		self.master.destroy()
		self.master.master.deiconify()

	def eliminar(self):
		try:
			response=requests.delete("http://127.0.0.1:8000/eliminarUsuario/"+self.campoUsuario.get())
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

