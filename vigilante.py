import customtkinter
from PIL import Image
import requests
import json
import tkinter as tk

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from controlador.usuario import Usuario

class MiFrame(customtkinter.CTkFrame):
	def __init__(self,master,usuario,contraseña,**kwargs):
		super().__init__(master,**kwargs)
		self.usuario=usuario
		self.contraseña=contraseña

		self.usu=Usuario(self.usuario,self.contraseña)
		
		#Imagenes
		self.atras = customtkinter.CTkImage(
			light_image=Image.open("./img/atras.png"),
			dark_image=Image.open("./img/atras.png"),
			size=(35,30))

		self.atrasBoton = customtkinter.CTkButton(
			self,
			image=self.atras,
			fg_color="#058749",
			hover_color="#058749",
			text="",
			command=self.cerrar)
		self.atrasBoton.grid(row=0,column=0,padx=20,pady=20,sticky="w")


		self.agregarFoto("./img/usuario.png")

		#Etiquetas
		self.titulo = customtkinter.CTkLabel(
			self,
			text="Registro de Entrada y salida",
			font=("Impact",50))
		self.titulo.grid(row=0,column=1,padx=20,pady=20,sticky="w")

		#Frame del cuerpo
		self.frameEtiquetas = customtkinter.CTkFrame(self)
		self.frameEtiquetas.grid(row=1, column=1, padx=20, pady=20, sticky="nwes")
		self.frameEtiquetas.configure(fg_color="#058749")

		self.frameEtiquetas.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
		self.frameEtiquetas.grid_columnconfigure(0, weight=1)

		self.agregarCampos()

		#Boton
		self.buscar = customtkinter.CTkButton(
			self,
			text="Buscar",
			font=("Impact",40),
			fg_color="#044b29",
			hover_color="#03b25f",
			width=300,
			corner_radius=9,
			command=self.buscarBoleta)
		self.buscar.grid(row=2,column=1,padx=350,pady=20,sticky="e")

		self.registrar = customtkinter.CTkButton(
			self,
			text="Registrar",
			font=("Impact",40),
			fg_color="#044b29",
			hover_color="#03b25f",
			width=300,
			corner_radius=9,
			command=self.registrar)
		self.registrar.grid(row=2,column=1,padx=20,pady=20,sticky="w")

	def agregarCampos(self):
		self.frameBoleta = customtkinter.CTkFrame(self.frameEtiquetas)
		self.frameBoleta.pack(pady=5,padx=10,anchor="w")
		self.frameBoleta.configure(fg_color="#058749")
		self.boleta = customtkinter.CTkLabel(
			self.frameBoleta,
			text="Boleta",
			font=("Impact",40))
		self.boleta.pack(pady=5,padx=10,side="left")
		self.campoBoleta = customtkinter.CTkEntry(
			self.frameBoleta,
			height=50,
			width=490,
			placeholder_text="Ingrese su boleta",
			font=("Impact",30))
		self.campoBoleta.pack(pady=5,padx=10,side="left")


		self.frameNombre = customtkinter.CTkFrame(self.frameEtiquetas)
		self.frameNombre.pack(pady=5,padx=10,anchor="w")
		self.frameNombre.configure(fg_color="#058749")
		self.nombre = customtkinter.CTkLabel(
			self.frameNombre,
			text="Nombre",
			font=("Impact",40))
		self.nombre.pack(pady=5,padx=10,side="left")
		self.campoNombre = customtkinter.CTkEntry(
			self.frameNombre,
			height=50,
			width=470,
			placeholder_text="Nombre del alumno",
			font=("Impact",30))
		self.campoNombre.pack(pady=5,padx=10,side="left")
		#self.campoNombre.configure(state="disabled")


		self.frameGrupos = customtkinter.CTkFrame(self.frameEtiquetas)
		self.frameGrupos.pack(pady=5,padx=10,anchor="w")
		self.frameGrupos.configure(fg_color="#058749")
		self.grupos = customtkinter.CTkLabel(
			self.frameGrupos,
			text="Grupos",
			font=("Impact",40))	
		self.grupos.pack(pady=5,padx=10,side="left")
		self.campoGrupos = customtkinter.CTkEntry(
			self.frameGrupos,
			height=50,
			width=480,
			placeholder_text="Grupo del alumno",
			font=("Impact",30))
		self.campoGrupos.pack(pady=5,padx=10,side="left")
		#self.campoGrupos.configure(state="disabled")


		self.frameGrupos = customtkinter.CTkFrame(self.frameEtiquetas)
		self.frameGrupos.pack(pady=5,padx=10,anchor="w")
		self.frameGrupos.configure(fg_color="#058749")
		self.turno = customtkinter.CTkLabel(
			self.frameGrupos,
			text="Turno",
			font=("Impact",40))
		self.turno.pack(pady=5,padx=10,side="left")
		self.campoTurno = customtkinter.CTkEntry(
			self.frameGrupos,
			height=50,
			width=505,
			placeholder_text="Turno del alumno",
			font=("Impact",30))
		self.campoTurno.pack(pady=5,padx=10,side="left")
		#self.campoTurno.configure(state="disabled")


		self.frameEspecialidad = customtkinter.CTkFrame(self.frameEtiquetas)
		self.frameEspecialidad.pack(pady=5,padx=10,anchor="w")
		self.frameEspecialidad.configure(fg_color="#058749")
		self.especialidad = customtkinter.CTkLabel(
			self.frameEspecialidad,
			text="Especialidad",
			font=("Impact",40))
		self.especialidad.pack(pady=5,padx=10,side="left")
		self.campoEspecialidad = customtkinter.CTkEntry(
			self.frameEspecialidad,
			height=50,
			width=390,
			placeholder_text="Carrera del alumno",
			font=("Impact",30))
		self.campoEspecialidad.pack(pady=5,padx=10,side="left")
		#self.campoEspecialidad.configure(state="disabled")

	def alerta(self,titulo,mensaje):
		alerta=customtkinter.CTkToplevel()
		alerta.title(titulo)
		alerta.geometry("350x250")
		alerta.configure(fg_color="white")
		alerta.resizable(False,False)

		frame=customtkinter.CTkFrame(alerta,fg_color="#058749",width=340,height=240)
		frame.pack(pady=10,padx=10)

		'''txt=customtkinter.CTkLabel(
			frame,
			text=mensaje,
			font=("Impact",20),
			justify="center")
		txt.pack()'''
		alerta.focus()

	def cerrar(self):
		self.master.destroy()

	def registrar(self):
		boleta=self.campoBoleta.get()
		datos=self.usu.verInfo(boleta)

		if datos["estado"]=="true":
			self.usu.RegistrarSalida(boleta)
		else:
			self.usu.RegistrarEntrada(boleta)

	def agregarFoto(self,foto):
		self.foto = customtkinter.CTkImage(
			light_image=Image.open(foto),
			dark_image=Image.open(foto),
			size=(325,325))
	
		self.fotoLabel = customtkinter.CTkLabel(
			self,
			image = self.foto,
			text="")
		self.fotoLabel.grid(row=1,column=0,padx=20,pady=20,sticky="ew")

	def buscarBoleta(self):
		try:
			boleta=self.campoBoleta.get()
			datos=self.usu.verInfo(boleta)

			self.campoNombre.delete(0, tk.END)
			self.campoNombre.insert(0,datos["nombre"])

			self.campoGrupos.delete(0, tk.END)
			self.campoGrupos.insert(0,datos["grupos"])

			self.campoTurno.delete(0, tk.END)
			self.campoTurno.insert(0,datos["turno"])

			self.campoEspecialidad.delete(0, tk.END)
			self.campoEspecialidad.insert(0,datos["especialidad"])

			self.agregarFoto(datos["foto"])
		except (requests.exceptions.RequestException, requests.exceptions.HTTPError) as e:
			print("Ocurrio un error en el servidor")
			self.alerta("","Ocurrio un error en el servidor")
		except json.decoder.JSONDecodeError as e:
			self.alerta("","No se encuentro el registro")

class Vigilante(customtkinter.CTkToplevel):
	def __init__(self,usuario,contraseña):
		super().__init__()
		self.geometry("1090x650")
		self.title("Registro de la entrada")
		self.configure(fg_color="white")
		self.resizable(False,False)
		
     		#Creando nuestro Frame verde
		self.mi_frame=MiFrame(master=self,usuario=usuario,contraseña=contraseña)
		self.mi_frame.configure(fg_color="#058749")
		self.mi_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

		self.grid_rowconfigure(0,weight=1) #Fila 0 ocupara más espacio
		self.grid_columnconfigure(0,weight=1) #Columna 0 ocupara más espacio

		self.mainloop()


