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
		etiqueta(self,"Registro de entrada y salida","white",50,0,1,20,20,"w")

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

inicio=Inicio()
inicio.configure(fg_color="white")
#inicio.resizable(False,False)
inicio.mainloop()

