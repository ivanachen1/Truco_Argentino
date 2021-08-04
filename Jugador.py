class Jugador():
    def __init__(self,mano,cartas,equipo,posicion,nombre):
        """[summary]

        Args:
            cantidad ([int]): [Cantidad de jugadores]
            cartas ([list]): [Son las cartas del jugador]
        """
        self.cartas = []
        self.equipo = None
        self.posicion = 0
        self.turno = False
        self.nombre = nombre
    
    def show_mano_del_jugador(self,mano):
        """
        Muestro la mano del jugador
        
        """
        if len(self.cartas) == 0:
            print("El jugador no tiene cartas")
        else:
            for carta in enumerate(self.cartas):
                print(carta.nombre_carta)
    
    def jugar_carta_elegida(self,objeto_mesa,carta_del_jugador):
        """
        Esta funcion quita una carta de la mano del jugador
        y la coloca en la mesa del juego
        
        Args: Le paso como argumento un objeto Mesa
        """
        
        self.mano.remove(carta_del_jugador)
        objeto_mesa.cantidad_cartas += 1
        objeto_mesa.cartas.append(carta_del_jugador)
    
    def perder_turno(self):
        
        """
        Este metodo le quita el turno a un jugador
        
        """
        
        self.turno = False
    
    def ganar_turno(self):
        
        """
        Este metodo le otorga el turno a un jugador
        """
        
        self.turno = True
    
    def elegir_carta_a_tirar(self):
        """
        Este metodo le pide al jugador el numero de carta  
        """
        
        indice = input("Coloque el numero de carta a tirar: ")
        
        while indice > len(self.cartas):
            print("Ha colocado un numero incorrecto")
            indice = input("Coloque el numero de carta a tirar: ")
        
        indice -= 1
        
        for idx,carta in enumerate(self.cartas):
            if idx == indice:
                return carta
                  
          