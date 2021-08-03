import numpy
import Card
import Jugador



class Partida():
    
    def __init__(self,jugadores):
        self.turnos = turnos
        self.jugadores = []
        self.equipos = (1,2)
        self.puntos = {1:0,2:0}
        self.mesa = []
    
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
        

                    
    