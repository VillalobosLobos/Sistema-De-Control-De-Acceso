import customtkinter as ctk
import requests

class MiFrame(ctk.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

		#Para las etiquetas de texto
		self.titulo = ctk.CTkLabel(
			self,
			text="Inicio de sesión",
			font=("Impact",80))
		self.titulo.grid(row=0,column=2,padx=20,pady=20,sticky="ew")

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
inicio.resizable(False,False)
inicio.mainloop()


