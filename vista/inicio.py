import customtkinter
from PIL import Image
import requests

class MiFrame(customtkinter.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)

        	#Para los logos del ipn y cet1
		self.cet1 = customtkinter.CTkImage(
			light_image=Image.open("./img/cet1.png"),
			dark_image=Image.open("./img/cet1.png"),
			size=(180,200))
		self.cet1Label = customtkinter.CTkLabel(
			self,
			image=self.cet1,
			text="")
		self.cet1Label.grid(row=0,column=0,padx=20,pady=20,sticky="ew")

		self.ipn = customtkinter.CTkImage(
			light_image=Image.open("./img/ipn.png"),
			dark_image=Image.open("./img/ipn.png"),
			size=(150,200))
		self.ipnLabel = customtkinter.CTkLabel(
			self,
			image=self.ipn,
			text="")
		self.ipnLabel.grid(row=0,column=2,padx=20,pady=20,sticky="ew")

        #Para las etiquetas de texto
		self.titulo = customtkinter.CTkLabel(
			self,
			text="Inicio de sesion",
			font=("Impact",80))
		self.titulo.grid(row=0,column=1,padx=20,pady=20,sticky="ew")

		self.usuario = customtkinter.CTkLabel(
			self,
			text="        Usuario",
			font=("Impact",40))
		self.usuario.grid(row=2,column=1,padx=20,pady=20,sticky="w")

		self.contraseña = customtkinter.CTkLabel(
			self,
			text="Contraseña",
			font=("Impact",40))
		self.contraseña.grid(row=3,column=1,padx=20,pady=20,sticky="w")

        #Para los campos de texto
		self.CampoUsuario = customtkinter.CTkEntry(
			self,
			placeholder_text="Ingrese su usuario",
			height=50,
			width=320,
			font=("Impact",30))
		self.CampoUsuario.grid(row=2,column=1,padx=20,pady=20,sticky="e")

		self.CampoContraseña = customtkinter.CTkEntry(
			self,
			placeholder_text="Ingrese su contraseña",
			height=50,
			width=320,
			font=("Impact",30),
			show="*")
		self.CampoContraseña.grid(row=3,column=1,padx=20,pady=20,sticky="e")

		self.boton=customtkinter.CTkButton(
			self,
			text="Ingresar",
			font=("Impact",40),
			fg_color="#044b29",
			hover_color="#03b25f",
			width=300,
			corner_radius=9,
			command=self.ingresar)
		self.boton.grid(row=4,column=1,padx=20,pady=20)

	def ingresar(self):
		usuario=self.CampoUsuario.get()
		contraseña=self.CampoContraseña.get()

		url='http://localhost:8000/login'
		data={
			"usuario":usuario,
			"contraseña":contraseña
		}

		response=requests.post(url,json=data)

		if response.text=="Correcto" and usuario[0]=='V':
			ventana=Vigilante(usuario,contraseña)
		elif response.text=="Correcto" and usuario[0]=='A':
			ventana=Administrador(usuario,contraseña)

class Inicio(customtkinter.CTk):
	def __init__(self):
		super().__init__()
		self.geometry("1090x650")
		self.title("CET1 Walter Cross Buchanan")

        	#Creando nuestro Frame verde
		self.mi_frame=MiFrame(master=self)
		self.mi_frame.configure(fg_color="#058749")
		self.mi_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

		self.grid_rowconfigure(0,weight=1) #Fila 0 ocupara más espacio
		self.grid_columnconfigure(0,weight=1) #Columna 0 ocupara más espacio

inicio=Inicio()
inicio.configure(fg_color="white")
inicio.resizable(False,False)
inicio.mainloop()


