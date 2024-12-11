from utilidades import utilidades as u
from utilidades import funciones as f
from utilidades import configuraciones as c
from utilidades import actualizarAlumnos as aa
import customtkinter as ctk

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		u.agregarEtiqueta(self,"Gestión de usuarios","white",50,0,1,20,20,"w")
		#Botones para la gestión de alumnos
		u.agregarBoton(self,"Actualizar alumno",c.tamLetra,c.verdeFuerte,c.verdeClaro,300,9,self.actualizarAlumno,1,0,20,20,"w")
		u.agregarBoton(self,"Eliminar alumno",c.tamLetra,c.verdeFuerte,c.verdeClaro,300,9,self.eliminarAlumno,2,0,20,20,"w")
		u.agregarBoton(self,"Agregar alumno",c.tamLetra,c.verdeFuerte,c.verdeClaro,300,9,self.agregarAlumno,3,0,20,20,"w")

		#Botones para la gestión de administradores
		u.agregarBoton(self,"Actualizar administrador",c.tamLetra,c.verdeFuerte,c.verdeClaro,300,9,self.actualizarUsuario,1,1,20,20,"w")
		u.agregarBoton(self,"Eliminar administrador",c.tamLetra,c.verdeFuerte,c.verdeClaro,300,9,self.eliminarUsuario,2,1,20,20,"w")
		u.agregarBoton(self,"Agregar administrador",c.tamLetra,c.verdeFuerte,c.verdeClaro,300,9,self.agregarUsuario,3,1,20,20,"w")

	def actualizarAlumno(self):
		f.ventanaActualizarAlumno(self.master)

	def eliminarAlumno(self):
		f.ventanaEliminarAlumno(self.master)

	def agregarAlumno(self):
		f.ventanaAgregarAlumno(self.master)

	def actualizarUsuario(self):
		f.ventanaActualizarUsuario(self.master)

	def eliminarUsuario(self):
		f.ventanaEliminarUsuario(self.master)

	def agregarUsuario(self):
		f.ventanaAgregarUsuario(self.master)

class Inicio(ctk.CTk):
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
