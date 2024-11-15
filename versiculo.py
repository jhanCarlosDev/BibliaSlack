import requests
import re
from deep_translator import GoogleTranslator
from Api import Api_key
from  citasBiblica import citas_biblicas_aleatorias

url = f"https://api.esv.org/v3/passage/text/?q={citas_biblicas_aleatorias}"

                                    
headers = {
  "Authorization": f"{Api_key}"
}

pasajeBiblico_Traducido = ""

Pasajes_de_respuesta_a_fallas = """
  Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito,
  para que todo aquel que en él cree, no se pierda, mas tenga vida eterna.
  """

try : 
  response = requests.get(url, headers=headers)

  if response.status_code == 200 :
    Datos = response.json()
    pasaje = Datos["passages"][0] 
    pasaje_Biblico =  re.sub(r'\[\d+\]|\(ESV\)', '', pasaje).strip()
    pasajeBiblico_Traducido = GoogleTranslator(source="en", target="es").translate(pasaje_Biblico)
  else : 
    Pasajes_de_respuesta_a_fallas

except :
  print("Error en la ejecucion")















