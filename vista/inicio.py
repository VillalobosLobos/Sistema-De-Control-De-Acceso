import customtkinter as ctk
from utilidades import utilidades as u
import requests

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		#Para las etiquetas de texto
		#agregarEtiqueta()root,texto,colorLetra,tamaño,fila,columna,x,y,s)
		u.agregarEtiqueta(self,"Inicio de sesión","white",80,0,1,20,20,"ew")
		u.agregarEtiqueta(self,"Usuario","white",40,2,1,20,20,"w")
		u.agregarEtiqueta(self,"Contraseña","white",40,3,1,20,20,"w")

		#Para agregar un campo de texto
		#agregarCampo(root,txt,altura,ancho,tam,fila,columna,x,y,s)
		u.agregarCampo(self,"Ingrese su usuario",50,320,30,2,1,20,20,"e")
		u.agregarCampoContraseña(self,"Ingrese su contraseña",50,320,30,3,1,20,20,"e")

		#Para agregar botones
		#def agregarBoton(root,txt,tam,colorFondo,colorHover,ancho,radio,fila,columna,x,y)
		u.agregarBoton(self,"Ingresar",40,"#044b29","#03b25f",300,9,4,1,20,20)

class Inicio(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.geometry("1090x650")
		self.title("CET1 Walter Cross Buchanan")

		#Agregando nuestro frame
		self.mi_frame=MiFrame(master=self)
		self.mi_frame.configure(fg_color="#058749")
		self.mi_frame.grid(row=0,column=0,padx=20,pady=20,sticky="nsew")

		self.grid_rowconfigure(0,weight=1) #Fila 0 ocupara más espacio
		self.grid_columnconfigure(0,weight=1) #Columna 0 ocupara más espacio

inicio=Inicio()
inicio.configure(fg_color="white")
#inicio.resizable(False,False)
inicio.mainloop()


