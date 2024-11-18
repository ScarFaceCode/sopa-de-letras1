- Proyecto: Sopa de Letras

- Autor
Juan Manuel Camacho Ibarguen

- Descripción del Proyecto
En este proyecto se podrá analizar una sopa de letras desde un documento de texto (input.txt), explorar un conjunto de palabras en la sopa de letras y crear un informe en forma de JSON especificando si cada palabra está presente o no.

Archivos del Proyecto
- main.py: Este archivo coordina la ejecución de un programa que lee un archivo de entrada (requirements.txt) utilizando read_input_file, procesa una matriz de búsqueda de sopa de letras y una lista de palabras, y guarda los resultados utilizando save_word_results. Maneja situaciones de error si el archivo no está presente o si sucede alguna otra excepción.
- path.py: Este archivo gestiona un diccionario de palabras almacenado en un archivo JSON. Proporciona funciones para cargar (load_words) y guardar (save_words) las palabras, asegurando que los datos persistan entre ejecuciones. Además, inicializa el diccionario words al cargar los datos existentes.
- reader.py: Este archivo lee input.txt, separa una sopa de letras en forma de matriz y una lista de palabras, y retorna ambos elementos como salida.
- soup.py: Este archivo contiene funciones para buscar palabras en una sopa de letras (find_word y find_words), generar un reporte con el estado de cada palabra (report_generator), y guardar los resultados en un archivo JSON actualizado (save_word_results), utilizando módulos externos para la gestión de datos.
- input.txt: Archivo de entrada que contiene la sopa de letras y la lista de palabras a buscar.
- words.json: Archivo de salida que contiene el reporte de las palabras encontradas y no encontradas en formato JSON.
- requirements.txt: Archivo que enumera los paquetes necesarios para ejecutar el proyecto.
