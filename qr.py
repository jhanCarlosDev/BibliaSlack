import qrcode
from versiculo import pasajeBiblico_Traducido,Pasajes_de_respuesta_a_fallas

if pasajeBiblico_Traducido : 
    url = pasajeBiblico_Traducido
else : 
    url = Pasajes_de_respuesta_a_fallas

def generador_Qr(url, nombre) : 
     qr = qrcode.QRCode(
           version = 1,
           box_size = 4,
           border = 1
        )
     qr.add_data(url)
     qr.make(fit=True)
     imagen = qr.make_image()
     imagen.save(nombre)

generador_Qr(url,"PasajeBiblicoQr.png")

               
    





