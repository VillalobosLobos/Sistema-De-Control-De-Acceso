from PIL import Image

def agregarImagen():
	imagen = customtkinter.CTkImage(light_image=Image.open("<path to light mode image>"),
                                  dark_image=Image.open("<path to dark mode image>"),
                                  size=(30, 30))

	etiquetaImagen = customtkinter.CTkLabel(app, image=imagen, text="")
