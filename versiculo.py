import requests
import re
from deep_translator import GoogleTranslator
from Api import Api_key
from  citasBiblica import citas_biblicas_aleatorias

url = f"https://api.esv.org/v3/passage/text/?q={citas_biblicas_aleatorias}"

                                    
headers = {
  "Authorization": f"{Api_key}"
}

response = requests.get(url, headers=headers)
Datos = response.json()


pasaje = Datos["passages"][0] 
pasaje_Biblico =  re.sub(r'\[\d+\]|\(ESV\)', '', pasaje).strip()

PasajeBiblico_Traducido = GoogleTranslator(source="en", target="es").translate(pasaje_Biblico)
print(PasajeBiblico_Traducido)














