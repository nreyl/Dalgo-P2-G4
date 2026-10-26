import sys

def contar_componentes_greedy(permutacion):
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
    # La primera línea indica cuántos casos de prueba hay
    casos = int(sys.stdin.readline())

    resultados = []
    for _ in range(casos):
        # Cada línea siguiente es una permutación con los números separados por espacio.
        # Se lee solo la cantidad de líneas necesaria, sin esperar al fin de la entrada.
        permutacion = list(map(int, sys.stdin.readline().split()))
        resultados.append(str(contar_componentes_greedy(permutacion)))
 
    # Imprimir una respuesta por línea
    print("\n".join(resultados))

main()