class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    
    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual != None:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
    
    def __len__(self):
        return self.tamanio

    def esta_vacia(self):
        return self.cabeza == None
    
    
    def agregar_al_inicio(self, datos):
        nodo_nuevo = Nodo(datos)
        if self.esta_vacia():
            self.cabeza = self.cola = nodo_nuevo
        else:
            nodo_nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nodo_nuevo
            self.cabeza = nodo_nuevo
        self.tamanio += 1

    def agregar_al_final(self, datos):
        nodo_nuevo = Nodo(datos)
        if self.esta_vacia():
            self.cabeza = self.cola = Nodo(datos)
        else:
            self.cola.siguiente = nodo_nuevo
            nodo_nuevo.anterior = self.cola
            self.cola = nodo_nuevo
        self.tamanio += 1



    
    def tamano(self):
        return self.tamanio

    
    def insertar(self, datos, posicion=None ):
        if posicion == None or posicion >= self.tamanio:
            self.agregar_al_final(datos)
        elif posicion == 0 or self.esta_vacia():
            self.agregar_al_inicio(datos)
        elif posicion < 0:
            raise RuntimeError("En esa posicion no se debe usar un numero con signo negativo ")
        else:
            nodo_nuevo = Nodo(datos)
            
            if posicion <= (self.tamanio/2):
                nodo_anterior = self.cabeza
                for _ in range(1,posicion):
                    nodo_anterior = nodo_anterior.siguiente
            else:
                nodo_anterior = self.cola
                for _ in range((self.tamanio-posicion)):
                    nodo_anterior = nodo_anterior.anterior

            nodo_siguiente = nodo_anterior.siguiente
            nodo_nuevo.siguiente = nodo_siguiente
            nodo_nuevo.anterior = nodo_anterior
            nodo_anterior.siguiente = nodo_nuevo
            nodo_siguiente.anterior = nodo_nuevo
            self.tamanio += 1


   
    def extraer(self, posicion=None):
        if posicion is None:
            if self.tamanio == 0:
                raise IndexError("La lista está vacía, no se puede extraer ningún elemento.")
            
            dato = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola is not None:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            if posicion < -1 or posicion >= self.tamanio:
                raise IndexError('Indice fuera de rango.')
            
            if posicion == -1:  # Manejar la posición -1
                dato = self.cola.dato
                self.cola = self.cola.anterior
                self.cola.siguiente = None

            elif posicion == 0: # si posicion es 0
                dato = self.cabeza.dato
                self.cabeza = self.cabeza.siguiente
                if self.cabeza is not None:
                    self.cabeza.anterior = None
                else:
                    self.cola = None

            elif posicion == self.tamanio - 1: #si posicion es igual al tamanio
                dato = self.cola.dato
                self.cola = self.cola.anterior
                self.cola.siguiente = None
            else: # caso donde busque la posicion
                actual = self.cabeza
                indice = 0
                while indice < posicion:
                    actual = actual.siguiente
                    indice += 1
                dato = actual.dato
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
        
        self.tamanio -= 1
        return dato



    def copiar(self):
        copia_lista = ListaDobleEnlazada()
        actual = self.cabeza

        while actual != None:
            copia_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente

        return copia_lista

        
    def invertir(self):
        if self.tamanio == 0:
            raise RuntimeError("Lista vacía")
        else:
            nodo = self.cabeza

            for i in range(self.tamanio):
                datos = nodo.dato
                self.agregar_al_inicio(datos)
                nodo = nodo.siguiente
                self.extraer(i+1)

    def ordenar(self):
        # Primera llamada a otro metodo, pasandole la posicion 0 que será la cabeza del nodo
        # y el final que sería la cola
        if not self.esta_vacia():
            self.ordenar_aux(0,self.tamanio-1)
        else:
            raise RuntimeError("Lista vacía")  
        
    def ordenar_aux(self,primero,ultimo):
        if primero < ultimo:
            # Lo segundo es llamar a la función quick_sort que va a ordenar y retornar
            # un punto para dividir la lista
            puntoDivision = self.particion(primero,ultimo)
            # Luego de dividir la lista, se llama a si misma para repetir el proceso de puntoDivision pero en
            # la primera mitad
            self.ordenar_aux(primero,puntoDivision-1)
            # Por ultimo, se llama de nuevo pero se invierten los valores para que ordene la segunda mitad
            self.ordenar_aux(puntoDivision+1,ultimo)     
    
    
    def particion(self,primero,ultimo):
        # En esta sección, determinamos los nodos a usar como pivote, izquierda y derecha
        # según los índices dados y la posición de los nodos en la lista.

        # Si los índices son los extremos de la lista, usamos la cabeza y la cola.
        if primero == 0 and ultimo == self.tamanio-1:
            nodo_pivote = self.cabeza
            nodo_Izq = self.cabeza.siguiente
            nodo_Der = self.cola
        else:
        # Si los índices no son los extremos, encontramos los nodos correspondientes.
            if primero < (self.tamanio/2):
                nodo_pivote = self.cabeza
                for _ in range(primero):
                    nodo_pivote = nodo_pivote.siguiente
                nodo_Izq = nodo_pivote.siguiente
            else:
                nodo_pivote = self.cola
                for _ in range(((self.tamanio - 1) - primero)):
                    nodo_pivote = nodo_pivote.anterior
                nodo_Izq = nodo_pivote.siguiente

            if ultimo > (self.tamanio/2):
                nodo_Der = self.cola
                for _ in range(((self.tamanio - 1) - ultimo)):
                    nodo_Der = nodo_Der.anterior
            else:
                nodo_Der = self.cabeza
                for _ in range(ultimo):
                    nodo_Der = nodo_Der.siguiente
        marcaIzq = primero + 1
        marcaDer = ultimo

        hecho = False
        while not hecho:

            while marcaIzq <= marcaDer and nodo_Izq.dato <= nodo_pivote.dato:
                nodo_Izq = nodo_Izq.siguiente
                marcaIzq += 1
            while nodo_Der.dato >= nodo_pivote.dato and marcaDer >= marcaIzq:
                nodo_Der = nodo_Der.anterior
                marcaDer -=1

            if marcaDer < marcaIzq:
                hecho = True

            else:
                dato_Temp = nodo_Izq.dato
                nodo_Izq.dato = nodo_Der.dato
                nodo_Der.dato = dato_Temp

        dato_Temp = nodo_pivote.dato
        nodo_pivote.dato = nodo_Der.dato
        nodo_Der.dato = dato_Temp

        return marcaDer        

    def concatenar(self,lista):
        if self.tamanio > 0 and len(lista) > 0:
            # Se copia la lista del parametro, para que no sea modificada 
            lista_2_copia = lista.copiar()
            # Se toma la cabeza de la lista copiada
            cabeza_lista_2 = lista_2_copia.cabeza
            # Luego la cola de la lista actual
            ultimo_nodo_lista_1 = self.cola

            # Posteriormente se conecta la cola de la lista actual con la cabeza de la lista copiada
            # y se actualiza la cola de la lista actual para que apunte a la cola de la lista copiada
            ultimo_nodo_lista_1.siguiente = cabeza_lista_2
            cabeza_lista_2.anterior = ultimo_nodo_lista_1
            self.cola = lista_2_copia.cola

            # Por otro lado, se suma el tamanio de la lista copiada a la actual
            self.tamanio += len(lista)
        else:
            raise RuntimeError("Una de las listas vacía")
    def __add__(self,lista):
        if self.tamanio > 0 and len(lista) > 0: 
            lista_concatenada = self.copiar()
            lista_concatenada.concatenar(lista)

            return lista_concatenada
        else:
            raise RuntimeError("Una de las listas vacía")

    def __str__(self):
        string = ""
        nodo = self.cabeza
        while nodo != None:
            string += str(nodo.dato)
            string += " "
            nodo = nodo.siguiente
        return string    
       