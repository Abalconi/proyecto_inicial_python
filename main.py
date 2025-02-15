import random
import interfaz

## Funciones del sistema
# Dentro del archivo __main.py__ deberá implementar las siguientes funciones que utilizará luego el bloque main para armar el proyecto:

### Funcion "leer_palabra_secreta"
# Encabezado de la función:

# Entrada (argumentos):
# - Esta función recibe por parámetro la lista de posibles palabras secretas a adivinar.

# Objetivo:
# - La función deberá utilizar la función `random.choice` para seleccionar aleatoriamente alguna palabra de la lista de palabras. Almacenar esa palabra seleccionada en una varible.

# Salida (return):
# - La función deberá retornar la palabra secreta seleccionada por el random.choice.

def leer_palabra_secreta(palabras):

    palabra_secreta = random.choice(palabras)
    return palabra_secreta

### Funcion "pedir_letra"
# Encabezado de la función:

# Entrada (argumentos):
# - Esta función recibe por parámetro la lista de palabras utilizadas hastas el momento.

# Objetivo:
# - Deberá armar un bucle While infinito que se ejecute hasta que el procedimiento de pedir letra se complete exitosamente.
# - Deberá pedirle al usuario que ingrese por "input" una letra nueva que no haya utilizado antes. Almacenar esa letra ingresada por "input" en una variable.
# - La letra ingresada deberá transformarse a minúscula para evitar problemas.
# - Utilizando la variable "letras_usadas" deberá verificar utilizando el operador "in" que esa letra es nueva y no se ha utilizado antes. Si se ha utilizado antes (es decir, existe dentro de "letras_usadas") el sistema no deberá salir del bucle y volverá al comienzo solicitando una letra nueva.
# - Deberá verificar que la letra ingresada es solo una letra, es decir, verificar que no se ha ingresado más de una letra a la vez. Para eso utilice la función "len". Si se ha ingresado más de una letra junta, el sistema no deberá salir del bucle y volverá al comienzo solicitando una letra nueva.
# - Si todas las condiciones se cumplen, deberá salir del bucle.
# - Antes de que finalice la función debe guardar la variable "letra" que validó en la lista "letras_usadas" utilizando append.

# Salida (return):
# - La función deberá retornar la letra validada (return).

def pedir_letra(letras_usadas):

    while True:
        letra = input("Ingrese una letra nueva: ").lower()
        if len(letra) != 1:
            print("Debe ingresar solo una letra. Intente nuevamente.")
            continue
        if letra in letras_usadas:
            print("La letra ya ha sido utilizada. Intente nuevamente.")
            continue
        letras_usadas.append(letra)
        break
    return letra

### Funcion "verificar_letra"
# Encabezado de la función:

# Entrada (argumentos):
# - Esta función recibe por parámetro la letra ingresada por el usuario y la palabra secreta a adivinar.

# Objetivo:
# - Deberá verificar si la variable "letra" es parte de la palabra secreta a divinar "palabra_secreta". Utilice el operador "in" para llevar a cabo esta verificación.

# Salida (return):
# - Si la letra pertenece a la palabra secreta a adivinar, esta función debe retornar True.
# - Si la letra __no__ pertenece a la palabra secreta a adivinar, esta función debe retornar False.
def verificar_letra(letra, palabra_secreta):
    if letra in palabra_secreta:
        return True
    else:
        return False

### Funcion "validar_palabra"
# Encabezado de la función:

# Entrada (argumentos):
# - Esta función recibe por parámetro las letras ingresada hasta el momento por el usuario "letras_usadas" y la palabra secreta a adivinar "palabra_secreta".

# Objetivo:
# - Deberá verificar si todas las letras de la "palabra_secreta" se encuentran contenidas/disponible en la lista de letras usadas "letras_usadas".
# - Para esto deberá armar un bucle que recorra todas las letras de "palabra_secreta". Con el operador "in" debe verificar si cada letra de la palabra secreta existe en la lista "letras_usadas".
# - Con que una letra de la palabra secreta no exista en las letras usadas, se debe terminar el bucle e indicar que aún no se ha adivinado la palabra secreta.

# Salida (return):
# - Si se avidinó por completo la palabra secreta, esta función debe retornar True.
# - Si __no__ se avidinó por completo la palabra secreta, esta función debe retornar False.

def validar_palabra(letras_usadas, palabra_secreta):
    for letra in palabra_secreta:
        if letra not in letras_usadas:
            return False
    return True


if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de una lista.
    palabras = ["listas", "bucles", "variables"]
    palabra_secreta = leer_palabra_secreta(palabras)
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos == 7 and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')