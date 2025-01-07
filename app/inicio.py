import customtkinter as ctk
import configuraciones as c
from paquete.etiqueta import agregarEtiqueta as etiqueta
from paquete.campo import agregarCampo as campo
from paquete.boton import agregarBoton as boton
from paquete.ingresar import ingresar as ingreso

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		#Para las etiquetas de texto
		etiqueta(self,"Inicio de sesión","white",80,0,1,20,20,"ew")
		etiqueta(self,"Usuario","white",40,2,1,20,20,"w")
		etiqueta(self,"Contraseña","white",40,3,1,20,20,"w")

		#Para los campos de texto
		self.usuarioCampo=campo(self,"Ingrese su usuario",50,320,30,2,1,20,20,"e")
		self.contraseñaCampo=campo(self,"Ingrese su contraseña",50,320,30,3,1,20,20,"e")

		#Para agregar botones
		boton(self,"Ingresar",40,c.verdeFuerte,c.verdeClaro,300,9,self.ingresar,-1,-1,310,350,-1)

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


