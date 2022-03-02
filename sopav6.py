# TP Final Programacion 2
# Angelo Alvarez

import random

# leerArchivo: List[Strings] -> String, List[String], String
# Toma el archivo ya leido y retorna por separado los datos
def leerArchivo(archivo):
    sinSalto = []
    dimension = 0
    palabras = []
    count = 0
    complejidad = 0
    for cadena in archivo: # Saca el \n de las cadenas
        cadena = cadena.strip('\n')
        sinSalto.append(cadena)
    
    for i in range(0, len(sinSalto)): # Busca la dimension de la sopa
        if sinSalto[i] == "DIMENSION":
            dimension = int(sinSalto[i+1])
        break
    
    for j in range(0, len(sinSalto)): # Busca las palabras
        if sinSalto[j] == "PALABRAS":
            count = j+1
            while sinSalto[count] != "COMPLEJIDAD":
                palabras.append(sinSalto[count])
                count += 1
            break
    for h in range(0,len(sinSalto)): # Busca la complejidad
        if sinSalto[h] == "COMPLEJIDAD":
            complejidad = int(sinSalto[h+1])
            break
        
    return dimension, palabras,complejidad

# letraRandom: None -> String
# letraRandom: Genera una letra aleatoria del abecedario
def letraRandom():
    num = random.randint(0, 25)
    abc = "abcdefghijklmnopqrstuvwxyz"
    letra = abc[num]
    return letra

# rellenar_sopa: List[strings] -> List[Strings]
# Toma una sopa a la que ya se hayan colocado las palabras y luego la rellena con
# letras randoms.

def rellenar_sopa(sopa):
    count = 0
    index = 0
    nuevaSopa = []
    while count < len(sopa[0]):
        fila = sopa[count]
        while index < len(fila):
            if fila[index] == " ":
                fila = fila[:index] + letraRandom() + fila[index+1:]            
            index += 1
        nuevaSopa.append(fila)
        count += 1
        index = 0
    return nuevaSopa

# generarSopa_vacia: Int -> List[Strings]
# Genera una lista de espacios vacios, que representa
# una sopa vacia que se rellenará posteriormente

def generarSopa_vacia(dimension):
    fila = " " * dimension
    sopa = []
    for i in range(0, dimension):
        sopa.append(fila)
    return sopa

# verificar_fila_vacia: String -> Boolean, List[Ints]
# Verifica si un string es solo el caracter espacio " "
# Retorna True si esta vacia y False si no lo esta, y retorna una 
# lista con las posiciones que estan ocupadas en el string

def verificarFilaVacia(fila):
    posiciones_ocupadas = []
    valor = True
    for i in range(0, len(fila)):
        if fila[i] != " ":
            posiciones_ocupadas.append(i)
            valor = False
    return valor, posiciones_ocupadas


# hay_espacio: List[Numbers], Int, Int -> Boolean, Int
# Verifica si hay espacio en la fila para que entre una palabra
# En caso de que haya espacio devuelve en que casillero de la fila hay que poner la palabra

def hay_espacio(pos_ocupadas, longitud_palabra, dimension):
    posiciones_ocupadas = [-1] # Se agrega el -1 para que empiece a contar desde la primer linea
    posiciones_ocupadas.extend(pos_ocupadas)
    posiciones_ocupadas.append(dimension) # Se agrega el ultimo casillero
    count = 0
    espacio = False
    while count < len(posiciones_ocupadas)-1:
        lugar = abs(posiciones_ocupadas[count+1] - posiciones_ocupadas[count])-1
        if lugar >= longitud_palabra:
            espacio = True
            return espacio, posiciones_ocupadas[count]+1            
        count += 1
    return espacio, posiciones_ocupadas


# obtenerColumna: List[Strings], Int, Int -> String
# Recibe una lista de strings, que seria nuestra sopa, y devuelve
# la columna deseadaa en forma de string

def obtenerColumna(sopa,columna,dimension):
    Columna = ""
    for i in range(0, dimension):
        linea = sopa[i]
        Columna += linea[columna]
    return Columna

# rotarSopa: List[Strings] -> List[Strings]
# Toma una sopa y la rota, de modo que las columnas son filas
# y las filas columnas

def rotarSopa(sopa):
    dimension = len(sopa[0])
    nuevaSopa = []
    for i in range(0, dimension):
        linea = ""
        for j in range(0, dimension):
            columna = sopa[j]
            linea += columna[i]
        nuevaSopa.append(linea)
    return nuevaSopa

# rotarSopa2: List[Strings] -> List[Strings]
# Toma una sopa y la rota en 45 grados
# Ej: abcd       dhlp
#     efgh  -->  cgko
#     ijkl       bfjo
#     mnop       aiem

def rotarSopa2(sopa):
    dimension = len(sopa[0])
    nuevaSopa = []
    count = dimension-1
    while count >= 0:
        linea = ""
        for i in range(0, dimension):
            columna = sopa[i]
            linea += columna[count]
        nuevaSopa.append(linea)
        count -= 1
    return nuevaSopa

# rotarSopa3: List[Strings] -> List[Strings]
# Toma una sopa y la rota en -45 grados

def rotarSopa3(sopa):
    dimension = len(sopa[0])
    nuevaSopa = []
    count = 0
    while count < dimension:
        linea = ""
        for i in range(0,dimension):
            columna = sopa[i]
            linea += columna[count]
        linea = linea[::-1]
        nuevaSopa.append(linea)
        count += 1
    return nuevaSopa

# filaHorizontal: String, String -> String, Boolean
# Toma un string que representa una fila de la sopa, y si entra la palabra en la fila,
# la pone aleatoriamente en una casillero que entre en la fila,
# caso contrario deja la fila como esta y devuelve un boolean indicando que no
# fue posible colocarla

def filaHorizontal(fila, palabra):
    dimension = len(fila)
    casillerosDisponibles = [] 
    valor = False
    for i in range(0, dimension-len(palabra)+1):
        casillerosDisponibles.append(i)
    if verificarFilaVacia(fila)[0]:
        casilla = casillerosDisponibles[random.randint(0, len(casillerosDisponibles)-1)]
        fila = fila[:casilla] + palabra + fila[casilla+len(palabra):]
    else:
        if hay_espacio(verificarFilaVacia(fila)[1], len(palabra), dimension)[0]:
            casilla = hay_espacio(verificarFilaVacia(fila)[1], len(palabra), dimension)[1]
            fila = fila[:casilla] + palabra + fila[casilla+len(palabra):]
        else:
            valor = True
    return fila, valor

# ponerPalabra: String, List[Ints], String, Int -> String
# Toma una linea, las posiciones que estan ocupadas en la linea, la palabra 
# a colocar y la dimension de la sopa, y trata de colocar la palabra, de modo que
# comparta alguna letra con la linea, haciendo que se puedan cruzar dos palabras

def ponerPalabra(linea, pos_ocupadas, palabra,dimension):
    count = 0
    aux = linea
    posibilidades = []
    while count <= dimension - len(palabra):
        valor = True
        linea = linea[:count] + palabra + linea[count+len(palabra):]
        for posicion in pos_ocupadas:
            if not(aux[posicion] == linea[posicion]):
                valor = False
                break
        if valor:
            posibilidades.append(linea)
        count += 1
        linea = aux
    if posibilidades:
        linea = posibilidades[random.randint(0, len(posibilidades)-1)]
    return linea

# obtenerVertical: List[Strings], Int, Int -> String
# Toma una sopa, una posicion de fila y columna, y devuelve la diagonal indicada

def obtenerVertical(sopa, Fila, Columna):
    dimension = len(sopa[0])
    if Fila >= Columna:
        fila = max(Fila, Columna) # Fila desde donde se va a empezar a iterar
        columna = min(Fila, Columna) # columna desde donde se va a empezar a iterar
    elif Columna > Fila:
        fila = min(Fila, Columna)
        columna = max(Fila, Columna)
    Vertical = ""
    for i in range(fila, dimension-Columna):  
        linea = sopa[i]
        Vertical += linea[columna]
        columna += 1
    return Vertical

# ponerVertical: List[Strings], String, Int, Int -> List[Strings]
# Toma una sopa, el string que queremos colocar y la fila y columna donde 
# queremos colocar la diagonal y la pone en la sopa, diagonalmente.

def ponerVertical(sopa, linea, Fila, Columna):
    dimension = len(sopa[0])
    count = 0
    if Fila >= Columna:
        fila = max(Fila, Columna)
        columna = min(Fila, Columna)
        count2 = columna
    elif Columna > Fila:
        fila = min(Fila, Columna)
        columna = max(Fila, Columna)
        count2 = columna
    while count < len(linea):
        aux = sopa[fila]
        aux = aux[:count2] + linea[count] + aux[count2+1:]
        sopa[fila] = aux
        fila += 1
        count += 1
        count2 += 1
    return sopa

# buscar_palabras_repetidasD0: List[Strings], List[Strings] -> Boolean
# Toma una sopa y las palabras y verifica que una palabra no este repetida
# en la sopa, si alguna palabra está repetida, retorna True, caso contrario
# retorna False. Sirve para la dificultad 0

def buscar_palabras_repetidasD0(sopa, palabras):
    while palabras:
        palabra = palabras[0]
        contador_palabras = 0
        # buscar palabra horizontalmente
        for linea in sopa:
            if palabra in linea:
                contador_palabras += 1
        if contador_palabras > 1:
            return True
        # Busca palabras verticalmente
        sopa = rotarSopa(sopa)
        for linea in sopa:
            if palabra in linea:
                contador_palabras += 1
        if contador_palabras > 1:
            return True
        palabras.remove(palabra)
    return False

# buscar_palabras_repetidasD1: List[Strings], List[Strings] -> Boolean
# Lo mismo que buscar_palabras_repetidasD0, solo que ahora tambien verifica
# en vertical. Sirve para la dificultad 1

def buscar_palabras_repetidasD1(sopa, palabras):
    dimension = len(sopa[0])
    while palabras:
        palabra = palabras[0]
        contador_palabras = 0
        # buscar palabra horizontalmente
        for linea in sopa:
            if palabra in linea:
                contador_palabras += 1
        if contador_palabras > 1:
            return True
        # Busca palabras verticalmente
        sopa = rotarSopa(sopa)
        for linea in sopa:
            if palabra in linea:
                contador_palabras += 1
        sopa = rotarSopa(sopa)
        if contador_palabras > 1:
            return True
        # Busca palabras verticalemente
        for i in range(0, (dimension-len(palabra))+1):
            Vertical = obtenerVertical(sopa, i, 0)
            if palabra in Vertical:
                contador_palabras += 1
        for j in range(0, (dimension-len(palabra)+1)):
            Vertical = obtenerVertical(sopa, 0, j)
            if palabra in Vertical:
                contador_palabras += 1
        if contador_palabras > 1:
            return True
        palabras.remove(palabra)
    return False

# buscar_palabras_repetidasD2: List[Strings], List[Strings] -> Boolean
# Lo mismo que buscar_palabras_repetidasD2, solo que ahora verifica las
# palabras al reves y en vertical de esquina sup der a esquina inf izq.
# Sirve para las dificultades 2 y 3

def buscar_palabras_repetidasD2(sopa, palabras):
    dimension = len(sopa[0])
    while palabras:
        palabra = palabras[0]
        contador_palabras = 0
        # buscar palabra horizontalmente
        for linea in sopa:
            if palabra in linea:
                contador_palabras += 1
            palabra = palabra[::-1]
            if palabra in linea:
                contador_palabras += 1
            palabra = palabras[0]
        if contador_palabras > 1:
            return True
        # Busca palabras verticalmente
        sopa = rotarSopa(sopa)
        for linea in sopa:
            if palabra in linea:
                contador_palabras += 1
            palabra = palabra[::-1]
            if palabra in linea:
                contador_palabras += 1
            palabra = palabras[0]
        sopa = rotarSopa(sopa)
        if contador_palabras > 1:
            return True
        # Busca palabras verticalemente (esquina sup izq a esquina inf der)
        for i in range(0, (dimension-len(palabra))+1):
            Vertical = obtenerVertical(sopa, i, 0)
            if palabra in Vertical:
                contador_palabras += 1
            palabra = palabra[::-1]
            if palabra in Vertical:
                contador_palabras += 1
            palabra = palabras[0]
        for j in range(0, (dimension-len(palabra)+1)):
            Vertical = obtenerVertical(sopa, 0, j)
            if palabra in Vertical:
                contador_palabras += 1
            palabra = palabra[::-1]
            if palabra in Vertical:
                contador_palabras += 1
            palabra = palabras[0]
        if contador_palabras > 1:
            return True
        # Busca palabras verticalemente (esquina inf izq a esquina sup der)
        sopa = rotarSopa2(sopa)
        for i in range(0, (dimension-len(palabra))+1):
            Vertical = obtenerVertical(sopa, i, 0)
            if palabra in Vertical:
                contador_palabras += 1
            palabra = palabra[::-1]
            if palabra in Vertical:
                contador_palabras += 1
            palabra = palabras[0]
        for j in range(0, (dimension-len(palabra)+1)):
            Vertical = obtenerVertical(sopa, 0, j)
            if palabra in Vertical:
                contador_palabras += 1
            palabra = palabra[::-1]
            if palabra in Vertical:
                contador_palabras += 1
            palabra = palabras[0]
        if contador_palabras > 1:
            return True
        sopa = rotarSopa3(sopa)
        palabras.remove(palabra)
    return False

# Dificultad0: Int, List[Strings] -> None
# Toma la dimension de la sopa y las palabras a colocar y, primero genera una sopa vacia
# Donde seran colocadas las palabras, luego aleatoriamente decide si va a ir horizontal
# o vertical. Si la palabra entra en la sopa correctamente, se la elimina de la lista y 
# sigue con la siguiente, si no entra, vuelve a probar con un numero maximo de intentos.
# En caso de que se terminen los intentos, se concluye que no es posible generar la sopa.

def Dificultad0(dimension, palabras):
    valor = True
    intentos = 0
    sopa = generarSopa_vacia(dimension)
    aux = palabras
    print(palabras)
    while palabras and intentos < 100:
        desicion = random.randint(0, 1) # 0 horizontal, 1 vertical
        palabra = palabras[0]
        if desicion == 0:
            fila_a_modificar = random.randint(0, (dimension-1))
            datos = filaHorizontal(sopa[fila_a_modificar], palabra)
            sopa[fila_a_modificar] = datos[0]
            if not(datos[1]):
                palabras.remove(palabra)
        elif desicion == 1:
            columna_a_modificar = random.randint(0, (dimension-1))
            sopa = rotarSopa(sopa)
            datos = filaHorizontal(sopa[columna_a_modificar], palabra)
            sopa[columna_a_modificar] = datos[0]
            if not(datos[1]):
                palabras.remove(palabra)
            sopa = rotarSopa(sopa)
        # Se verifica que no haya palabras repetidas, en caso de que haya
        # Se vuelve a intentar con una nueva sopa
        if not(palabras):
            sopa = rellenar_sopa(sopa)
            if buscar_palabras_repetidasD0(sopa, palabras):
                sopa = generarSopa_vacia(dimension)
                palabras = aux
        intentos += 1
    if intentos >= 100:
        print("No es posible generar la sopa")
        return
    else:
        for linea in sopa:
            print(linea)

# Dificultad1: Int, List[Strings] -> None
# Similar a Dificultad0, solo que se agrega la posibilidad de
# que se ponga la palabra en vertical

def Dificultad1(dimension, palabras):
    valor = True
    intentos = 0
    aux = palabras
    sopa = generarSopa_vacia(dimension)
    while palabras and intentos < 100:
        desicion = random.randint(0, 2) # 0 horizontal, 1 vertical, 2 diagonal 
        palabra = palabras[0]
        if desicion == 0:
            fila_a_modificar = random.randint(0, (dimension-1))
            datos = filaHorizontal(sopa[fila_a_modificar], palabra)
            sopa[fila_a_modificar] = datos[0]
            if not(datos[1]):
                palabras.remove(palabra)
        elif desicion == 1:
            columna_a_modificar = random.randint(0, (dimension-1))
            sopa = rotarSopa(sopa)
            datos = filaHorizontal(sopa[columna_a_modificar], palabra)
            sopa[columna_a_modificar] = datos[0]
            if not(datos[1]):
                palabras.remove(palabra)
            sopa = rotarSopa(sopa)
        elif desicion == 2:
            desicion3 = random.randint(0,1)
            if desicion3 == 0:
                Fila = random.randint(0, dimension-len(palabra))
                Columna = 0
            else:
                Fila = 0
                Columna = random.randint(0, dimension-len(palabra))
            Vertical = obtenerVertical(sopa, Fila, Columna)
            datos = filaHorizontal(Vertical, palabra)
            sopa = ponerVertical(sopa, datos[0], Fila, Columna)
            if not(datos[1]):
                palabras.remove(palabra)
        if not(palabras):
            sopa = rellenar_sopa(sopa)
            if buscar_palabras_repetidasD1(sopa, palabras):
                sopa = generarSopa_vacia(dimension)
                palabras = aux
        intentos += 1
    if intentos >= 100:
        print("No es posible generar la sopa")
        return
    else:
        for linea in sopa:
            print(word)
    

# Dificultad2: Int, List[Strings] -> None
# Similar a Dificultad0, solo que se agrega la posibilidad de
# que las verticales puedan ir de esquina sup der a esquina inf izq

def Dificultad2(dimension, palabras):
    intentos = 0
    valor = True
    sopa = generarSopa_vacia(dimension)
    aux = palabras
    while palabras and intentos < 100:
        palabra = palabras[0]
        desicion = random.randint(0,2) # 0 horizontal, 1 vertical, 2 diagonal
        if desicion == 0:
            desicion2 = random.randint(0,1) # 0 normal, 1 al reves
            if desicion2 == 0:
                palabra = palabra
            elif desicion2 == 1:
                palabra = palabra[::-1]
            fila_a_modificar = random.randint(0, (dimension-1))
            datos = filaHorizontal(sopa[fila_a_modificar], palabra)
            sopa[fila_a_modificar] = datos[0]
            if not(datos[1]):
                palabra = palabras[0]
                palabras.remove(palabra)
        elif desicion == 1:
            desicion2 = random.randint(0, 1) # 0 vertical normal, 1 vertical al reves
            if desicion2 == 0:
                # Se pone vertical normal
                palabra = palabra
            elif desicion2 == 1:
                # Se pone vertical al reves
                palabra = palabra[::-1]
            columna_a_modificar = random.randint(0, (dimension-1))
            sopa = rotarSopa(sopa)
            datos = filaHorizontal(sopa[columna_a_modificar], palabra)
            sopa[columna_a_modificar] = datos[0]
            if not(datos[1]):
                palabra = palabras[0]
                palabras.remove(palabra)
            sopa = rotarSopa(sopa)
        elif desicion == 2:
            desicion2 = random.randint(0, 1)
            if desicion2 == 0:
                # Se pone en diagonal de esquina sup izq a esquina inf dere
                desicion3 = random.randint(0,1) # 0 normal 1 al reves
                if desicion3 == 0:
                    palabra = palabra
                elif desicion3 == 1:
                    palabra = palabra[::-1]
                desicion4 = random.randint(0,1)
                if desicion4 == 0:
                    Fila = random.randint(0, dimension-len(palabra))
                    Columna = 0
                elif desicion4 == 1:
                    Fila = 0
                    Columna = random.randint(0, dimension-len(palabra))
                Vertical = obtenerVertical(sopa, Fila, Columna)
                datos = filaHorizontal(Vertical, palabra)
                sopa = ponerVertical(sopa, datos[0], Fila, Columna)
                if not(datos[1]):
                    palabra = palabras[0]
                    palabras.remove(palabra)
            elif desicion2 == 1:
                # Se pone en diagonal de esquina sup der a esquina inf izq
                desicion3 = random.randint(0,1) # 0 normal 1 al reves
                if desicion3 == 0:
                    palabra = palabra
                elif desicion3 == 1:
                    palabra = palabra[::-1]
                desicion4 = random.randint(0,1)
                if desicion4 == 0:
                    Fila = random.randint(0, dimension-len(palabra))
                    Columna = 0
                elif desicion4 == 1:
                    Fila = 0
                    Columna = random.randint(0, dimension-len(palabra))
                sopa = rotarSopa2(sopa)
                Vertical = obtenerVertical(sopa, Fila, Columna)
                datos = filaHorizontal(Vertical, palabra)
                sopa = ponerVertical(sopa, datos[0], Fila, Columna)
                sopa = rotarSopa2(sopa)
                if not(datos[1]):
                    palabra = palabras[0]
                    palabras.remove(palabra)
        if not(palabras):
            sopa = rellenar_sopa(sopa)
            if buscar_palabras_repetidasD2(sopa, palabras):
                sopa = generarSopa_vacia(dimension)
                palabras = aux
        intentos += 1
    if intentos >= 100:
        print("No es posible generar la sopa")
        return
    else:
        for word in sopa:
            print(word)

# Dificultad2: Int, List[Strings] -> None
# Similar a Dificultad0, solo que ahora las palabras se pueden
# cruzar

def Dificultad3(dimension, palabras):
    intentos = 0
    valor = True
    sopa = generarSopa_vacia(dimension)
    while palabras and intentos < 100:
        palabra = palabras[0]
        desicion = random.randint(0,2) # 0 horizontal, 1 vertical, 2 diagonal
        if desicion == 0:
            desicion2 = random.randint(0,1) # 0 normal, 1 al reves
            if desicion2 == 0:
                palabra = palabra
            elif desicion2 == 1:
                palabra = palabra[::-1]
            fila_a_modificar = random.randint(0, (dimension-1))
            datos = filaHorizontal(sopa[fila_a_modificar], palabra)
            sopa[fila_a_modificar] = datos[0]
            if not(datos[1]):
                palabra = palabras[0]
                palabras.remove(palabra)
            else:
                fila = sopa[fila_a_modificar]
                aux = sopa[fila_a_modificar]
                sopa[fila_a_modificar] = ponerPalabra(fila, verificarFilaVacia(fila)[1], palabra, dimension)
                if fila != sopa[fila_a_modificar]:
                    palabra = palabras[0]
                    palabras.remove(palabra)
        elif desicion == 1:
            desicion2 = random.randint(0, 1) # 0 vertical normal, 1 vertical al reves
            if desicion2 == 0:
                # Se pone vertical normal
                palabra = palabra
            elif desicion2 == 1:
                # Se pone vertical al reves
                palabra = palabra[::-1]
            columna_a_modificar = random.randint(0, (dimension-1))
            sopa = rotarSopa(sopa)
            datos = filaHorizontal(sopa[columna_a_modificar], palabra)
            sopa[columna_a_modificar] = datos[0]
            if not(datos[1]):
                palabra = palabras[0]
                palabras.remove(palabra)
            else:
                fila = sopa[columna_a_modificar]
                aux = sopa[columna_a_modificar]
                sopa[columna_a_modificar] = ponerPalabra(fila, verificarFilaVacia(fila)[1], palabra, dimension)
                if fila != sopa[columna_a_modificar]:
                    palabra = palabras[0]
                    palabras.remove(palabra)
            sopa = rotarSopa(sopa)
        elif desicion == 2:
            desicion2 = random.randint(0, 1)
            if desicion2 == 0:
                # Se pone en diagonal de esquina sup izq a esquina inf dere
                desicion3 = random.randint(0,1) # 0 normal 1 al reves
                if desicion3 == 0:
                    palabra = palabra
                elif desicion3 == 1:
                    palabra = palabra[::-1]
                desicion4 = random.randint(0,1)
                if desicion4 == 0:
                    Fila = random.randint(0, dimension-len(palabra))
                    Columna = 0
                elif desicion4 == 1:
                    Fila = 0
                    Columna = random.randint(0, dimension-len(palabra))
                Vertical = obtenerVertical(sopa, Fila, Columna)
                datos = filaHorizontal(Vertical, palabra)
                sopa = ponerVertical(sopa, datos[0], Fila, Columna)
                if not(datos[1]):
                    palabra = palabras[0]
                    palabras.remove(palabra)
                else:
                    aux = Vertical
                    Vertical = ponerPalabra(Vertical, verificarFilaVacia(Vertical)[1], palabra, len(Vertical))
                    sopa = ponerVertical(sopa, Vertical, Fila, Columna)
                    if Vertical != aux:
                        palabra = palabras[0]
                        palabras.remove(palabra)
            elif desicion2 == 1:
                # Se pone en diagonal de esquina sup der a esquina inf izq
                desicion3 = random.randint(0,1) # 0 normal 1 al reves
                if desicion3 == 0:
                    palabra = palabra
                elif desicion3 == 1:
                    palabra = palabra[::-1]
                desicion4 = random.randint(0,1)
                if desicion4 == 0:
                    Fila = random.randint(0, dimension-len(palabra))
                    Columna = 0
                elif desicion4 == 1:
                    Fila = 0
                    Columna = random.randint(0, dimension-len(palabra))
                sopa = rotarSopa2(sopa)
                Vertical = obtenerVertical(sopa, Fila, Columna)
                datos = filaHorizontal(Vertical, palabra)
                sopa = ponerVertical(sopa, datos[0], Fila, Columna)
                if not(datos[1]):
                    palabra = palabras[0]
                    palabras.remove(palabra)
                else:
                    aux = Vertical
                    Vertical = ponerPalabra(Vertical, verificarFilaVacia(Vertical)[1], palabra, len(Vertical))
                    sopa = ponerVertical(sopa, Vertical, Fila, Columna)
                    if Vertical != aux:
                        palabra = palabras[0]
                        palabras.remove(palabra)
                sopa = rotarSopa3(sopa)
        if not(palabras):
            sopa = rellenar_sopa(sopa)
            if buscar_palabras_repetidasD1(sopa, palabras):
                sopa = generarSopa_vacia(dimension)
                palabras = aux
        intentos += 1
    if intentos >= 100:
        print("No es posible generar la sopa")
        return
    else:
        for word in sopa:
            print(word)
    
# main: None -> None
# Funcion principal, pide el nombre del archivo, usa las funciones respectivas
# y dependiendo la complejidad, corre la funcion que le corresponde

def main():
    # Se leen los archivos del txt
    Valor = False
    while (not Valor):
        fileName = input("Ingrese el nombre del archivo: ")
        try:
            archivo = open(fileName, "r")
            Valor = True 
        except FileNotFoundError:
            print("Archivo no existente, ingrese bien el nombre, o caso contrario ingrese\
 el path completo del archivo")
    # Se clasifican los datos
    File = archivo.readlines()
    datos = leerArchivo(File)
    archivo.close()
    dimension = int(datos[0])
    palabras = datos[1]
    palabras = sorted(palabras, key=len)
    palabras = palabras[::-1]
    complejidad = int(datos[2])
    # Se verifica si se puede generar la sopa
    for word in palabras:
        if len(word) > dimension:
            print("No es posible genererar la sopa")
            return
    # Se genera la sopa aleatoriamente
    print("Palabras a encontrar: ")
    for palabra in palabras:
        print(palabra)
    print("\n\n")
    if complejidad == 0:
        Dificultad0(dimension, palabras)
    elif complejidad == 1:
        Dificultad1(dimension, palabras)
    elif complejidad == 2:
        Dificultad2(dimension, palabras)
    elif complejidad == 3:
        Dificultad3(dimension, palabras)
    
main()