from path import words, save_words, JSON_PATH

def find_word(ls, word):
    """
    Busca si una palabra está presente en la sopa de letras en cualquier dirección indicada
    Parámetros:
    ls (list[list[str]]): Matriz que representa la sopa de letras.
    word (str): El término que se intenta encontrar en la sopa de letras.
    Retorna: bool: Retorna True si la palabra está presente en la sopa de letras, de lo contrario retorna False.
    
    """
    rows, cols = len(ls), len(ls[0])
    word_len = len(word)
    npc = False
    directions = [
        (0, 1),  # Horizontal izquierda a derecha
        (0, -1), # Horizontal derecha a izquierda
        (1, 0),  # Vertical de arriba hacia abajo
        (-1, 0), # Vertical de abajo hacia arriba
        (1, 1),  # Diagonal izquierda a derecha y arriba hacia abajo
        (-1, -1),# Diagonal derecha a izquierda y abajo hacia arriba
        (1, -1), # Diagonal derecha a izquierda y arriba hacia abajo
        (-1, 1), # Diagonal izquierda a derecha y abajo hacia arriba
    ]

    def is_word_at(i, j, dir_x, dir_y):
        """
        Verifica si la palabra se encuentra en una posición específica de la sopa de letras y en una dirección dada.
        Parámetros:
        i (int): Fila inicial donde se va a verificar la palabra.
        j (int): Columna inicial donde se va a verificar la palabra.
        dir_x (int): Dirección en el eje x (horizontal o diagonal).
        dir_y (int): Dirección en el eje y (vertical o diagonal).
        Retorna: 
        bool: Retorna True si la palabra está completamente presente en la sopa de letras,siguiendo las direcciones, de lo contrario retorna False.
    
        """
        aux = True
        for k in range(word_len):
            new_i = i + k * dir_x
            new_j = j + k * dir_y
            if not (0 <= new_i < rows and 0 <= new_j < cols) or ls[new_i][new_j] != word[k]:
                aux = False
        return aux

    for i in range(rows):
        for j in range(cols):
            for dir_x, dir_y in directions:
                if is_word_at(i, j, dir_x, dir_y):
                    npc = True

    return npc


def find_words(ls, words):
    """
    Verifica si todas las palabras de una lista están presentes en la sopa de letras.
    Parámetros:
    ls (list[list[str]]): Matriz que representa la sopa de letras.
    words (list[str]): Lista de palabras a buscar en la sopa de letras.
    Retorna: 
    bool: Retorna True si todas las palabras estan presentes, False si falta al menos una.
    
    """
    count = 0
    npc = False
    for word in words:
        if find_word(ls, word):
            count += 1
    if count == len(words):
        npc = True

    return npc

def report_generator(ls, words):
    """
    Verifica si todas las palabras de una lista están presentes en la sopa de letras.
    Parámetros:
    ls (list[list[str]]): Matriz que representa la sopa de letras.
    words (list[str]):  Lista de palabras a verificar en la sopa de letras.
    Retorna: 
    Diccionario donde las claves son las palabras y los valores son True (si la palabra está presente) o False (si no lo está).
    
    """
    dictionary = {}
    for word in words:
        dictionary[word] = find_word(ls, word)

    return dictionary


def save_word(s_matrix, search_words):
    """
    Busca las palabras en la sopa de letras y guarda los resultados en el JSON
    Parámetros:
    s_matrix (list[list[str]]): Matriz que representa la sopa de letras.
    search_words (list[str]): Lista de palabras a buscar en la sopa de letras.

    Retorna: 
    Diccionario con los resultados de búsqueda de cada palabra (True o False).
    """
    # Generar el reporte de palabras encontradas
    results = report_generator(s_matrix, search_words)
    
    # Actualizar el diccionario global
    for word in search_words:
        words[word] = results[word]
    
    # Guardar los cambios en el archivo JSON
    save_words(words)
    
    return results