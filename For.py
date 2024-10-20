#1 Imprimir todos los dígitos decimales, del 0 al 9, utilizando una repetición.
# for x in range (10):
#     print (x)

#2 Imprimir todos los números entre el 100 y el 199.
# for x in range (100,200):
#     print(x)

#3 Imprimir los números entre el 5 y el 20, saltando de tres en tres.
# for x in range (5,20,3):
#     print (x)

#4 Requerir al usuario que ingrese un número entero positivo e imprimir todos los números correlativos 
# entre el ingresado por el usuario y uno menos del doble del mismo.

# n= int(input ("ingrese un número entero positivo: "))
# for x in range (n,n*2):
#     print(x)

#5 Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. En cada 
# iteración, solicitar al usuario que ingrese un número. Al finalizar, mostrar la suma de todos los números ingresados.

# c=int(input("Cantidad de números: "))
# total=0
# for variable in range(c):
#    numero=int(input("Número: "))
#    total+=numero # => total= total+numero
# print("Total de la suma:", total)


#6 Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales 
# que aparecen en esa frase (sin repetirlas).

# frase=input("Frase: ")
# print ("vocales en la frase:")
# for x in "aeiou":
#     if x in frase:
#         print(x)

#7 Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se encuentran en dicha frase.

# frase= input("ingrese una frase: " )
# Cantidad=0
# for x in frase:
#     if x in "aeiou":
#         Cantidad=Cantidad+1
# print ("Cantidad de vocales:", Cantidad)
       
#8 Escribir un programa que muestre la sumatoria de todos los números entre el 0 y el 100.

# Total=0
# for i in range(101):
#     Total=Total+i # => total=total+i
# print("sumatoria:", Total)

#9 Escribir un programa que muestre la sumatoria de todos los múltiplos de 3 encontrados entre el 0 y el 100.

# total=0
# for i in range(101):
#     if i%3 == 0:
#         total=total+i
# print("Sumatoria de los múltiplos de 3:", total)

#10 Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene 
# multiplicando todos los números enteros positivos que hay entre el 1 y ese número.

# numero=int(input("Número:"))
# f=1
# if numero!=0:
#     for i in range(1,numero+1):
#         f=f*i
# print("Factorial:", f)

#11 Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza 
# con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la 
# secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(8):
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3

#12 Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o 
# negativos. Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
#No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un 
# error si no se ingresaron números positivos.

# sumaPositivos=0
# cantidadPositivos=0
# sumaNegativos=0
# for i in range(6):
#    nro=int(input("Número: "))
#    if nro>0:
#        sumaPositivos=sumaPositivos+nro
#        cantidadPositivos=cantidadPositivos+1
#    else:
#        sumaNegativos=sumaNegativos+nro
# print("Sumatoria de los negativos: ", sumaNegativos)
# if cantidadPositivos!=0:
#    print("Promedio de los positivos: ",sumaPositivos/cantidadPositivos)
# else:
#    print("No se ingresaron números positivos")

#13 //For con continue//
#Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, 
# que sean bisiestos y múltiplos de 10. Nota: para que un año sea bisiesto debe ser divisible por 4 
# y no debe ser divisible por 100, excepto que también sea divisible por 400.

añoInicio=int(input("Año inicial:"))
añoFin=int(input("Año final:"))
print("Año(s) bisiesto(s):")
for año in range(añoInicio, añoFin+1):
   if not año%10==0:
       continue
   if not año%4==0:
       continue
   if año%100!=0 or año%400==0:
      print(año)


 