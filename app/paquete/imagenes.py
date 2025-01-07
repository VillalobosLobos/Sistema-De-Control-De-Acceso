import customtkinter as ctk
from PIL import Image

def agregarImagen(ruta,ancho,alto):
	imagen = ctk.CTkImage(light_image=Image.open(ruta),
			dark_image=Image.open(ruta),
			size=(ancho, alto))
	return imagen
