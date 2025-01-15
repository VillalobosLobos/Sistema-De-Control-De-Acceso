import customtkinter as ctk
from tkinter import filedialog
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
from PIL import Image,ImageTk
from io import BytesIO
from .agregarEstudiante import agregarEstudiante
from .subirExcel import subirExcel
import os

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		#Para el botón de regreso
		btimg(self,"paquete/img/atras.png",0,0,30,30,"e")

		#Para las etiquetas de texto
		etiqueta(self,"Agregar estudiante","white",50,-1,-1,280,20,"w")
		
		etiqueta(self,"Boleta","white",30,-1,-1,10,130,"w")
		etiqueta(self,"Nombre","white",30,-1,-1,10,170,"w")
		etiqueta(self,"Grupos","white",30,-1,-1,10,210,"w")
		etiqueta(self,"Turno","white",30,-1,-1,10,250,"w")
		etiqueta(self,"Especialidad","white",30,-1,-1,10,290,"w")

		#Campos de texto
		self.campoBoleta = campo(self,"Ingrese la boleta",c.altura,580,c.tamLetra,-1,-1,100,132,"w")
		self.campoNombre = campo(self,"Nombre del alumno",c.altura,558,c.tamLetra,-1,-1,120,172,"w")
		self.campoGrupos = campo(self,"Grupos del alumno",c.altura,567,c.tamLetra,-1,-1,110,212,"w")
		self.campoTurno = campo(self,"Turno del alumno",c.altura,588,c.tamLetra,-1,-1,90,252,"w")
		self.campoEspecialidad = campo(self,"Especialidad del alumno",c.altura,500,c.tamLetra,-1,-1,180,292,"w")

		self.imagen="e"
		#Botones
		boton(self,"Agregar",40,c.verdeFuerte,c.verdeClaro,100,10,self.agregarEstudiante,-1,-1,20,400,-1)
		boton(self,"Examinar",40,c.verdeFuerte,c.verdeClaro,100,10,self.examinar,-1,-1,220,400,-1)
		boton(self,"Importar excel",40,c.verdeFuerte,c.verdeClaro,100,10,self.excel,-1,-1,430,400,-1)
		boton(self,"subir fotos",40,c.verdeFuerte,c.verdeClaro,100,10,self.fotos,-1,-1,730,400,-1)

		#Para la imagen del usuario
		foto(self,"paquete/img/usuario.png",680,100,250,250)

	def cerrar(self):
		self.master.destroy()
		self.master.master.deiconify()

	def agregarEstudiante(self):
		if self.campoBoleta.get()=="":
			alerta("Falta ingresar\nla boleta")
		elif self.campoNombre.get()=="":
			alerta("Falta ingresar\nel nombre")
		elif self.campoGrupos.get()=="":
			alerta("Falta ingresar\nel grupo")
		elif self.campoTurno.get()=="":
			alerta("Falta ingresar\nel tunro")
		elif self.campoEspecialidad.get()=="":
			alerta("Falta ingresar\nla especialidad")
		elif self.imagen=="e":
			alerta("Falta ingresar\nla foto del\nestudiante")
		else:
			agregarEstudiante(
					self.campoBoleta.get(),
					self.campoNombre.get(),
					self.campoGrupos.get(),
					self.campoTurno.get(),
					self.campoEspecialidad.get(),
					self.campoBoleta.get())

			with open(self.imagen,'rb') as archivo:
				archivos={
					"imagen":archivo
				}

				respuesta=requests.post("http://127.0.0.1:8000/subirImagen/"+self.campoBoleta.get()+".png",files=archivos)
				if respuesta.status_code!=200:
					alerta("Error al subir \nla imagen")

		

	def examinar(self):
		fotoUsuario=filedialog.askopenfilename(
			title="Selecciona foto del estudiante",
			filetypes=[("Archivos de imagen", "*.png *jpg")])

		if foto:
			try:
				foto(self,fotoUsuario,680,100,250,250)
				self.imagen=fotoUsuario
			except Exception as e:
				print(e)
				alerta("Error en la imagen")

	def fotos(self):
		carpeta = filedialog.askdirectory(
			title="Selecciona la carpeta que contiene las imágenes")
		if carpeta:
			try:
				imagenes = [
					os.path.join(carpeta, archivo)
					for archivo in os.listdir(carpeta)
					if archivo.lower().endswith(".jpg")
				]

				if not imagenes:
					alerta("No se encontraron\nlas imagenes")
				for imagen in imagenes:
					with open(imagen,'rb') as archivo:
						archivos={
							"imagen":archivo
						}

						respuesta=requests.post("http://127.0.0.1:8000/subirImagen/"+str(os.path.basename(imagen)),files=archivos)
						if respuesta.status_code!=200:
							alerta("Error al subir \nla imagen")
				alerta("Se cargaron\ncorrectamente\nlas imagenes")
			except Exception as e:
				print(e)

	def excel(self):
		doc=filedialog.askopenfilename(
			title="Selecciona el Excel",
			filetypes=[("Archivos de Excel", "*.xlsx *.xls *.csv")])

		if doc:
			try:
				subirExcel(doc)
				alerta("Se cargo\ncorrectamente\nel excel")
			except Exception as e:
				print(e)
				alerta("Error en con\nel Excel")

class Inicio(ctk.CTkToplevel):
	def __init__(self):
		super().__init__()
		self.geometry(c.dimensiones)
		self.title("Agregar estudiante")

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

