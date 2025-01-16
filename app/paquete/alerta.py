from .imagenes import agregarImagen as img
from paquete import configuraciones as c
import customtkinter as ctk

def alerta(txt):
	root=ctk.CTkToplevel()	
	root.resizable(False,False)
	root.title("")
	root.geometry("300x200")
	root.configure(fg_color=c.verdeFuerte)

	msj=ctk.CTkLabel(root,text=txt,text_color="white",font=(c.fuente,c.tamAlerta))
	msj.pack(pady=20)

	cerrar=ctk.CTkButton(root,text="Aceptar",font=(c.fuente,c.tamAlerta),fg_color=c.verde,hover_color=c.verdeClaro,command=root.destroy)
	cerrar.pack()

