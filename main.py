import numpy
import Card
import Jugador
import Mesa 



class Partida():
    
    def __init__(self,turnos):
        self.turnos = turnos
        self.jugadores = []
        self.equipos = (1,2)
        self.puntos = {1:0,2:0}
        self.mesa = []
        self.sub_partidas = 0
        self.orden_de_partida = []
    
    def inicio_variables(self,cantidad_jugadores):
        """
        [Inicio todas las variables del juego]

        Args:
            cantidad_jugadores ([type]): [description]
        """
        if cantidad_jugadores == 2:
            
            jugador1 = Card.Jugador()
            jugador2 = Card.Jugador()
            lista_jugadores =[jugador1,jugador2]
            for i in lista_jugadores:
                self.jugadores.append(i)
            
        
        elif cantidad_jugadores == 4:
            jugador1 = Card.Jugador()
            jugador2 = Card.Jugador()
            jugador3 = Card.Jugador()
            jugador4 = Card.Jugador()
            
            lista_jugadores =[jugador1,jugador2,jugador3,jugador4]
            for i in lista_jugadores:
                self.jugadores.append(i)

        
    def armar_equipo(self):
        """
        Metodo que elige aleatoriamente los equipos de los jugadores
        """   
        
        if len(self.jugadores) == 4:
        
            for i in self.jugadores:
                valor = numpy.random.randint(0,1)
                if valor == 1 and lista_valores.count(valor) == 2:
                    i.equipo = 2
                elif valor == 2 and lista_valores.count(valor) == 2:
                    i.equipo = 1
                else:
                    i.equipo = valor
        
        elif len(self.jugadores) == 2:
            self.jugadores[0].equipo = 1
            self.jugadores[1].equipo = 2
        
        
        
    def primer_turno(self):
        """
        Este metodo comprueba que estemos en la primer sub-partida.
        Una subpartida es cuando se terminan de jugar las cartas, se canta todo y 
        se vuelve a mezclar. Es un fin de ciclo de juego.
        Este metodo activa el booleano de turno del jugador 
        """
        
        if self.sub_partidas == 0:
            if len(self.jugadores) == 2:
                jugador_primer_turno = numpy.random.randint(1,2)
                if jugador_primer_turno == 1:
                    self.jugadores[0].turno = True
                else:
                    self.jugadores[1].turno = True                  
            elif len(self.jugadores) == 4:
                jugador_primer_turno = numpy.random.randint(1,4)
                
                if jugador_primer_turno == 1:
                    self.jugadores[0].turno = True
                
                elif jugador_primer_turno == 2:
                    self.jugadores[1].turno = True
                
                elif jugador_primer_turno == 3:
                    self.jugadores[2].turno = True
                
                else:
                    self.jugadores[3].turno = True
                    
                
    def orden_de_juego_primer_partida(self):
        """
        Esta funcion busca ordenar a los jugadores para la primer 
        subpartida.
        """            
        
        orden_terminado = False
        
        #Con este for pongo al primer jugador en el orden
        for jugador in self.jugadores:
            if jugador.turno == True:
                self.orden_de_partida.append(jugador)
                jugador.posicion = 1
        
        
        if self.jugadores == 2:
            self.orden_de_partida.append(self.jugadores[1])
        
        elif self.jugadores == 4:
            
            contador = 0
            
            while len(self.orden_de_partida) != 4:
                for jugador in self.jugadores:
                    if jugador == self.orden_de_partida[0]:
                        continue
                    else:
                        if jugador.equipo != self.orden_de_partida[0].equipo and contador == 0:
                            self.orden_de_partida.append(jugador)
                            contador += 1
                        elif jugador.equipo == self.orden_de_partida[0].equipo and contador == 0:
                            continue
                        
                        elif jugador.equipo == self.orden_de_partida[0].equipo and contador == 1:
                            self.orden_de_partida.append(jugador)
                            contador += 1
                        
                        elif jugador.equipo != self.orden_de_partida[0].equipo and contador == 1:
                            continue
                            
                        elif jugador.equipo != self.orden_de_partida[0].equipo and contador == 2:
                            self.orden_de_partida.append(jugador)
                            contador += 1
                        
                        elif jugador.equipo == self.orden_de_partida[0].equipo and contador == 2:
                            continue
                            
                            
    def orden_juego_distintas_partidas(self):
        """
        Este metodo es invocado para cambiar el orden de juego de los jugadores
        
        """            
        
        if len(self.jugadores) == 2:
            
            for jugador in self.jugadores:
                if jugador.posicion == 2:
                    jugador.posicion = 1
                elif jugador.posicion == 1:
                    jugador.posicion = 2

        elif len(self.jugadores) == 4:
            for jugador in self.jugadores:
                if jugador.posicion != 4:
                    jugador.posicion += 1
                else:
                    jugador.posicion = 1
        
                    
    @classmethod
    def jugar(cls):
        """
        Este metodo ejecuta la partida del juego
        """            

        cantidad_jugadores = input("De cuantos jugadores queres hacer la partida")
        
        while cantidad_jugadores != ["2","4"]:
            print("Jugadores mal introducidos, puede jugar de a 2 o de a 4")
            cantidad_jugadores = input("De cuantos jugadores queres hacer la partida")
        
        mesa = Mesa()
        
        mesa.iniciar_variables(cantidad_jugadores)
        
        mesa.armar_equipo()
        
        in_game = True
        
        while in_game == True:
            if self.sub_partidas == 0:
                
                mesa.orden_de_juego_primer_partida()
                
                #Armar la logica de los turnos
                
        
        
                          