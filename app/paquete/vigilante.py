import customtkinter as ctk
import configuraciones as c
from .etiqueta import agregarEtiqueta as etiqueta
from .imagenes import agregarImagen as img
from .botonImagen import botonImagen as btimg
from .campo import agregarCampo as campo
from .boton import agregarBoton as boton
from .foto import foto
import configuraciones as c

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		#Para el botón de regreso
		btimg(self,"paquete/img/atras.png",0,0,30,30,"e")

		#Para las etiquetas de texto
		etiqueta(self,"Registro de entrada y salida","white",50,-1,-1,180,20,"w")
		
		etiqueta(self,"Boleta","white",30,-1,-1,10,130,"w")
		etiqueta(self,"Nombre","white",30,-1,-1,10,170,"w")
		etiqueta(self,"Grupos","white",30,-1,-1,10,210,"w")
		etiqueta(self,"Turno","white",30,-1,-1,10,250,"w")
		etiqueta(self,"Especialidad","white",30,-1,-1,10,290,"w")

		#Campos de texto
		campoBoleta = campo(self,"Ingrese la boleta",c.altura,580,c.tamLetra,-1,-1,100,132,"w")
		campoNombre = campo(self,"Nombre del alumno",c.altura,558,c.tamLetra,-1,-1,120,172,"w")
		campoGrupos = campo(self,"Grupos del alumno",c.altura,567,c.tamLetra,-1,-1,110,212,"w")
		campoTruno = campo(self,"Turno del alumno",c.altura,588,c.tamLetra,-1,-1,90,252,"w")
		campoEspecialidad = campo(self,"Especialidad del alumno",c.altura,500,c.tamLetra,-1,-1,180,292,"w")

		#Botones
		boton(self,"Buscar",40,c.verdeFuerte,c.verdeClaro,100,10,"",-1,-1,250,400,-1)
		boton(self,"Registrar",40,c.verdeFuerte,c.verdeClaro,100,10,"",-1,-1,530,400,-1)

		#Para la imagen del usuario
		foto(self,"paquete/img/usuario.png",680,100,250,250)

	def cerrar(self):
		self.master.destroy()
		self.master.master.deiconify()		

class Inicio(ctk.CTkToplevel):
	def __init__(self):
		super().__init__()
		self.geometry(c.dimensiones)
		self.title("Vigilante")

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

