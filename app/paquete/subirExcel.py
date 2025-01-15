from .alerta import alerta
import pandas as pd
import requests
import json

def subirExcel(ruta):
	df=pd.read_excel(ruta)

	for index, row in df.iterrows():
		boleta=row['BOLETA']
		nombre=f"{row['APELL_PATERNO']} {row['APELL_MATERNO']} {row['NOMBRE']}"
		grupos=row['GRUPO']
		turno=row['TURNO']
		especialidad="Pendiende"
		estado="false"
		foto=f"{row['BOLETA']}.jpg"

		datos={
			"boleta":boleta,
			"nombre":nombre,
			"grupos":grupos,
			"turno":turno,
			"especialidad":especialidad,
			"estado":estado,
			"foto":"fotos/"+str(boleta)+".jpg"
		}

		try:
			response=requests.post("http://127.0.0.1:8000/altaAlumno",json=datos)
		except requests.exceptions.ConnectionError as e:
			alerta("No hay conexión\ndel servidor")

		#comando=f"insert into alumnos (boleta, nombre, grupos, turno, especialidad, estado,foto) values ({boleta},{nombre},{grupos},{turno},{especialidad},{estado},{foto});"
		#print(comando)


