import Card

class Partida():
    
    def __init__(self,jugadores):
        self.turnos = turnos
        self.jugadores = []
        self.equipos = (Equipo1,Equipo2)
    
    
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
            for 
         