from fpdf import FPDF
import os

class pdf():
	def __init__(self,titulo,info):
		self.info=info

		self.ruta_descargas = self.obtener_ruta_descargas()
		archivo_salida = os.path.join(self.ruta_descargas, titulo)

		self.pdf=FPDF(orientation='P',unit='mm',format='A4')
		self.pdf.add_page()

		self.fuente('helvetica','B',20)

		self.imagen("paquete/img/ipn.png",10,10,25)
		self.imagen("paquete/img/cet1.png",170,10,30)

		self.texto("Instituto Politécnico Nacional")
		self.texto("Centro de Estudios Tecnológicos")
		self.texto("No. 1")
		self.texto("\"Walter Cross Buchanan\"")

		self.fuente("helvetica","",16)
		
		self.pdf.ln(20)
		self.texto("Este fue el registro de entradas y salidas de los alumnos dentro del plantel:")

		self.tabla()

		self.pdf.ln(10)
		self.fuente('helvetica','',10)
		self.texto('Esta fue la información recopilada hasta el momento')

		self.pdf.output(archivo_salida)
	
	def fuente(self,fuente,estilo,tamaño):
		self.pdf.set_font(fuente,style=estilo,size=tamaño)

	def imagen(self,ruta,posx,posy,dimensiones):
		self.pdf.image(ruta,x=posx,y=posy,w=dimensiones)
	
	def texto(self,txt):
		self.pdf.cell(0,10,txt,ln=True,align="C")
	
	def obtener_ruta_descargas(self):
	    carpeta_usuario = os.path.expanduser("~")
	    ruta_downloads = os.path.join(carpeta_usuario, "Downloads")
	    ruta_downloads = os.path.join(carpeta_usuario, "Descargas")
	    if os.path.exists(ruta_downloads):
	        return ruta_downloads
	    elif os.path.exists(ruta_descargas):
	        return ruta_descargas
	        
	    

	def tabla(self):
		titulos=["Boleta","Estado del alumno","hora de entrada/salida"]
		#Para agregar los encabezados
		self.pdf.ln()
		for titulo in titulos:
			self.pdf.cell(60,10,titulo,1,0,'C')
		self.pdf.ln()

		#Para agregar el contenido a la tabla
		for i in self.info:
			for datos in i:
				self.pdf.cell(60,10,str(datos),1,0,'C')
			self.pdf.ln()
		self.pdf.ln()

#doc=pdf()

