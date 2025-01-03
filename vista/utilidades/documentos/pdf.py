from fpdf import FPDF

class pdf():
	def __init__(self):
		self.pdf=FPDF(orientation='P',unit='mm',format='A4')
		self.pdf.add_page()

		self.fuente('helvetica','B',20)

		self.imagen("ipn.png",10,10,25)
		self.imagen("cet1.png",170,10,30)

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

		self.pdf.output('hola.pdf')
	
	def fuente(self,fuente,estilo,tamaño):
		self.pdf.set_font(fuente,style=estilo,size=tamaño)

	def imagen(self,ruta,posx,posy,dimensiones):
		self.pdf.image(ruta,x=posx,y=posy,w=dimensiones)
	
	def texto(self,txt):
		self.pdf.cell(0,10,txt,ln=True,align="C")

	def tabla(self):
		titulos=["Boleta","hora de entrada","hora de salida"]
		info=[
			["boleta1","10:15","14:30"],
			["boleta2","10:15","14:30"],
			["boleta3","10:15","14:30"],
			["boleta4","10:15","14:30"],
			["boleta5","10:15","14:30"],
			["boleta6","10:15","14:30"],
			["boleta7","10:15","14:30"],
			["boleta8","10:15","14:30"],
			["boleta9","10:15","14:30"],
			["boleta10","10:15","14:30"],
			["boleta11","10:15","14:30"],
			["boleta12","10:15","14:30"],
			["boleta13","10:15","14:30"],
			["boleta14","10:15","14:30"],
			["boleta15","10:15","14:30"],
			["boleta16","10:15","14:30"],
			["boleta17","10:15","14:30"],
			["boleta18","10:15","14:30"]
		]
		#Para agregar los encabezados
		self.pdf.ln()
		for titulo in titulos:
			self.pdf.cell(60,10,titulo,1,0,'C')
		self.pdf.ln()

		#Para agregar el contenido a la tabla
		for i in info:
			for datos in i:
				self.pdf.cell(60,10,datos,1,0,'C')
			self.pdf.ln()
		self.pdf.ln()

doc=pdf()

