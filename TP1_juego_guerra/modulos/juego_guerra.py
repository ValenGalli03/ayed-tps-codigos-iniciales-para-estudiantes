from random import shuffle
from ListaDoblementeEnlazada.lista_doblemente_enlazada import ListaDobleEnlazada


valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
palos = ["♠", "♥", "♦", "♣"]

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return str(self.valor) + str(self.palo)

    def __repr__(self):
        return self.__str__()
    
class JuegoGuerra:
    def __init__(self):
        self.turno = 1
        self.guerra = False
        self.mazo = Mazo()
        self.Player1 = Mazo()
        self.Player2 = Mazo()
        self.mesa = Mazo()
        self.string_cartas = ""

    def repartir(self):
        for i in range(1, 53):
            carta = self.mazo.sacar_arriba()
            # Se reparte para que nunca se le repartan 2 al mismo 
            if i % 2 == 0:
                self.Player1.poner_arriba(carta)
            else:
                self.Player2.poner_arriba(carta)

    def iniciar_guerra(self,carta1,carta2):
        self.mesa.poner_abajo(carta1)
        self.mesa.poner_abajo(carta2)
        # tienen suficientes cartas? si/no
        if len(self.Player1.mazo) < 4 or len(self.Player2.mazo) < 4:
            return True
        for _ in range(3):
            self.mesa.poner_abajo(self.Player1.sacar_arriba())
            self.mesa.poner_abajo(self.Player2.sacar_arriba())

    def comparar_cartas(self, carta1, carta2):
        Valor1 = valores.index(carta1.valor) + 2
        Valor2 = valores.index(carta2.valor) + 2
        # El valor mayor sera el ganador 
        if Valor1 > Valor2:
           
            #Si, solo si inicia una guerra que seria verdad guerra y valor 1 mayor al 2
            # se le repartirian las cartas al player1 en este caso 
           
            if self.guerra:
                for _ in self.mesa.mazo:
                    self.Player1.poner_abajo(self.mesa.sacar_arriba())
                self.Player1.poner_abajo(carta1)
                self.Player1.poner_abajo(carta2)

                # Luego de repartir, cambia el estado de guerra 

                self.guerra = False
                self.string_cartas = ""
            # Si guerra = Flase se ejecutaría el else y se reparte normal
            else:
                self.Player1.poner_abajo(carta1)
                self.Player1.poner_abajo(carta2)

        elif Valor1 < Valor2:
            if self.guerra:
                for _ in self.mesa.mazo:
                    self.Player2.poner_abajo(self.mesa.sacar_arriba())
                self.Player2.poner_abajo(carta1)
                self.Player2.poner_abajo(carta2)
                self.guerra = False
                self.string_cartas = ""
            else:
                self.Player2.poner_abajo(carta1)
                self.Player2.poner_abajo(carta2)
       
        #como no hay ganador, cambia y entra en iniciar guerra 
        else:
            self.guerra = True

    def iniciar_juego(self):
        self.mazo.mezclar()
        self.repartir()

        while self.turno <= 10000:
            # Se prueba constantemente el tamaño de los mazos por precaucion 
            if  self.Player1.mazo.tamanio == 0 or self.Player2.mazo.tamanio == 0:
                break
           
            carta1 = self.Player1.sacar_arriba()
            carta2 = self.Player2.sacar_arriba()

            # input("Presiona Enter para avanzar al siguiente turno...")
                            # Este bloque imprimpe la interfaz
            #------------------------------------------------------------------------
            print("--------------------------------------")

            
            if self.guerra:
                print(" "*20,"**** Guerra!! ****")

            print("Turno: ", self.turno)
            print("Jugador 1:")
            # Imprimo las cartas boca abajo del mazo del jugador 1 según su cantidad
            for i in range(len(self.Player1.mazo)):
                if i % 10 == 0 and i != 0:
                    print()  # Salto de línea después de cada 10 cartas
                print("-X", end=" ")  # Imprime la carta, sin salto de línea

            print("\n")
            # Se muestran todas las cartas de la guerra
            if self.guerra:
                self.string_cartas += " " + "-X"*6+ " " + str(carta1) + " " + str(carta2)
                print(" "*10,self.string_cartas)
            # Y si no hay guerra, se guarda en string_cartas lo cual ayuda en el momento de guerra
            else:
                self.string_cartas = str(carta1) + " " + str(carta2)
                print(" "*10, self.string_cartas)

            print("\n")
            print("Jugador 2:")
            # Imprimo las cartas boca abajo del mazo del jugador 2 según su cantidad
            for i in range(len(self.Player2.mazo)):
                if i % 10 == 0 and i != 0:
                    print()  # Salto de línea después de cada 10 cartas
                print("-X", end=" ")  # Imprimir carta, sin salto de línea

            print("\n--------------------------------------")
            #------------------------------------------------------------------------
            self.turno += 1
            # Primero compara las cartas
            self.comparar_cartas(carta1,carta2)
            # Y después comprueba si guerra cambió a True
            if self.guerra:
                # En el caso de que uno de los mazos no tenga suficientes cartas
                # devuelve True y se rompe el while
                if self.iniciar_guerra(carta1,carta2):
                    break

        else:
            return print(" "*16+"****** Empate ******")
        # Si el mazo del Player1 == 0 o el mismo posea menos cartas que el Player2
        # (en el caso de que entren en guerra y tenga menos de 4 cartas) gana el 2
        if self.Player1.mazo.tamanio == 0 or self.Player2.mazo.tamanio > self.Player1.mazo.tamanio:
            print(" "*8,"****** Jugador 2 gana la partida ******")
        elif self.Player2.mazo.tamanio == 0 or self.Player1.mazo.tamanio > self.Player2.mazo.tamanio:
            print(" "*8, "****** Jugador 1 gana la partida ******")

class Mazo:
  def __init__(self):
    self.mazo= ListaDobleEnlazada() #se usa la lista doblemente enlazada para el mazo

  def generar_mazo(self):
    for palo in palos: #Se le agregan las cartas con los valores y palos al mazo
      for valor in valores:
          self.mazo.agregar_al_final(Carta(valor,palo))

  def barajar(self):
    self.generar_mazo()
    cartas_lista = list(self.mazo)
    shuffle(cartas_lista) #mezclamos las cartas
    self.mazo = ListaDobleEnlazada()
    for carta in cartas_lista:
      self.mazo.agregar_al_final(carta)

  def repartir(self):
    Player1 = Mazo() #Se le asignan a los jugadores los metodos de Mazo
    Player2 = Mazo()
    for x,carta in enumerate(self.mazo): #Se itera sobre el mazo y se reparten las cartas para cada jugador
      if x % 2 == 0:
        Player1.poner_arriba(carta)
      else:
        Player2.poner_arriba(carta)
    return Player1, Player2

  def poner_arriba(self, carta):
    self.mazo.agregar_al_inicio(carta)

  def poner_abajo(self, carta):
    self.mazo.agregar_al_final(carta)

  def sacar_arriba(self, jugador=None):
    if not self.mazo.esta_vacia():
        return self.mazo.extraer(0)
    else:
        otro_jugador = 1 if jugador == 2 else 2
        self.ganador = otro_jugador
        print(f"El jugador {jugador} se quedó sin cartas para continuar con el juego")
        print(f"\n                               ***** Jugador {otro_jugador} gana la partida *****")
        exit(1) #si un jugador no tiene cartas para jugar, se termina el juego
  
  def __iter__(self):
    return iter(self.mazo)



