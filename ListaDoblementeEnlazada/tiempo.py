import matplotlib.pyplot as plt
import numpy as np
import time

def ordenar(self):
        if self.cabeza is None:
            return nodo_actual = self.cabeza
        while nodo_actual:
            min_nodo = nodo_actual
            nodo_temp = nodo_actual.siguiente
            while nodo_temp:
                if nodo_temp.dato < min_nodo.dato:
                    min_nodo = nodo_temp
                nodo_temp = nodo_temp.siguiente
            
            # Intercambiar valores
            if min_nodo != nodo_actual:
                nodo_actual.dato, min_nodo.dato = min_nodo.dato, nodo_actual.dato
            
            nodo_actual = nodo_actual.siguiente    
 
# algoritmo de prueba
def algoritmo(n):
    acumulador = 0
    for i in range(n):
        for i in range(n):
            acumulador += 1

# analisis
#tam = [10, 50, 100, 500, 1000,  5000]
tam = np.logspace(10, 1000, 10)
tiempos = []

for cantidad in tam:
    tini = time.time()
    ordenar(int(cantidad))
    tfin = time.time()

    duracion = tfin - tini
    tiempos.append(duracion)

print(tiempos)

plt.plot(tam, tiempos, marker='o', linestyle='-', color='b')
plt.xlabel('Tamaño de Entrada')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Análisis de Orden de Complejidad del Algoritmo de Ordenamiento')
plt.grid(True)
plt.show()