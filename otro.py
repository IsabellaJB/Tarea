import numpy


def funcion_objetivo(arreglo):
    x = arreglo[0] 
    y = arreglo[1]
    operacion = ((x**2 + y - 11)**2) + ((x + y**2 - 7)**2)
    return operacion


prueba = [1,1]
deltaX = 0.01


def combinacion(x, delta, funcion):
    derivadas2 = []
    lista8 = []
    for i in range (0, len(x)):
        valor1 = 0
        valor2 = 0
        valor3 = 0
        valor_final = 0
        
        copia = x.copy()
        copia[i] = x[i] + delta
        valor1 = funcion(copia)
        valor2 = 2*(funcion(x))
        copia[i] = x[i] - delta
        valor3 = funcion(copia)
        valor_final = (valor1 - (valor2) + valor3) / (delta**2)
        lista8.append(valor_final)

        print(lista8)
        lista = []
        lista2 = []
        lista3 = []
        lista4 = []
        for j in range(len(x)):
            
            parte_uno_uno = (x[i]+delta)
            parte_uno_dos = (x[j]+delta)
            lista.append(parte_uno_uno)
            lista.append(parte_uno_dos)
            v1 = funcion(lista)
            # print(v1)



            parte_dos_uno = (x[i] + delta)
            parte_dos_dos = (x[j] - (delta))
            lista2.append(parte_dos_uno)
            lista2.append(parte_dos_dos)
            v2 = funcion(lista2)

        

            parte_tres_uno = (x[i]-delta)
            parte_tres_dos = (x[j]+delta)
            lista3.append(parte_tres_uno)
            lista3.append(parte_tres_dos)
            v3 = funcion(lista3)

            parte_cuatro_uno = (x[i]-delta)
            parte_cuatro_dos = (x[j]-delta)
            lista4.append(parte_cuatro_uno)
            lista4.append(parte_cuatro_dos)
            v4 = funcion(lista4)

        v_f = (v1 - (v2) - (v3) + v4) / (4*delta*delta)
        lista8.append(v_f)
        print(lista8)
        print("\n")
    # derivadas2.append(lista8)
    return derivadas2






print(combinacion(prueba, deltaX,funcion_objetivo))






