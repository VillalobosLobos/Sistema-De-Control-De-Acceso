import customtkinter as ctk
from PIL import Image
from .imagenes import agregarImagen as img
import configuraciones as c

def etiquetaImagen(self,ruta,posx,posy,x,y):
	botonAtras=ctk.CTkButton(
			master=self,
			text="",
			image=img(ruta,x,y),
			command=self.cerrar,
			fg_color=c.verdeFuerte,
			hover_color=c.verdeClaro,
			width=40,
			height=40,
			corner_radius=10)
