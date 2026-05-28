import os
os.system("cls")

#ejercicio 1
print("ejercicio 1\n")
lista1 = [4,7,2,9,1]
for x in range(5):
    print(lista1[x])

#ejercicio 2
print("\nejercicio 2\n")
lista2 = [5,8,3,10]
suma = lista2[0] + lista2[1] + lista2[2] + lista2[3]
print(f"{lista2[0]} + {lista2[1]} + {lista2[2]} + {lista2[3]} = {suma}")


#ejercicio 3
print("\nejercicio 3")
lista3 = [2,5,8,11,14,7]
print("\nejercicio 3\n")
for x in range(6):
    if lista3[x] %2 == 0:
        print(lista3[x])

#ejercicio 4
print("\nejercicio 4\n")
lista4 = [12,4,19,7,15]

lista4.sort()
print(lista4[4])

#ejercicio 5
print("\nejercicio 5\n")
lista5 = [5.5,6.0,4.8,7.0,5.9]
contador = 0
for x in range(5):
    contador = contador + lista5[x]
promedio = contador / 5
print(f"El promedio es: {round(promedio,2)}")

#ejercicio 6
print("\nejercicio 6\n")

lista6 = [1,2,3,4,5]
dobles = []
for x in range(5):
    dobles.append(lista6[x]*2)
    
print(dobles)

#ejercicio 7 
print("\nejercicio 7\n")

lista7 = ["manzana","pera","manzana","uva","pera","manzana"]
contador_manzana = 0
for x in range(6):
    if lista7[x] == "manzana":
        contador_manzana = contador_manzana + 1
print(f"La lista dice {contador_manzana} veces manzana.")

#ejercicio 8
print("\nejercicio 8\n")

lista8 = [1,2,3,4,5]
inverso = []
for x in range(4,-1,-1):
    inverso.append(lista8[x])
print(inverso)

#ejercicio 9
print("\nejercicio 9\n")

lista9 = [1,2,2,3,4,4,5]
repetidos = list(set(lista9))
print(repetidos)

#ejercicio 10
print("\nejercicio 10\n")

lista10 = [3,8,1,10,5,2,7]
par = []
inpar = []

for x in range(7):
    if lista10[x] % 2 == 0:
        par.append(lista10[x])
    elif lista10[x] % 2 != 0:
        inpar.append(lista10[x])
par.sort()
inpar.sort()

print(par)
print(inpar)

#ejercicio 11
print("\nejercicio 11\n")

lista11 = []
suma11 = 0
for x in range(5):
    lista11.append(input("Ingrese un numero:\n"))
for x in range(5):
    suma11 = suma11 + (lista11[x])
lista11.sort()
promedio11 = suma11 / 5
print(lista11)
print(lista11[4])
print(lista1[0])
print(promedio11)


