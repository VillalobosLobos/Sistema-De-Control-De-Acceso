from paquete.etiquetaImagen import etiquetaImagen as escudos
from paquete.etiqueta import agregarEtiqueta as etiqueta
from paquete.ingresar import ingresar as ingreso
from paquete.boton import agregarBoton as boton
from paquete.campo import agregarCampo as campo
import paquete.configuraciones as c
from paquete.campoC import campoC
import customtkinter as ctk

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		#Para las imagenes
		escudos(self,c.cet1,30,30,150,150)
		escudos(self,c.ipn,790,30,130,150)

		#Para las etiquetas de texto
		etiqueta(self,"Inicio de sesión","white",80,-1,-1,220,30,"ew")
		etiqueta(self,"Usuario","white",40,-1,-1,260,200,"w")
		etiqueta(self,"Contraseña","white",40,3,1,200,260,"w")

		#Para los campos de texto
		self.usuarioCampo=campo(self,"Ingrese su usuario",50,320,30,-1,-1,406,200,"e")
		self.contraseñaCampo=campoC(self,"Ingrese su contraseña",50,320,30,-1,-1,405,260,"e")

		#Para agregar botones
		boton(self,"Ingresar",40,c.verdeFuerte,c.verdeClaro,300,9,self.ingresar,-1,-1,320,350,-1)

	def ingresar(self):
		ingreso(self.usuarioCampo.get(),self.contraseñaCampo.get(),self.master)

class Inicio(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.geometry(c.dimensiones)
		self.title("CET1 Walter Cross Buchanan")

		#Agregando nuestro frame
		self.mi_frame=MiFrame(master=self)
		self.mi_frame.configure(fg_color=c.verde)
		self.mi_frame.grid(row=0,column=0,padx=20,pady=20,sticky="nsew")

		self.grid_rowconfigure(0,weight=1)
		self.grid_columnconfigure(0,weight=1)

inicio=Inicio()
inicio.configure(fg_color="white")
#inicio.resizable(False,False)
inicio.mainloop()


