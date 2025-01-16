from mysql.connector.errors import IntegrityError
from flask import Flask, request,send_file
from mysql.connector import Error
from flask import jsonify
import mysql.connector
import os

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

@app.route('/reporte', methods=['GET', 'POST'])
def reporte():
	cursor=coneccion.cursor()
	cursor.execute("SELECT boleta,estado,TIME(actualizar) AS hora FROM alumnos WHERE DATE(actualizar)=CURDATE();")
	resultados=cursor.fetchall()
	resultados_serializables = [
		{
			"boleta": fila[0],
			"estado": fila[1],
			"hora": str(fila[2])
		}
		for fila in resultados
	]

	cursor.close()
	return jsonify(resultados_serializables)

@app.route('/subirImagen/<nombre>',methods=['POST'])
def subirImagen(nombre):
	if 'imagen' not in request.files:
		return jsonify({"error": "No se envió ninguna imagen"}), 400

	imagen=request.files['imagen']
	ruta=f"./fotos/{nombre}"
	imagen.save(ruta)
	return jsonify({"mensaje": "Imagen subida correctamente", "ruta": ruta}), 200

@app.route('/imagen/<nombre>')
def imagen(nombre):
	ruta=f'fotos/{nombre}'
	try:
		return send_file(ruta,mimetype='image/jpeg')
	except FileNotFoundError:
		return {"error":"Imagen no encontrada"},404

@app.route('/info/<boleta>',methods=['GET'])
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

@app.route('/infoUsuario/<string:usuario>',methods=['GET'])
def infoUsuario(usuario):
	cursor=coneccion.cursor()
	cursor.execute("SELECT * FROM usuarios where usuario=%s;",(usuario,))

	resultados = cursor.fetchall()
	cursor.close()

	salida={
		"usuario":resultados[0][0],
		"contraseña":resultados[0][1],
		"turno":resultados[0][2],
		"rol":resultados[0][3]
	}

	return jsonify(salida)

@app.route('/altaAlumno',methods=['POST'])
def altaAlumno():
	info=request.json
	boleta=info.get('boleta')
	nombre=info.get('nombre')
	grupos=info.get('grupos')
	turno=info.get('turno')
	especialidad=info.get('especialidad')
	estado=info.get('estado')
	foto=info.get('foto')

	cursor=coneccion.cursor()
	try:
		cursor.execute("insert into alumnos (boleta, nombre, grupos, turno, especialidad, estado,foto) values (%s, %s, %s, %s, %s, %s, %s);",(boleta,nombre,grupos,turno,especialidad,estado,foto))
		coneccion.commit()
		return "Registro éxitoso"
	except IntegrityError as e:
		return "Esa boleta ya\nexiste"
	except Error as e:
			return jsonify({"error": "Error en conexión o en el SQL", "details": str(e)}), 500
	finally:
		cursor.close()

@app.route('/altaUsuario',methods=['POST'])
def altaUsuario():
	info=request.json
	usuario=info.get('usuario')
	contraseña=info.get('contraseña')
	turno=info.get('turno')
	rol=info.get('rol')

	cursor=coneccion.cursor()
	try:
		cursor.execute("insert into usuarios (usuario, contraseña, turno, rol) values (%s, %s, %s, %s);",(usuario,contraseña,turno,rol))
		coneccion.commit()
		cursor.close()
		return "Registro exitoso"
	except IntegrityError as e:
		return "Ese usuario ya\nexiste"
	except Error as e:
			return "Error en conexión\no en el SQL"
	finally:
		cursor.close()

@app.route('/actualizarAlumno',methods=['POST'])
def actualizarAlumno():
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
	info=request.json
	usuario=info.get('usuario')
	turno=info.get('turno')
	contraseña=info.get('contraseña')
	rol=info.get('rol')

	cursor=coneccion.cursor()
	cursor.execute("update usuarios set usuario=%s,contraseña=%s, turno=%s, rol=%s where usuario=%s",(usuario,contraseña,turno,rol,usuario))
	coneccion.commit()
	cursor.close()
	
	return "Actualización exitosa"

@app.route('/eliminarAlumno/<boleta>',methods=['DELETE'])
def eliminarAlumno(boleta):
	cursor=coneccion.cursor()
	cursor.execute("delete from  alumnos where boleta=%s;",(boleta,))
	coneccion.commit()
	cursor.close()
	ruta="fotos/"+str(boleta)+".jpg"

	if os.path.exists(ruta):
		os.remove("fotos/"+str(boleta)+".jpg")
	else:
		return "No existe ese\nusuario"

	return "Se a eliminado \ncorrectamente"

@app.route('/eliminarUsuario/<string:usuario>',methods=['DELETE'])
def eliminarUsuario(usuario):
	cursor=coneccion.cursor()
	cursor.execute("delete from  usuarios where usuario=%s;",(usuario,))
	coneccion.commit()
	cursor.close()

	return "Se a eliminado\ncorrectamente"

@app.route('/registrarAlumno/<boleta>/<estado>',methods=['GET'])
def registrarAlumno(boleta,estado):
	cursor=coneccion.cursor()
	cursor.execute("update alumnos set estado=%s where boleta=%s;",(estado,boleta))
	coneccion.commit()
	cursor.close()

	return "Estado cambiado"

@app.route('/login', methods=['POST'])
def login():
	info=request.json
	usuario=info.get('usuario')
	contraseña=info.get('contraseña')

	cursor=coneccion.cursor()	
	cursor.execute("select contraseña,rol from usuarios where usuario=%s;",(usuario,))
	resultado=cursor.fetchone()
	cursor.close()

	if resultado is None:
		return "Error al ingresar"
	elif resultado[0]==contraseña:
		return resultado[1]
	else:
		return "Error al ingresar"

if __name__ == '__main__':
    app.run(port=8000,debug=True)

