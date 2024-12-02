from flask import Flask, request
import mysql.connector
from flask import jsonify

coneccion=mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="cet1"
)

cursor=coneccion.cursor()

app = Flask(__name__)


@app.route('/')
def index():
    return "qué hubo padrino?"

@app.route('/info/<int:boleta>',methods=['GET'])
def info(boleta):
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

@app.route('/alta',methods=['POST'])
def alta():
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
	
	return f'Registro exitoso'

@app.route('/actualizar',methods=['POST'])
def actualizar():
	info=request.json
	boleta=info.get('boleta')
	nombre=info.get('nombre')
	grupos=info.get('grupos')
	turno=info.get('turno')
	especialidad=info.get('especialidad')
	estado=info.get('estado')
	foto=info.get('foto')

	cursor=coneccion.cursor()
	cursor.execute("update alumnos set boleta=%s, nombre=%s, grupos=%s, turno=%s, especialidad=%s, estado=%s,foto=%s where boleta=%s",(boleta,nombre,grupos,turno,especialidad,estado,foto,boleta))
	coneccion.commit()
	cursor.close()
	
	return f'Actualización exitosa'

@app.route('/eliminar/<int:boleta>',methods=['DELETE'])
def eliminar(boleta):
	cursor=coneccion.cursor()
	cursor.execute("delete from  alumnos where boleta=%s;",(boleta,))
	coneccion.commit()
	cursor.close()

	return f'Se a eliminado correctamente'

@app.route('/registrar/<boleta>/<estado>',methods=['GET'])
def registrar(boleta,estado):
	cursor=coneccion.cursor()
	cursor.execute("update alumnos set estado=%s where boleta=%s;",(estado,boleta))
	coneccion.commit()
	cursor.close()

	return f'Estado cambiado'

@app.route('/login', methods=['POST'])
def login():
	info=request.json
	usuario=info.get('usuario')
	contraseña=info.get('contraseña')

	cursor=coneccion.cursor()	
	cursor.execute("select contraseña from usuarios where usuario=%s;",(usuario,))
	resultado=cursor.fetchone()
	cursor.close()

	if resultado is None:
		return f'Error al ingresar'
	elif resultado[0]==contraseña:
		return f'Correcto'
	else:
		return f'Error al ingresar'

if __name__ == '__main__':
    app.run(port=8000,debug=True)

