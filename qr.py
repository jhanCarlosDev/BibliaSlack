import qrcode
from versiculo import PasajeBiblico_Traducido
url = str({PasajeBiblico_Traducido})

qr = qrcode.QRCode(
    version = 1,
    box_size = 4,
    border = 1
)

qr.add_data(url)
qr.make(fit=True)

imagen = qr.make_image()
imagen.save("Mi_imagen.png")

