import customtkinter as ctk

def agregarEtiqueta(root,txt,color,tam,fila,columna,x,y,s):
	etiqueta=ctk.CTkLabel(
		root,
		text=txt,
		text_color="white",
		font=("Impact",int(tam)))
	etiqueta.grid(row=int(fila),column=int(columna),padx=int(x),pady=int(y),sticky=s)






