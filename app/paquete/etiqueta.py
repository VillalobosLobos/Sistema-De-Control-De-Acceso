import customtkinter as ctk
import configuraciones as c

def agregarEtiqueta(root,txt,color,tam,fila,columna,x,y,s):
	etiqueta=ctk.CTkLabel(
			root,
			text=txt,
			text_color=color,
			font=(c.fuente,tam),
			bg_color=c.verde)

	if fila==-1 or columna==-1:
		etiqueta.place(x=x,y=y)
	else:
		etiqueta.grid(row=fila,column=columna,padx=x,pady=y,sticky=s)

