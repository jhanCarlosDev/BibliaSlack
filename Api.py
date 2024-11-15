
from dotenv import load_dotenv
import os

# Carga las variables del archivo .env
load_dotenv()

# Obtiene las claves API desde las variables de entorno
Api_key = os.getenv("Api_key")


