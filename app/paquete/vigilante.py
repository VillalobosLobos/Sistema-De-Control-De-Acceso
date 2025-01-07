import customtkinter as ctk
import configuraciones as c
from .etiqueta import agregarEtiqueta as etiqueta
from .imagenes import agregarImagen as img
from .botonImagen import botonImagen as btimg

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		#Para el botón de regreso
		btimg(self,"paquete/img/atras.png",30,30)

		#Para las etiquetas de texto
		etiqueta(self,"Registro de entrada y salida","white",50,0,1,20,20,"w")

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

