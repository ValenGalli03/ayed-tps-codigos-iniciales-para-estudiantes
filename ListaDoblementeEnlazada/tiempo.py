import random
import time
import matplotlib.pyplot as plt
from lista_doblemente_enlazada import ListaDobleEnlazada

def generar_lista_aleatoria(tamano):
    lista = []
    for _ in range(tamano):
        lista.append(random.randint(1, 100))
    return lista

def analizar_orden_complejidad(tamano_lista):
    lista_aleatoria = generar_lista_aleatoria(tamano_lista)
    lista_doble_enlazada = ListaDobleEnlazada()
    for elemento in lista_aleatoria:
        lista_doble_enlazada.agregar_al_final(elemento)
    
    inicio = time.time()
    lista_doble_enlazada.ordenar()
    fin = time.time()
    
    tiempo_transcurrido = fin - inicio
    return tamano_lista, tiempo_transcurrido

def graficar_orden_complejidad(tamanos_lista, tiempos_transcurridos):
    plt.plot(tamanos_lista, tiempos_transcurridos)
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo transcurrido (segundos)')
    plt.title('Orden de complejidad del algoritmo de ordenamiento')
    plt.show()