def mostrar_estudiantes_y_calificaciones(estudiantes: list, calificaciones: list) -> None:
    """
    funcion que se encarga de mostrar todos los estudiantes y sus calificaciones
    ----
    recibe:
    estudiantes(list): lista que contiene los nombres de los estudiantes
    calificaciones(list): lista que contiene listas con las calificaciones de lso estudiantes
    """
    print(f'{"ESTUDIANTE":^12}|{"MATEMATICA":^12}|{"HISTORIA":^12}|{"BIOLOGIA":^12}|')
    for i in range(len(calificaciones)):
        print(f'{estudiantes[i]:^12}|', end='')
        for j in range(len(calificaciones[i])):
            print(f'{calificaciones[i][j]:^12}|', end='') 
        print()

def promediar_valores (valores:list)->list:
    """
    funcion que se encarga de encontrar el promedio de las notas
    ------
    recibe:
    valores(list): lista de valores
    ---------
    retorna:
    promedios(list): es una lista con los promedios de los valoreres pasados
    """
    promedios =[]
    for i in range (len(valores)):
        suma = 0 
        contador = 0
        for j in range(len(valores[i])):
            suma += valores[i][j]
            contador += 1
        resultado = suma / contador
        resultado_convertido = int(resultado * 100) / 100
        promedios.append(resultado_convertido)
    return promedios

def ordenar_may_men_promedio (estudiantes :list, calificaciones: list)->None:
    """
    funcion que se encarga de ordenar de mayor a menor segun un parametro
    -----
    recibe:
    estudiantes(list):lista que contiene los nombres de los estudiantes
    calificaciones(list): lista que contiene listas con las calificaciones de lso estudiantes
    ------

    """
    promedios = promediar_valores(calificaciones)
    estudiantes_copia = []
    calificaciones_copia = []
    promedios_copia = []

    for i in range(len(estudiantes)):
        estudiantes_copia.append(estudiantes[i])
        calificaciones_copia.append(calificaciones[i])
        promedios_copia.append(promedios[i])

    print('---------------------------------')
    print(f'{"ESTUDIANTE":^12}|{"MATEMATICA":^12}|{"HISTORIA":^12}|{"BIOLOGIA":^12}|{"PROMEDIO":^12}|')
    while len(promedios_copia) > 0:        
        max_total = -1
        pos_max = -1

        for i in range(len(promedios_copia)):
            if promedios_copia[i] > max_total:
                max_total = promedios_copia[i]
                pos_max = i

        print(f'{estudiantes_copia[pos_max]:^12}|', end='')
        for j in range(len(calificaciones_copia[pos_max])):
            print(f'{calificaciones_copia[pos_max][j]:^12}|', end='')  
        print(f'{promedios_copia[pos_max]:^12}|')
        
        estudiantes_copia.pop(pos_max)
        calificaciones_copia.pop(pos_max)
        promedios_copia.pop(pos_max)
   
def buscar_estudiante (estudiantes: list, calificaciones: list)-> None:
    """
    funcion que se encarga de buscar un estudiante por su nombre y mostrar sus calificaciones
    -------
    recibe:
    estudiantes(list): lista que contiene los nombres de los estudiantes
    calificaciones(list): lista que contiene listas con las calificaciones de lso estudiantes

    """
    verificado = False
    print('estudiantes disponibles:')
    for nombre in estudiantes:
        print(f'{nombre}-', end='')
    print()
    estudiante_buscado = input('ingrese el nombre del estudiante que desea buscar: ').lower()  
    verificado = verificar_los_datos(estudiante_buscado, estudiantes)
    while not verificado:
        estudiante_buscado = input('¡¡ERROR!! ingrese el nombre del estudiante que desea buscar: ').lower()
        verificado = verificar_los_datos(estudiante_buscado, estudiantes)
    
    for i in range(len(estudiantes)):
        if estudiantes[i] == estudiante_buscado:
            print('----------------------------------------------------')
            print(f'{"ESTUDIANTE":^12}|{"MATEMATICA":^12}|{"HISTORIA":^12}|{"BIOLOGIA":^12}|')
            print(f'{estudiantes[i]:^12}|', end='')
            for j in range(len(calificaciones[i])):
                print(f'{calificaciones[i][j]:^12}|', end='')
            print()

def verificar_los_datos (dato, respuestas_correctas: list)-> bool:
    """""
    funcion que se encarga de verificar si un dato es correcto
    -------
    recibe:
    dato: es el dato a verificar
    respuestas_correctas(list): lista de posibles respuestas validas
    ----------
    retorna:
    existe(bool): si el dato se encuentra en la lista de respuestas correctas retoena True
    """""
    existe = False
    for respuesta in respuestas_correctas:
        if respuesta == dato:
            existe = True
    
    return existe 

def buscar_calificacion (estudiantes: list, calificaciones: list)->None:
    """
    funcion que ese encarga de buscar una calificacion y mostrar a que estudianmtes y materia pertenece
    -------
    recibe:
    estudiantes(list): lista que contiene los nombres de los estudiantes
    calificaciones(list): lista que contiene listas con las calificaciones de lso estudiantes
    """
    seguir = 's'
    while seguir == 's':
        nota_buscada = int(input('ingrese la nota que desea buscar: '))
        print('-----------------------------------------')
        calificacion_encontrada = False
        for i in range(len(calificaciones)):
            for j in range(len(calificaciones[i])):
                materia = ''
                if nota_buscada == calificaciones[i][j]:
                    if calificacion_encontrada == False:
                        print('Nota/s encontrada:\n')
                    if j == 0:
                        materia = 'matematica'
                    elif j == 1:
                        materia = 'historia'
                    else:
                        materia = 'biologia'
                    print(estudiantes[i],' |',materia,':', calificaciones[i][j],'|')
                    print('---------------------------------------------')
                    calificacion_encontrada = True
        if calificacion_encontrada == False:
            print('Nota no encontrada!')
            print('-----------------------------------')
        seguir = input('desea ingresar otra nota (s)(n):').lower()
        while seguir != 's' and seguir != 'n':
            seguir = input('desea ingresar otra nota (s)(n):').lower()   

