# Crear un nuevo archivo
with open("my_notes.txt", "w") as file:
    # Escribiendo tres líneas de notas personales
    file.write("Nota 1: Mi nombre es Patricio Bustamante.\n")
    file.write("Nota 2: Estoy estudiando Ingeniería en TI.\n")
    file.write("Nota 3: Soy hincha del Deportivo Quito.\n")

# Abrir el archivo para leer su contenido
with open("my_notes.txt", "r") as file:
    # Leer y mostrar cada línea
    line = file.readline()  # Leer la primera línea
    while line:  
        print(line.strip())  # Mostrar la línea
        line = file.readline()  # Leer la siguiente línea

    # Verificar si el archivo está cerrado
    if file.closed:
        print("El archivo está cerrado.")
    else:
        print("El archivo sigue abierto.")
