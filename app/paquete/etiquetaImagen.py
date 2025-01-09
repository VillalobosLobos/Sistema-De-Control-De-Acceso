import customtkinter as ctk
from PIL import Image
from .imagenes import agregarImagen as img
import configuraciones as c

def etiquetaImagen(self,ruta,posx,posy,x,y):
		etiqueta=ctk.CTkLabel(
			self,
			image=img(ruta,x,y),
			text="")

		etiqueta.place(x=posx,y=posy)
