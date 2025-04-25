"""
EJERCICIO 1

APLANAR UNA LISTA
"""
# lst = [[1, 2], [3, 4], [5, 6], [7, 8]]
# lst2 = [1, 2, 3, 4, 5, 6, 7, 8]

# lst_resultado = []
# for elem in lst:
#     for num in elem:
#         lst_resultado.append(num)

# print(lst_resultado)

"""
EJERCICIO 2

ENCONTRAR EL NUMERO MAYOR Y EL NUMERO MENOR
"""

# lst = [3, 5, 20, 9, 1, 50, 10, 100]
# res = [1, 100]

# nmenor, nmayor = lst[0], lst[0]

# for num in lst:
#     if num > nmayor:
#         nmayor = num
    
#     if num < nmenor:
#         nmenor = num

# print(nmenor, nmayor)


"""
CREAR UNA FUNCION QUE, AL INGRESAR UNA LISTA CON n RADIOS DE CIRCULO,
DEVUELVA LAS n ÁREAS

ENTRADA: [1, 2, 3, 4]
SALIDA: [1**2*pi 2**2*pi ...]
"""
from math import pi

def calc_areas(lst):
    lst_areas = []
    for elem in lst:
        area = elem**2*pi
        lst_areas.append(area)
    return lst_areas



"""
CREAR UNA FUNCION QUE, DADA UNA STRING, DEVUELVA LA CANTIDAD
DE VOCALES QUE HAYA EN ELLA.

ENTRADA: 'KAMATACHUKY'
SALIDA: 4
"""

def count_vocals(palabra):
    vocal = 'aeiouAEIOU'
    contador = 0
    for letra in palabra:
        if letra in vocal:
            contador += 1
    return contador


"""
CREAR UNA FUNCION QUE, DADO UN NUMERO, RETORNE True SI ES PRIMO
O False SI NO ES PRIMO.
"""
def es_primo(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True


"""
[2, 6, 9, 10]
[True, False, False, True]
"""

def primos(lista_numeros):
    result = []
    for num in lista_numeros:
        if num <= 2:
            result.append(True)
            continue

        for i in range(2, num):
            if num%i == 0:
                result.append(False)
                break
        
        else:
            result.append(True)
    
    return result


contador = 0
while True:
    contador += 1
    print(contador)

    if contador == 100:
        break