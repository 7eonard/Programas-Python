
#1 Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
# total=0
# nro=int(input("Ingrese Número: "))
# while nro != 0:
#     total+=nro
#     nro=int(input("Ingrese Número: "))

#2 Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

# positivos=0
# n=int(input("Número (0 para terminar): "))
# while n!=0:
#     if n>0:
#         positivos+=1
#     n=int(input("Número (0 para terminar): "))
# print("Cantidad de positivos:", positivos)

#3 Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el
   # mayor número ingresado.

# mayor=-1
# n=int(input("Ingrese numero positivo:" ))
# while n>=0:
#     if n>mayor:
#        mayor=n
#     n=int(input("Ingrese numero positivo: "))
# print ("El mayor numero ingresado es:", mayor)

#4 Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
# suma=0
# n=int(input("ingrese el numero positivo:" ))
# while n!=0:
#     dígito=n%10
#     suma+=dígito #=> suma=suma+dígito
#     n=n//10
# print("suma de los dígitos:" ,suma)

#5 Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos
#  que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los 
# números ingresados por el usuario fueron números pares.

# pares=0
# n=int(input("Número (-1 para terminar el programa): "))
# while n!=-1:
#     if n%2 == 0:
#         pares+=1
#     suma=0
#     while n!=0:
#         dígito=n%10
#         suma+=dígito #=> suma=suma+dígito
#         n=n//10
#     print("Suma de sus dígitos:", suma)
#     n=int(input("Número (-1 para terminar el programa): "))
# print("Se ingresaron", pares, "números pares") 

#6 //While con Break//
# Mostrar un menú con tres opciones: 
# 1- comenzar programa, 
# 2- imprimir listado, 
# 3-finalizar programa. 
# A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). 
# Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada
# cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. 
# Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

# while True:
#     print("Opción 1 - comenzar programa")
#     print("Opción 2 - imprimir listado")
#     print("Opción 3 - finalizar programa")
#     opción=int(input("Opción elegida: "))
#     if opción==1:
#         print("¡Comenzamos!")
#     elif opción==2:
#         print("Listado:")
#         print("Nadia, Esteban, Maricela, Fernanda")
#     elif opción==3:
#         print("Hasta la próxima")
#         break
#     else:
#         print("Opción incorrecta. Debe ingresar 1, 2 o 3")

#7 //While con Break y Continue//
# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
# Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar
# que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una 
# coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

# frase=input("Frase: ")
# Letra=input("Digite la Letra para buscar su posición: ")
# i=0
# while i!=len(frase):
#     if Letra!=frase[i]:
#         print(Letra, "No se encontró en la posición", i)
#         i+=1
#         continue
#     print(Letra, "Se encontró en la posición", i)
#     break

#8 //While_for_If con Break//
# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.

# cantidad=0
# n=int(input("Número: "))
# while n!=0:
#  primo=True
#  for i in range(2,n):
#    if n%i==0:
#      primo=False
#      break
#  if primo:
#    cantidad+=1
#  n=int(input("Número: "))
# print("primos: ", cantidad)

#9 Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce 
# la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos 
# cuando el usuario ingrese el monto 0.
# Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, 
# informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe
# aplicar un 10% de descuento.

# total=0
# monto=float(input("Monto de una venta: $"))
# while monto!=0:
#     if monto<0:
#         print("Monto no válido.")
#     else:
#         total+=monto #=> total=total + monto
#     monto=float(input("Monto de una venta: $"))
# if total>1000:
#     total-=total*0.1 #=>total=total-(total*0.1)
# print("Monto total a pagar: $", total)

#10 Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
# Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
# Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

# numero=int(input("numero: "))
# totalPares=0
# totalImpares=0
# while numero!=0:
#    pares=0
#    impares=0
#    while numero!=0:   
#        ultimo_dígito=numero%10
#        if ultimo_dígito%2==0:
#            pares+=1
#            totalPares+=1
#        else:
#            impares+=1
#            totalImpares+=1
#        numero=numero//10
#    print("El número ingresado tiene ",pares," dígitos pares y ",impares," dígitos impares")
#    numero=int(input("Otro número: "))
# print("Total de dígitos pares:", totalPares)
# print("Total de dígitos impares:", totalImpares)

#11 Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando 
# el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de 
# longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea 
# completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de 
# libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
#**Ejemplo de ejecución:**
# Libro: Los 3 mosqueteros
# Libro: Historia de 2 ciudades
# Libro: /
# Línea completa. Aparecen 2 dígitos numéricos.
# Libro: 20000 leguas de viaje submarino
# Libro: El señor de los anillos
# Libro: /
# Línea completa. Aparecen 5 dígitos numéricos.
# Libro: 20 años después
# Libro: *
# Fin. Se leyeron 2 líneas completas.

lineas=0
dígitos="0123456789"
cantidadDigitos=0
Título=input("Título del libro: ")
while Título!="*":
    for caracter in Título:
        if caracter in dígitos:
            cantidadDigitos+=1
    if Título=="/":
        lineas+=1
        print("Aparecen ", cantidadDigitos, " dígitos en la línea")
        cantidadDigitos=0
    Título=input("Título: ")
print("Se leyeron ",lineas," líneas completas")

#12 Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga 
# (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará 
# como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

frase=input("Frase: ").strip()
cantidad=0
len_p_mas_larga=0
while len(frase) != 0:
    cantidad=cantidad+1
    i=frase.find(" ")
    if i != -1:
        palabra=frase[0:i]
        while i < len(frase) and frase[i] == " ":
            i=i+1
        frase=frase[i:]
    else:
        palabra=frase
        frase=""
    if len(palabra) > len_p_mas_larga:
        len_p_mas_larga=len(palabra)
        p_mas_larga=palabra
if cantidad > 0:
    print("Palabra más larga:", p_mas_larga)
print("Cantidad de palabras:", cantidad)