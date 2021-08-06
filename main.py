import numpy
import Card
import Jugador
import Mesa 
import Mazo

class Partida():
    
    def __init__(self,turnos):
        self.turnos = turnos
        self.jugadores = []
        # Esta tupla de self.equipos no tiene uso, podria analizar quitarla
        self.equipos = (1,2)
        self.puntos = {1:0,2:0}
        self.sub_partidas = 0
        
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
        
        # ver aca como juegan las variables por defecto de la clase
        
        if cantidad_jugadores == 2:
            
            jugador1 = Jugador.Jugador()
            jugador2 = Jugador.Jugador()
            lista_jugadores =[jugador1,jugador2]
            
            for i in lista_jugadores:
                self.jugadores.append(i)
            
        
        elif cantidad_jugadores == 4:
            jugador1 = Jugador.Jugador()
            jugador2 = Jugador.Jugador()
            jugador3 = Jugador.Jugador()
            jugador4 = Jugador.Jugador()
            
            lista_jugadores =[jugador1,jugador2,jugador3,jugador4]
            for i in lista_jugadores:
                self.jugadores.append(i)
        
        
        
    def armar_equipo(self):
        """
        Metodo que elige aleatoriamente los equipos de los jugadores
        """   
        
        
        
        
        if len(self.jugadores) == 4:
        
            jugadores_asignados = 0
            
            for i in self.jugadores:
                               
                valor = numpy.random.randint(0,1)
                if i == self.jugadores[0]:
                    
                    if valor == 1 and lista_valores.count(valor) == 2:
                        i.equipo = 2
                        jugadores_asignados += 1
                    elif valor == 2 and lista_valores.count(valor) == 2:
                        i.equipo = 1
                        jugadores_asignados += 1
                
                if jugadores_asignados == 1:
                    
                    if self.jugadores[0].equipo ==1:
                        i.equipo = 2
                        jugadores_asignados += 1
                    else:
                        i.equipo = 1 
                        jugadores_asignados +=1
                
                elif jugadores_asignados == 2:
                    i.equipo = self.jugadores[0].equipo
                    jugadores_asignados +=1
                 
                elif jugadores_asignados == 3:
                    i.equipo = self.jugadores[1].equipo   
                
                
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
        
        orden_de_partida = []
        
        for jugador in self.jugadores:
            if jugador.turno == True:
                orden_de_partida.append(jugador)
                jugador.posicion = 1
        
        
        if self.jugadores == 2:
            orden_de_partida.append(self.jugadores[1])
        
        elif partida.jugadores == 4:
            
            contador = 0
            
            while len(self.orden_de_partida) != 4:
                
                for jugador in self.jugadores:
                    if jugador == self.orden_de_partida[0]:
                        continue
                    else:
                        if jugador.equipo != orden_de_partida[0].equipo and contador == 0:
                            orden_de_partida.append(jugador)
                            jugador.posicion = 2
                            contador += 1
                        elif jugador.equipo == orden_de_partida[0].equipo and contador == 0:
                            continue
                        
                        elif jugador.equipo == orden_de_partida[0].equipo and contador == 1:
                            orden_de_partida.append(jugador)
                            jugador.posicion = 3
                            contador += 1
                        
                        elif jugador.equipo != orden_de_partida[0].equipo and contador == 1:
                            continue
                            
                        elif jugador.equipo != orden_de_partida[0].equipo and contador == 2:
                            orden_de_partida.append(jugador)
                            jugador.posicion = 4
                            contador += 1
                        
                        elif jugador.equipo == orden_de_partida[0].equipo and contador == 2:
                            continue
                            
                # Aca estoy armando una lista de jugadores identica a la de self.jugadores, deberia optimizar esto
        
        self.jugadores = orden_de_partida
                            
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
    
    
    def opciones_de_juego(self,objeto_jugador):
        """
        Esta funcion a extender le consulta al usuario que quiere hacer
        en su turno
        En esta version puede hacer 3 cosas:
        A - Jugar callado
        B - Cantar envido
        C - Cantar truco
        
        """
        print("1 - Jugar callado")
        print("2 - Cantar envido")
        print("3- Cantar truco")
        
        opcion = input("¿Que desea hacer?")
        
        while opcion not in ["1","2","3"]:
            print("opcion mal introducida")
            opcion = input("¿Que desea hacer?")

        opcion = int(opcion)
        
        return opcion
        
        
        ###################################
        ## METO LAS FUNCIONES DEL ENVIDO ##
        ###################################   
    
    def circuito_envido(self,objeto_jugador):
        """
        Esta funcion es la Padre del envido, arma el circuito completo de esta
        parte del juego
        
        
        Args:
            objeto_jugador ([Obj]): [Es un objeto de la clase jugador, es el jugador que canta el envido]
        """

        # me fijo si algun jugador del equipo contrario acepta o no
        
        aceptacion = False
        
        for jugador in self.jugadores:
            if jugador == objeto_jugador:
                continue
            elif jugador.equipo == objeto_jugador.equipo:
                # aca verifico que un un jugador del mismo equipo no tenga la chance de aceptar o rechazar el tanto
                continue
            else:
                #funcion para mostrar el tablero del envido con las opciones del jugador---> tengo que referenciar al jugador 
                respuesta = self.opciones_envido()
                
                # Aca pueden aceptar / cantar envido / cantar real envido / cantar falta envido / rechazar
                puntos_disputa = 1
                
                if respuesta == 1:
                    
                    #aceptacion
                    puntos_disputa = 2
                    jugador_ganador = self.mostrar_puntos_envido()
                    
                    self.sumar_puntos_envido_partida(objeto_jugador = jugador_ganador, puntos = puntos_disputa)
                
                elif respuesta == 2:
                    print("Resolver el circuito de envido - envido ")
                
                elif respuesta == 5:
                    
                    #rechazo
                    
                    print("espera sentado")
                    self.rechazo_envido(objeto_jugador = jugador, puntos = puntos_disputa)
                    
                

    def opciones_envido(self):
        
        """
        Esta funcion muestra las opciones de envido del jugador 
        """
        
        print("Opcion 1: Aceptar")
        print("Opcion 2: Cantar envido")
        print("Opcion 3: Cantar real envido")
        print("Opcion 4: Cantar falta envido")
        print("Opcion 5: Rechazar")
        
        respuesta = input("Elija una opcion: ")
        
        while respuesta != ["1","2","3","4"]:
            print("opcion mal introducida")
            respuesta = input("Elija una opcion: ")
        
        return respuesta
    
    
    def rechazo_envido(self,objeto_jugador,puntos):
        
        """
        Asigno los puntos en caso de rechazar el envido
        
        Args:
            Objeto_jugador = Es el jugador que rechaza el envido
        """

        #Escenario 1 ---> Rechazo de un envido común
        
        if objeto_jugador.equipo == 1:
            self.puntos[2] += puntos
        elif objeto_jugador.equipo == 2:
            self.puntos[1] += puntos
            
    def mostrar_puntos_envido(self):
        """
        Esta funcion crea la forma de mostrar los puntos de envido
        de cada jugador y los muestra y dice quien gano. Retorna el jugador ganador.
        Resuelve = visualizacion de tanto, ganador del tanto con y sin parda
        
        """        
        
        for jugador in self.jugadores:
            if jugador.puntos_envido == 1:
                print("El jugador {} tiene {} punto".format(jugador.nombre,jugador.puntos_envido))
            
            else:
                print("El jugador {} tiene {} puntos".format(jugador.nombre,jugador.puntos_envido))
                
        
        puntos_totales = -1
        nombre_jugador = ""
        for jugador in self.jugadores:
            if puntos_totales < jugador.puntos_envido:
                puntos_totales = jugador.puntos_envido
                nombre_jugador = jugador.nombre
                jugador_aux = jugador
            elif puntos_totales == jugador.puntos_envido:
                
                if jugador_aux.posicion < jugador.posicion:
                    
                    puntos_totales = jugador.puntos_envido
                    nombre_jugador = jugador.nombre
                    jugador_aux = jugador
                
                else:
                    continue
                         
            else:
                continue
                
        print("El jugador {} ganó el envido".format(nombre_jugador))         
            
         
         #con el codigo de abajo asigno los puntos, pero es mejor usar una funcion aparte
         #self.puntos[jugador_aux.equipo] += 2    
            
        return jugador_aux
    
    def sumar_puntos_envido_partida(self,objeto_jugador,puntos):
        ### Tengo que resolver como le paso los puntos a adicionar
        """
        Esta funcion asigna los puntos ganados por el envido al equipo del jugador ganador

        Args:
            objeto_jugador ([Object Jugador]): [Objeto de la clase jugador ganador de la partida]
        """
        
        self.puntos[objeto_jugador.equipo] += puntos 
        
        
                    
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
        
        mazo = Mazo.Mazo()
        
        mazo.crear_mazo()
        
        partida.inicio_variables(cantidad_jugadores)
        
        partida.asignar_primer_turno_aleatoriamente()
        
        partida.armar_equipo()
        
        in_game = True
        
        while in_game == True:
            
            # Tengo que armar el circuito de reparto de cartas y de ahi asignar los puntos envido de los jugadores
            
            if partida.cantidad_jugadores_partida() == 2:
                
                if partida.primer_turno() == True:
                    
                    partida.orden_de_juego_primer_partida() 
                    
                    partida.turnos = 0
                    
                    for idx,jugador in enumerate(partida.jugadores):
                        #verifico de quien es el turno
                        if partida.turnos == 1:
                            if jugador.turno == True:
                                #Le pido al jugador que carta quiere tirar a la mesa ---> Crear un método que busque la carta en la mano y la tire.
                                carta = Jugador.jugador.elegir_carta_a_tirar()
                                
                                Jugador.jugador.jugar_carta_elegida(objeto_mesa = mesa,carta_del_jugador = carta)
                                
                                jugador.perder_turno()
                                
                                jugador[idx +1].ganar_turno()
                            
                            partida.turnos += 1
                        
                        elif partida.turno == 2:
                            # puede cantar envido / cantar truco / jugar callado
                            opcion = partida.opciones_de_juego()
                            
                            if opcion == 1:
                                
                                partida.circuito_envido()
                                
                                      
                            elif opcion == 2:
                                print("desarrollar logica truco")
                            elif opcion == 3:
                                print("Logica de jugar la carta")
                                
                                
               
                    
