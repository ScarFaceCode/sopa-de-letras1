import os
from reader import read_input
from soup import save_word

def process_files():
    """
    Verifica la existencia de 'input.txt', lee la sopa de letras y las palabras,
    y guarda los resultados de la búsqueda.
    """
    # Validar la existencia del archivo antes de procesar
    if os.path.exists('input.txt'):
        # Leer los datos del archivo
        soup_matrix, words = read_input()

        # Validar que se obtuvieron datos válidos
        if soup_matrix and words:
            save_word(soup_matrix, words)
            print("Procesamiento completado con éxito.")
        else:
            print("Error: El archivo 'input.txt' no contiene datos válidos.")
    else:
        print("Error: No se encontró el archivo 'input.txt'.")
        # Agregar un ejemplo de archivo si no existe
        create_sample_file()

def create_sample_file():
    """
    Crea un archivo de ejemplo 'input.txt' si no existe para guiar al usuario.
    """
    with open('input.txt', 'w', encoding='utf-8') as sample_file:
        sample_file.write("A B C D\nE F G H\nI J K L\nM N O P\n---\nPALABRA\nOTRA")
    print("Se creó un archivo de ejemplo llamado 'input.txt'.")

if __name__ == "__main__":
    process_files()