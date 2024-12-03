import customtkinter as ctk

def agregarEtiqueta(root,txt,color,tam,fila,columna,x,y,s):
	etiqueta=ctk.CTkLabel(
		root,
		text=txt,
		text_color="white",
		font=("Impact",int(tam)))
	etiqueta.grid(row=int(fila),column=int(columna),padx=int(x),pady=int(y),sticky=s)

def agregarCampo(root,txt,altura,ancho,tam,fila,columna,x,y,s):
	campo=ctk.CTkEntry(
		root,
		placeholder_text="Ingrese usuario",
		height=int(altura),
		width=int(ancho),
		font=("Impact",int(tam)))
	campo.grid(row=int(fila),column=int(columna),padx=int(x),pady=int(y),sticky=s)

def agregarCampoContraseña(root,txt,altura,ancho,tam,fila,columna,x,y,s):
	campo=ctk.CTkEntry(
		root,
		placeholder_text="Ingrese usuario",
		height=int(altura),
		width=int(ancho),
		font=("Impact",int(tam)),
		show="*")
	campo.grid(row=int(fila),column=int(columna),padx=int(x),pady=int(y),sticky=s)





