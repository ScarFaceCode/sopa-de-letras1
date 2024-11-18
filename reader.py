def read_input(filename="input.txt"):
    """
    Lee el archivo input.txt y separa la sopa de letras y las palabras
    Parámetros: 
    filename (str): El nombre del archivo a leer. Por defecto es "input.txt"
    Retorna:
    -soup_matrix (list): Una lista de listas, donde cada lista interna corresponde a una fila de la sopa de letras, y cada elemento de la lista interna es una letra.
    -words (list): Una lista de las palabras que deben ser buscadas en la sopa de letras.
    """
    # Abrir el archivo y leer el contenido
    with open(filename, 'r') as file:
        content = file.read().strip()
    
    # Verificar si el archivo tiene la estructura esperada
    parts = content.split('---')
    if len(parts) != 2:
        raise ValueError(f"El archivo {filename} no tiene la estructura esperada.")
    
    # Separar sopa de letras y palabras
    soup_part, words_part = parts
    soup_lines = soup_part.splitlines()
    
    # Construir la matriz de sopa de letras
    soup_matrix = [line.split() for line in soup_lines]
    
    # Procesar las palabras
    words = words_part.splitlines()

    return soup_matrix, words