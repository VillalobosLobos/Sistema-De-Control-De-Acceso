import customtkinter as ctk
import configuraciones as c
from .etiqueta import agregarEtiqueta as etiqueta
from .botonImagen import botonImagen as btimg
from .boton import agregarBoton as boton
import configuraciones as c
from .etiquetaImagen import etiquetaImagen
from .agregarAlumno import Inicio as ae
from .actualizarAlumno import Inicio as ue
from .eliminarAlumno import Inicio as ea
from .agregarUsuario import Inicio as au
from .actualizarUsuario import Inicio as uu
from .eliminarUsuario import Inicio as eu

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		#Para el botón de regreso
		btimg(self,"paquete/img/atras.png",0,0,30,30,"e")

		#Para las etiquetas de texto
		etiqueta(self,"Gestión de usuarios","white",50,-1,-1,260,20,"w")

		#Botones Alumno
		boton(self,"Agregar",30,c.verdeFuerte,c.verdeClaro,100,10,self.agregarEstudiante,-1,-1,190,320,-1)
		boton(self,"Actualizar",30,c.verdeFuerte,c.verdeClaro,100,10,self.actualizarEstudiante,-1,-1,180,380,-1)
		boton(self,"Eliminar",30,c.verdeFuerte,c.verdeClaro,100,10,self.eliminarEstudiante,-1,-1,190,440,-1)

		#Botones Administrador
		boton(self,"Agregar",30,c.verdeFuerte,c.verdeClaro,100,10,self.agregarUsuario,-1,-1,640,320,-1)
		boton(self,"Actualizar",30,c.verdeFuerte,c.verdeClaro,100,10,self.actualziarUsuario,-1,-1,630,380,-1)
		boton(self,"Eliminar",30,c.verdeFuerte,c.verdeClaro,100,10,self.eliminarUsuario,-1,-1,640,440,-1)

		#Apartado de Alumno
		etiquetaImagen(self,"paquete/img/libro.png",150,80,200,200)
		etiqueta(self,"Estudiantes","white",30,-1,-1,175,270,"w")

		#Apartado de Administrador
		etiquetaImagen(self,"paquete/img/carpeta.png",595,80,200,200)
		etiqueta(self,"Administradores","white",30,-1,-1,595,270,"w")
	
	def cerrar(self):
		self.master.destroy()
		self.master.master.deiconify()

	def agregarEstudiante(self):
		self.master.withdraw()
		ventana=ae()
		ventana.configure(fg_color="white")

	def actualizarEstudiante(self):
		self.master.withdraw()
		ventana=ue()
		ventana.configure(fg_color="white")

	def eliminarEstudiante(self):
		self.master.withdraw()
		ventana=ea()
		ventana.configure(fg_color="white")

	def agregarUsuario(self):
		self.master.withdraw()
		ventana=au()
		ventana.configure(fg_color="white")

	def actualziarUsuario(self):
		self.master.withdraw()
		ventana=uu()
		ventana.configure(fg_color="white")

	def eliminarUsuario(self):
		self.master.withdraw()
		ventana=eu()
		ventana.configure(fg_color="white")

class Inicio(ctk.CTkToplevel):
	def __init__(self):
		super().__init__()
		self.geometry(c.dimensiones)
		self.title("Administrador")

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

