import customtkinter as ctk
from PIL import Image
from .imagenes import agregarImagen as img
import configuraciones as c

def foto(self,ruta,posx,posy,x,y):
	botonAtras=ctk.CTkButton(
			master=self,
			text="",
			image=img(ruta,x,y),
			#command=self.cerrar,
			fg_color=c.verde,
			hover_color=c.verde,
			width=x,
			height=y,
			corner_radius=10)

	botonAtras.place(x=posx,y=posy)
