from flask import Flask, request
import mysql.connector
from flask import jsonify

coneccion=mysql.connector.connect(
	host="localhost",
	user="villalobos",
	password="root",
	database="cet1"
)

cursor=coneccion.cursor()

app = Flask(__name__)


@app.route('/')
def index():
	return "Servidor vivo"

@app.route('/info/<int:boleta>',methods=['GET'])
def info(boleta):
	'''
	Función para obtener la información del alumno usando su boleta
	Parametros:
		int: boleta

	Valor de regreso:
		json: salida
	'''
	cursor=coneccion.cursor()
	cursor.execute("SELECT * FROM alumnos where boleta=%s;",(boleta,))

	resultados = cursor.fetchall()
	cursor.close()

	salida={
		"boleta":resultados[0][0],
		"nombre":resultados[0][1],
		"grupos":resultados[0][2],
		"turno":resultados[0][3],
		"especialidad":resultados[0][4],
		"estado":resultados[0][5],
		"foto":resultados[0][6]
	}

	return jsonify(salida)

@app.route('/infoUsuario/<string:usuario>',methods=['GET'])
def infoUsuario(usuario):
	'''
	Función para obtener la información del usuario usando su usuario
	Parametros:
		String : usuario

	Valor de regreso:
		json: salida
	'''
	cursor=coneccion.cursor()
	cursor.execute("SELECT * FROM usuarios where usuario=%s;",(usuario,))

	resultados = cursor.fetchall()
	cursor.close()

	salida={
		"usuario":resultados[0][0],
		"turno":resultados[0][2],
	}

	return jsonify(salida)


@app.route('/altaAlumno',methods=['POST'])
def altaAlumno():
	'''
	Función para agregar a un alumno a la BD
	Parametros:
		Ninguno
	Valor de retorno:
		string: "Regristro exitoso"
	'''
	info=request.json
	boleta=info.get('boleta')
	nombre=info.get('nombre')
	grupos=info.get('grupos')
	turno=info.get('turno')
	especialidad=info.get('especialidad')
	estado=info.get('estado')
	foto=info.get('foto')

	cursor=coneccion.cursor()
	cursor.execute("insert into alumnos (boleta, nombre, grupos, turno, especialidad, estado,foto) values (%s, %s, %s, %s, %s, %s, %s);",(boleta,nombre,grupos,turno,especialidad,estado,foto))
	coneccion.commit()
	cursor.close()
	
	return "Registro exitoso"

@app.route('/altaUsuario',methods=['POST'])
def altaUsuario():
	'''
	Función para agregar a un usuario a la BD
	Parametros:
		Ninguno
	Valor de retorno:
		string: "Regristro exitoso"
	'''
	info=request.json
	usuario=info.get('usuario')
	contraseña=info.get('contraseña')
	turno=info.get('turno')

	cursor=coneccion.cursor()
	cursor.execute("insert into usuarios (usuario, contraseña, turno) values (%s, %s, %s);",(usuario,contraseña,turno))
	coneccion.commit()
	cursor.close()
	
	return "Registro exitoso"

@app.route('/actualizarAlumno',methods=['POST'])
def actualizarAlumno():
	'''
	Función para actualiar a los alumnos dentro de la BD
	Parametros:
		Ninguno
	Valor de retorno:
		string:"Actualización exitosa"
	'''
	info=request.json
	boleta=info.get('boleta')
	nombre=info.get('nombre')
	grupos=info.get('grupos')
	turno=info.get('turno')
	especialidad=info.get('especialidad')
	#estado=info.get('estado')
	foto=info.get('foto')

	cursor=coneccion.cursor()
	cursor.execute("update alumnos set boleta=%s, nombre=%s, grupos=%s, turno=%s, especialidad=%s,foto=%s where boleta=%s",(boleta,nombre,grupos,turno,especialidad,foto,boleta))
	coneccion.commit()
	cursor.close()
	
	return "Actualización exitosa"

@app.route('/actualizarUsuario',methods=['POST'])
def actualizarUsuario():
	'''
	Función para actualiar a los usuarios dentro de la BD
	Parametros:
		Ninguno
	Valor de retorno:
		string:"Actualización exitosa"
	'''
	info=request.json
	usuario=info.get('usuario')
	turno=info.get('turno')
	
	cursor=coneccion.cursor()
	cursor.execute("update usuarios set usuario=%s, turno=%s where usuario=%s",(usuario,turno,usuario))
	coneccion.commit()
	cursor.close()
	
	return "Actualización exitosa"

@app.route('/eliminarAlumno/<int:boleta>',methods=['DELETE'])
def eliminarAlumno(boleta):
	'''
	Función para eliminar de la BD a un alumno
	Parametros:
		Ninguno
	Valor de retorno:
		string: "Se a eliminado correctamente"
	'''
	cursor=coneccion.cursor()
	cursor.execute("delete from  alumnos where boleta=%s;",(boleta,))
	coneccion.commit()
	cursor.close()

	return "Se a eliminado \ncorrectamente"

@app.route('/eliminarUsuario/<string:usuario>',methods=['DELETE'])
def eliminarUsuario(usuario):
	'''
	Función para eliminar de la BD a un usuario
	Parametros:
		Ninguno
	Valor de retorno:
		string: "Se a eliminado correctamente"
	'''
	cursor=coneccion.cursor()
	cursor.execute("delete from  usuarios where usuario=%s;",(usuario,))
	coneccion.commit()
	cursor.close()

	return "Se a eliminado\ncorrectamente"

@app.route('/registrarAlumno/<boleta>/<estado>',methods=['GET'])
def registrarAlumno(boleta,estado):
	'''
	Función para registrar si el alumno está dentro o afuera del plantel
	Parametros:
		int:boleta
		string:estado
	Valor de retorno:
		string: "Estado cambiado"
	'''
	cursor=coneccion.cursor()
	cursor.execute("update alumnos set estado=%s where boleta=%s;",(estado,boleta))
	coneccion.commit()
	cursor.close()

	return "Estado cambiado"

@app.route('/login', methods=['POST'])
def login():
	'''
	Función para el login del sistema
	Parametros:
		Ninguno
	Valor de regreso:
		string
	'''
	info=request.json
	usuario=info.get('usuario')
	contraseña=info.get('contraseña')

	cursor=coneccion.cursor()	
	cursor.execute("select contraseña from usuarios where usuario=%s;",(usuario,))
	resultado=cursor.fetchone()
	cursor.close()

	if resultado is None:
		return "Error al ingresar"
	elif resultado[0]==contraseña:
		return "Correcto"
	else:
		return "Error al ingresar"

if __name__ == '__main__':
    app.run(port=8000,debug=True)

