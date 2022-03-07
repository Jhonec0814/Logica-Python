#Logica de Python

'''edad= int(input("Digita tu edad: "))
print(edad)

# Condición lógica simple
bandera=True
if(edad>=18 and bandera==True):
    print("Bienvenido a Globant")
else:
    print("Andaté de aquí mi pae")'''

#Ejemplo 1 Hidroituango
'''nivelAgua= float(input("Ingre que nivel de agua se encuentra actualmente: "))    

if(nivelAgua>=0 and nivelAgua<200):
    print("La represa tiene poca agua")

elif(nivelAgua>=200 and nivelAgua<450):
    print("La represa se encuentra en niveles optimos")

elif(nivelAgua>450):        
    print("¡Cuidado!, Se necesitan abrir las compuertas")

else:
    print("Digitó un nivel invalido")    '''


#Ejemplo 2 Estaciones
'''mes=(input("Ingrese el mes que necesita consultar: ")).lower()

if(mes=='enero' or mes =='febrero' or mes =='marzo'):
    print("Actualmente nos encontramos en Invierno, ponte un saco")

elif(mes=='abril' or mes=='mayo' or mes=='junio'):
    print("Actualmente nos encontramos en Verano, chupa paleta")

elif(mes=='julio' or mes=='agosto' or mes=='septiembre'):
    print("Actualmente nos encontramos en Otoño, recoge las hojas")        

elif(mes=='octubre' or mes=='noviembre' or mes=='diciembre')
    print("Actualmente nos encontramos en Primavera, vamos por flores")

else:
    print("ERROR, Ingresa un número valido")
    '''


# Ejemplo 3 Edad
'''while(True):
    edad=float(input("Ingrese su edad: "))

    if(edad>=0 and edad<=14):
        print("Actualmente eres un Niño")

    elif(edad>14 and edad<=28):
        print("Actualmente eres Joven")

    elif(edad>28 and edad<=60):
        print("Actualmente eres un Adultero")

    elif(edad>60):
        print("Actualmente eres un Adulto Mayor")

    else:
        print("¡Ingresa un número valido!")    '''

# Ejemplo 4 Operador ternario
'''parametro=True



print("El parametro es verdadero") if parametro==True else print("El parametro es Falso")


estaLloviendo=False

print("Está lloviendo") if estaLloviendo==True else print("No está lloviendo")'''







