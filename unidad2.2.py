# Práctica 1: Ordenar una lista de precios de menor a mayor
precios = [43, 57, 92, 20, 37, 5, 9]  # Se define una lista de precios
precios.sort()  # Se ordena la lista de precios en orden ascendente
print(precios)  # Se imprime la lista ordenada

"""
# Práctica 2 y 3: Crear una lista de asignaturas y un mensaje
w = ["matematicas"]  # Lista que contiene la asignatura de matemáticas
e = ["humanidades"]  # Lista que contiene la asignatura de humanidades
r = ["ingles"]  # Lista que contiene la asignatura de inglés
t = ["programacion "]  # Lista que contiene la asignatura de programación
y = ["metodologia"]  # Lista que contiene la asignatura de metodología
u = ["estoy cursando"]  # Lista que contiene un mensaje sobre el curso
# Se crea una nueva lista combinando los elementos de las listas anteriores
o = (u + w + u + e + u + r + u + t + u)
print(o)  # Se imprime la lista combinada
"""

"""
# Práctica 4: Solicitar calificaciones del usuario
a = int(input('ingresa calificacion de mate '))  # Se solicita y almacena la calificación de matemáticas
b = int(input("ingresa calificacion de ingles"))  # Se solicita y almacena la calificación de inglés
c = int(input("ingresa calificacion de humanidades"))  # Se solicita y almacena la calificación de humanidades
d = int(input("ingresa calificacion de metodologia"))  # Se solicita y almacena la calificación de metodología
e = int(input("ingresa calificacion de programacion"))  # Se solicita y almacena la calificación de programación
# Se imprimen las calificaciones ingresadas por el usuario
print("tu calificacion de mates es", a)
print("tu calificacion de ingles es", b)
print("tu calificacion de metodologia es", c)
print("tu calificacion de humanidades es", d)
print("tu calificacion de programacion es", e)
"""

"""
# Práctica 5: Ingresar números ganadores de la lotería y ordenarlos
print("")  # Imprime una línea en blanco
print("castruita soto emmanuel")  # Imprime un nombre
print("")  # Imprime otra línea en blanco
lista = []  # Se define una lista vacía para almacenar los números ganadores
# Se solicita al usuario que ingrese los números ganadores
numero1 = input("ingresa el primer numero ganador de la loteria")  # Primer número
num1 = int(numero1)  # Convierte el primer número a entero
lista.append(num1)  # Agrega el primer número a la lista
numero2 = input("ingresa el segundo numero ganador de la loteria")  # Segundo número
num2 = int(numero2)  # Convierte el segundo número a entero
lista.append(num2)  # Agrega el segundo número a la lista
numero3 = input("ingresa el 3 numero ganador de la loteria")  # Tercer número
num3 = int(numero3)  # Convierte el tercer número a entero
lista.append(num3)  # Agrega el tercer número a la lista
lista.sort()  # Ordena la lista de números ganadores
print("los numeros quedan en el siguiente orden")  # Mensaje indicando que se van a mostrar los números ordenados
print(lista)  # Imprime la lista ordenada de números
