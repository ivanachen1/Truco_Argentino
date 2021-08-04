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
        
    @classmethod 
    def crear_partida(cls):
        """
        Este metodo crea un objeto de la clase partida y lo retorna
        """
    
        partida = Partida()
        
        return partida
        
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
        # Recordar = Declare la variable partida como global
        
        if self.sub_partidas == 0:
            return True
        else:
            return False
           
                    
                
    def orden_de_juego_primer_partida(self):
        """
        Esta funcion busca ordenar a los jugadores para la primer 
        subpartida.
        """            
        
        #Con este for pongo al primer jugador en el orden
        
        for jugador in self.jugadores:
            if jugador.turno == True:
                self.orden_de_partida.append(jugador)
                jugador.posicion = 1
        
        
        if self.jugadores == 2:
            self.orden_de_partida.append(self.jugadores[1])
        
        elif partida.jugadores == 4:
            
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
        
 
    
    def asignar_primer_turno_aleatoriamente(self):
        """
        Este metodo busca aleatoriamente asignar el primer turno
        del juego, pone en True el atributo turno de un solo objeto jugador

        Args:
            lista_jugadores ([List]): [Lista de objetos de la clase jugador]
        """
        
        objeto_jugador_elegido = numpy.random.choice(self.jugadores)
        
        objeto_jugador_elegido.turno = True
        
    def cantidad_jugadores_partida(self):
        """
        Cuenta la cantidad de jugadores que hay en la partida
        """     

        if len(self.jugadores) == 2:
            return 2
        elif len(self.jugadores) == 4:
            return 4
        else:
            print("hay mas jugadores que 4,revisar")
                    
    @classmethod
    def jugar(cls):
        """
        Este metodo ejecuta la partida del juego
        """            

        cantidad_jugadores = input("De cuantos jugadores queres hacer la partida")
        
        while cantidad_jugadores != ["2","4"]:
            print("Jugadores mal introducidos, puede jugar de a 2 o de a 4")
            cantidad_jugadores = input("De cuantos jugadores queres hacer la partida")
        
        partida = Partida.crear_partida()
        
        mesa = Mesa()
        
        partida.inicio_variables(cantidad_jugadores)
        
        partida.asignar_primer_turno_aleatoriamente()
        
        partida.armar_equipo()
        
        in_game = True
        
        while in_game == True:
            
            if partida.cantidad_jugadores_partida() == 2:
                
                if partida.primer_turno() == True:
                    
                    partida.orden_de_juego_primer_partida() 
                    
                    for jugador in partida.jugadores:
                        if jugador.turno == True:
                            #Le pido al jugador que carta quiere tirar a la mesa ---> Crear un método que busque la carta en la mano y la tire.
                            carta = Jugador.jugador.elegir_carta_a_tirar()
                            #No cuento con la herramienta de seleccionar con botones. ---> Solucion = Le muestro la carta y un número para que elija ese numero
                            
                            
                            
                    # Luego tengo que pedirle al jugador que elija una carta de su mano y la tire
                    # tengo que cambiar el turno de un jugador y darselo al otro
                    # tendria que contabilizar los turnos transcurridos en la ronda asi identifico los momentos del juego para cantar o tirar
                    # 
                    

        
                          