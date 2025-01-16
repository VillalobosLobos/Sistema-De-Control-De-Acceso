from paquete import configuraciones as c
import customtkinter as ctk

def agregarBoton(root,txt,tam,colorFondo,colorHover,ancho,radio,comando,fila,columna,x,y,s):
	boton=ctk.CTkButton(
			root,
			text=txt,
			font=(c.fuente,int(tam)),
			fg_color=colorFondo,
			hover_color=colorHover,
			width=ancho,
			corner_radius=radio,
			command=comando)
	if s==-1:
		boton.place(x=x,y=y)
	else:
		boton.grid(row=int(fila),column=int(columna),padx=int(x),pady=int(y),sticky=s)

