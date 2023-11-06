def merge_sort(nombre_archivo, tam_bloque):
    def mezclar(izquierda, derecha):
        mezclado = []
        i, j = 0, 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] <= derecha[j]:
                mezclado.append(izquierda[i])
                i += 1
            else:
                mezclado.append(derecha[j])
                j += 1
        mezclado.extend(izquierda[i:])
        mezclado.extend(derecha[j:])
        return mezclado

    def ordenar_y_escribir(bloque):
        bloque.sort()
        with open(nombre_archivo, 'a') as archivo:
            archivo.write('\n'.join(map(str, bloque)) + '\n')

    # Paso 1: Leer el archivo y dividirlo en bloques
    bloques = []
    with open(nombre_archivo, 'r') as archivo:
        bloque = []
        for linea in archivo:
            bloque.append(int(linea))
            if len(bloque) == tam_bloque:
                bloques.append(bloque)
                bloque = []
        if bloque:
            bloques.append(bloque)

    # Paso 2: Ordenar cada bloque por separado
    for bloque in bloques:
        ordenar_y_escribir(bloque)

    # Paso 3: Mezclar los bloques ordenados
    with open(nombre_archivo, 'w') as archivo:
        # Inicializar una lista de iteradores para cada bloque
        iteradores = [iter(bloque) for bloque in bloques]

        # Inicializar una lista para almacenar los valores actuales de cada bloque
        valores_actuales = [next(iterador, None) for iterador in iteradores]

        while any(valores_actuales):
            min_valor = min(valor for valor in valores_actuales if valor is not None)
            archivo.write(str(min_valor) + '\n')

            min_indice = valores_actuales.index(min_valor)
            valores_actuales[min_indice] = next(iteradores[min_indice], None)

merge_sort('datos.txt', 100000)