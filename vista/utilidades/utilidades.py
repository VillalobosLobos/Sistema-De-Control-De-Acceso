import customtkinter as ctk
from utilidades import funciones as f
from utilidades import configuraciones as c

def agregarEtiqueta(root,txt,color,tam,fila,columna,x,y,s):
	etiqueta=ctk.CTkLabel(
		root,
		text=txt,
		text_color=color,
		font=(c.fuente,int(tam)),
		bg_color=c.verde)
	if fila==-1 or fila==-1:
		etiqueta.pack(pady=y,padx=x,side=s)
	else:
		etiqueta.grid(row=int(fila),column=int(columna),padx=int(x),pady=int(y),sticky=s)

def agregarCampo(root,txt,altura,ancho,tam,fila,columna,x,y,s):
	campo=ctk.CTkEntry(
		root,
		placeholder_text=txt,
		height=int(altura),
		width=int(ancho),
		font=(c.fuente,int(tam)),
		bg_color=c.verde)
	if fila==-1 or columna==-1:
		campo.pack(pady=y,padx=x,side=s)
	else:
		campo.grid(row=int(fila),column=int(columna),padx=int(x),pady=int(y),sticky=s)
	return campo

def agregarCampoContraseña(root,txt,altura,ancho,tam,fila,columna,x,y,s):
	campo=ctk.CTkEntry(
		root,
		placeholder_text=txt,
		height=int(altura),
		width=int(ancho),
		font=(c.fuente,int(tam)),
		show="*")
	campo.grid(row=int(fila),column=int(columna),padx=int(x),pady=int(y),sticky=s)
	return campo

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
		boton.grid(row=int(fila),column=int(columna),padx=int(x),pady=int(y))
	else:
		boton.grid(row=int(fila),column=int(columna),padx=int(x),pady=int(y),sticky=s)

def agregarCampoInfo(root,txtE,txtC,color,tamE,tamC,altura,ancho,fila,columna,x,y,s):
	root.frameCampo=ctk.CTkFrame(root.frame)
	root.frameCampo.pack(pady=5,padx=10,anchor="w")
	root.frame.configure(fg_color=c.verdeFuerte)

	agregarEtiqueta(root.frameCampo,txtE,color,tamE,fila,columna,x,y,s)
	campo=agregarCampo(root.frameCampo,txtC,altura,ancho,tamC,fila,columna,x,y,s)
	return campo

def frameInfoAlumno(root):
	root.frame = ctk.CTkFrame(root)
	root.frame.grid(row=1, column=1, padx=20, pady=20, sticky="nwes")
	root.frame.configure(fg_color=c.verde)

	root.frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
	root.frame.grid_columnconfigure(0, weight=1)

	root.boleta=agregarCampoInfo(root,"Boleta","Ingrese su boleta","white",c.tamLetra,c.tamCampo,c.altura,c.anchoBoleta,-1,-1,5,10,"left")
	root.nombre=agregarCampoInfo(root,"Nombre","Nombre del alumno","white",c.tamLetra,c.tamCampo,c.altura,c.anchoNombre,-1,-1,5,10,"left")
	root.grupos=agregarCampoInfo(root,"Grupos","Grupos del alumno","white",c.tamLetra,c.tamCampo,c.altura,c.anchoGrupos,-1,-1,5,10,"left")
	root.turno=agregarCampoInfo(root,"Turno","Turno del alumno","white",c.tamLetra,c.tamCampo,c.altura,c.anchoTurno,-1,-1,5,10,"left")
	root.especialidad=agregarCampoInfo(root,"Especialidad","Carrera del alumno","white",c.tamLetra,c.tamCampo,c.altura,c.anchoEspecialidad,-1,-1,5,10,"left")
	

	agregarBoton(root,"Buscar",c.tamLetra,c.verdeFuerte,c.verdeClaro,300,9,lambda:buscarAlumno(root),2,1,350,20,"e")
	agregarBoton(root,"Registrar",c.tamLetra,c.verdeFuerte,c.verdeClaro,300,9,lambda:registrarEntrada(root),2,1,20,20,"w")

def buscarAlumno(root):
	boleta=root.boleta.get()
	informacion=f.buscar(boleta)

def registrarEntrada(root):
	boleta=root.boleta.get()
	f.registrar(boleta)









