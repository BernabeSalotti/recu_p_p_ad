from funciones_parcial import *
estudiantes = ["ana","bruno","carla","diego"]
calificaciones = [
    #mate, historia, biologia
    [9, 8, 10],  #Ana
    [6, 7, 8],   #Bruno
    [10, 10, 9], #Carla
    [7, 6, 5]      #Diego
]

separador = "----------------------------------"
seguir = "s"
while seguir == "s":
    opcion = 0
    while opcion <1 or opcion >6:
        print('\n---------MENU DE OPCIONES---------\n ' \
        '1. Mostrar la lista de los estudiantes y sus notas \n ' \
        '2. Ordenar estudiantes de mayor a menor segun su promedio \n ' \
        '3. Buscar estudiante por nombre y mostrar sus calificaciones \n ' \
        '4. Buscar una calificación y mostrar a qué estudiante y materia pertenece \n ' \
        '5. Salir')
        opcion = int(input('\n-Ingrese una de las opciones segun su numeracion (1-5): '))
        
    if opcion == 1:
        print(separador)
        mostrar_estudiantes_y_calificaciones(estudiantes,calificaciones)
        print(separador)

    elif opcion ==2:
        print(separador)
        ordenar_may_men_promedio(estudiantes,calificaciones)
        print(separador)

    elif opcion ==3:
        print(separador)
        buscar_estudiante(estudiantes,calificaciones)
        print(separador)
        
    elif opcion ==4:
        print(separador)
        buscar_calificacion(estudiantes,calificaciones)
        print(separador)   

    elif opcion == 5:
        seguir = "n"

print('programa terminado, ¡¡Adios!!')


