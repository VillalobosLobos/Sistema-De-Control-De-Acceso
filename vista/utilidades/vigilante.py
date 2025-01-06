from utilidades import utilidades as u
from utilidades import funciones as f
from utilidades import configuraciones as c
import customtkinter as ctk
from PIL import Image

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)
		self.imagenes={}

		#Para las etiquetas de texto
		u.agregarEtiqueta(self,"Registro de entrada y salida","white",50,0,1,20,20,"w")
		
		#Campos donde mostraremos la información del alumno
		u.frameInfoAlumno(self)

		my_image = ctk.CTkImage(light_image=Image.open("utilidades/img/cet1.png"),
					dark_image=Image.open("utilidades/img/cet1.png"),
					size=(100,100))
		image_label = ctk.CTkLabel(self, image=my_image, text="")
		image_label.grid(row=0,column=0,padx=20,pady=20,sticky="e")

class Inicio(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.geometry(c.dimensiones)
		self.title("Vigilante")

		#Agregando nuestro frame
		self.mi_frame=MiFrame(master=self)
		self.mi_frame.configure(fg_color="blue")#c.verde)
		self.mi_frame.grid(row=0,column=0,padx=20,pady=20,sticky="nsew")

		self.grid_rowconfigure(0,weight=1) #Fila 0 ocupara más espacio
		self.grid_columnconfigure(0,weight=1) #Columna 0 ocupara más espacio
