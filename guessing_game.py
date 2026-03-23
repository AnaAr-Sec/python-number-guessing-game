from random import randint
print(f"{'=' * 5} Adivina un numero {'=' * 5}\n")

# 1. Preparación
nombre = input('¿Cual es tu nombre?: ')
numero_random = randint(1, 100)
intentos = 0
print(f'¡{nombre}, tienes solo 8 intentos para adivinarlo!.')
#--------------------------------------------------------------------
# 2. El bucle FOR (del 0 al 7, total 8 vueltas) 
for intento in range(1, 9): # Usamos 1 a 9 para que 'intento' sea el número real
    conteo = input(f'Intento {intento} - ¿Cuál es el número?: ')
  
    try:
        estimacion = int(conteo)
    except ValueError:
        print('Solo se permiten números.')
        continue
    if estimacion < 1 or estimacion > 100:
        print('Número NO permitido')
    elif estimacion < numero_random :
        print('Incorrecto, este número es menor al que yo he elegido.')
    elif estimacion > numero_random :
        print('Incorrecto, este número es mayor al que yo he elegido.')
    else:
        print(f'"Ganaste", Y solo te tomó {intento} intentos.')
        break
# 3. Final por derrota
else: # Este 'else' pertenece al FOR: se ejecuta solo si el bucle termina
    print(f"Se agotaron los intentos. El número era {numero_random}.")
