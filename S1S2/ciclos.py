#Realice un contador de 1 a 10
#ciclo while

#para comenzar la variable desde UNO
contador = 1.00
while contador <= 10:
    print(contador)
    contador +=1 # esta expresion equivale a: { contador = contador + 1 }
print("fin del ciclo while")

#para comenzar la variable desde CERO
contador = 0                            #1. siempre hay que iniciar la variable
while contador <= 10:              #2. Formular adecuadamente la condición
    contador = contador + 1     #3. Modificar la variable
    print(contador)
print("fin del ciclo while")

#CICLOS CON FOR
for cont in range(10): #cuenta de 0-9 o 0-(10-1)
    print(cont)
print("fin conteo")

for cont in range(1, 11): #cuenta de 1-10, cuenta de UNO en UNO
    print(cont)
print("fin del conteo uno en uno")

for cont in range(0,26,5): #cuenta 
    print(cont)
print("cuenta en reversa")

for cont in range(20,-1,-1): #cuenta desde 1-10, cuenta de uno en uno
    print(cont)
print("fin conteo x")
