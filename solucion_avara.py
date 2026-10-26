import sys

def contar_componentes(permutacion):
    # Mayor valor visto hasta la posición actual
    maximo = 0
    # Cantidad de componentes encontrados (cada corte cierra uno)
    componentes = 0
 
    for i in range(len(permutacion)):
        # Actualizar el máximo del prefijo
        if permutacion[i] > maximo:
            maximo = permutacion[i]
 
        # La posición real es i + 1 porque el índice empieza en 0.
        # Si el máximo coincide con la posición, el prefijo es {1..i+1}
        # y por lo tanto aquí termina un componente.
        if maximo == i + 1:
            componentes += 1
 
    return componentes

def main():
    # Leer toda la entrada de una vez, es más rápido que leer línea por línea
    lineas = sys.stdin.read().split("\n")
 
    # La primera línea indica cuántos casos de prueba hay
    casos = int(lineas[0])
 
    resultados = []
    for k in range(1, casos + 1):
        # Cada línea siguiente es una permutación con los números separados por espacio
        permutacion = list(map(int, lineas[k].split()))
        resultados.append(str(contar_componentes(permutacion)))
 
    # Imprimir una respuesta por línea
    print("\n".join(resultados))

main()