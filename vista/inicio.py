import customtkinter

class Inicio(customtkinter.CTk):
	def __init__(self):
		super().__init__()
		self.geometry("1090x650")
		self.title("CET1 Walter Cross Buchanan")
		self.grid_rowconfigure(0,weight=1) #Fila 0 ocupara más espacio
		self.grid_columnconfigure(0,weight=1) #Columna 0 ocupara más espacio

inicio=Inicio()
inicio.configure(fg_color="white")
inicio.resizable(False,False)
inicio.mainloop()


