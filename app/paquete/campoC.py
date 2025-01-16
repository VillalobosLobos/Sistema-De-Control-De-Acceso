from paquete import configuraciones as c
import customtkinter as ctk

def campoC(root,txt,altura,ancho,tam,fila,columna,x,y,s):
	campo=ctk.CTkEntry(
		root,
		placeholder_text=txt,
		height=altura,
		width=ancho,
		font=(c.fuente,tam),
		bg_color=c.verde,
		show="*")

	if fila==-1 or columna==-1:
		campo.place(x=x,y=y)
	else:
		campo.grid(row=fila,column=columna,padx=x,pady=y,sticky=s)
	return campo
	

