import requests
from versiculo import pasajeBiblico_Traducido, Pasajes_de_respuesta_a_fallas
from Api import urlSlack

if pasajeBiblico_Traducido : 
    mensaje = pasajeBiblico_Traducido
else :
    mensaje = Pasajes_de_respuesta_a_fallas


def mensajeSlack (mensaje) :
    url = urlSlack
    respuestaSlack = requests.post(url,json=({"text": mensaje}))
mensajeSlack(mensaje)






