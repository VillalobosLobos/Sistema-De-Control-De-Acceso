import customtkinter as ctk
from utilidades import utilidades as u
from utilidades import funciones as f
from utilidades import configuraciones as c

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		#Agregando los escudos
		u.agregarImagen(self,"utilidades/img/cet1.png",c.cet1x,c.cet1y,0,2,20,20,"e")
		u.agregarImagen(self,"utilidades/img/ipn.png",c.ipnx,c.ipny,0,0,20,20,"e")

		#Para las etiquetas de texto
		u.agregarEtiqueta(self,"Inicio de sesión","white",80,0,1,20,20,"ew")
		u.agregarEtiqueta(self,"Usuario","white",40,2,1,20,20,"w")
		u.agregarEtiqueta(self,"Contraseña","white",40,3,1,20,20,"w")

		#Para agregar un campo de texto
		self.usuarioCampo=u.agregarCampo(self,"Ingrese su usuario",50,320,30,2,1,20,20,"e")
		self.contraseñaCampo=u.agregarCampoContraseña(self,"Ingrese su contraseña",50,320,30,3,1,20,20,"e")

		#Para agregar botones
		u.agregarBoton(self,"Ingresar",40,c.verdeFuerte,c.verdeClaro,300,9,self.ingresar,4,1,20,20,-1)

	def ingresar(self):
		usuario=self.usuarioCampo.get()
		contraseña=self.contraseñaCampo.get()
		f.ingresar(usuario,contraseña,self.master)

class Inicio(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.geometry(c.dimensiones)
		self.title("CET1 Walter Cross Buchanan")

		#Agregando nuestro frame
		self.mi_frame=MiFrame(master=self)
		self.mi_frame.configure(fg_color=c.verde)
		self.mi_frame.grid(row=0,column=0,padx=20,pady=20,sticky="nsew")

		self.grid_rowconfigure(0,weight=1) #Fila 0 ocupara más espacio
		self.grid_columnconfigure(0,weight=1) #Columna 0 ocupara más espacio

inicio=Inicio()
inicio.configure(fg_color="white")
#inicio.resizable(False,False)
inicio.mainloop()


