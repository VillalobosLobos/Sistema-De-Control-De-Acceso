from .imagenes import agregarImagen as img
from paquete import configuraciones as c
import customtkinter as ctk
from PIL import Image

def botonImagen(self,ruta,fila,columna,x,y,s):
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

	botonAtras.grid(row=fila,column=columna,padx=20,pady=20,sticky=s)


