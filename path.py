import json
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_PATH, "words.json")

words = {}  # Almacenará los datos

def load_words():
    """
    Carga las palabras que existen en el archivo json.
    """
    # Comprobar si el archivo existe
    if not os.path.exists(JSON_PATH):
        return {}

    # Comprobar si el archivo está vacío
    file_size = os.path.getsize(JSON_PATH)
    if file_size == 0:
        return {}

    # Leer el contenido del archivo
    with open(JSON_PATH, "r", encoding='utf-8') as j:
        content = j.read()

    # Verificar si el contenido no está vacío
    if not content:
        return {}

    # Comprobar si el contenido es un JSON válido
    if content[0] == '{' and content[-1] == '}':
        # Intentar convertir el contenido en un diccionario
        return json.loads(content)
    
    return {}

def save_words(new_words):
    """
    Guarda el diccionario de palabras en el archivo json.
    """
    with open(JSON_PATH, "w", encoding='utf-8') as f:
        json.dump(new_words, f, indent=2, ensure_ascii=False)

# Cargar palabras existentes al iniciar
words = load_words()