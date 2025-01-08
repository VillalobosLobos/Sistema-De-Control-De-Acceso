from .alerta import alerta
from .buscar import buscar
import requests
import json

URL="http://127.0.0.1:8000/"

def registrar(boleta):
        try:
                datos=buscar(boleta)
        except json.decoder.JSONDecodeError as e:
                alerta("No sé pudo registrar \nla entrada o salida")
        else:
                if datos==None:
                        pass
                elif datos["estado"]=="true":
                        response=requests.get(URL+"registrarAlumno/"+boleta+"/false")
                        alerta("Registro de salida\néxitoso")
                else:
                        response=requests.get(URL+"registrarAlumno/"+boleta+"/true")
                        alerta("Registro de entrada\néxitoso")
