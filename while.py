
# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
total=0
nro=int(input("Número: "))
while nro != 0:
    total+=nro
    nro=int(input("Número: "))



pares=0
n=int(input("Número (-1 para terminar el programa): "))
while n!=-1:
    if n%2 == 0:
        pares+=1
    suma=0
    while n!=0:
        dígito=n%10
        suma+=dígito
        n=n//10
    print("Suma de sus dígitos:", suma)
    n=int(input("Número (-1 para terminar el programa): "))
print("Se ingresaron", pares, "números pares")  