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
        
    def crear_jugadores(self,cantidad_jugadores,tipo_oponente):
        """
        [Inicio de los jugadores en el juego]

        Args:
            cantidad_jugadores ([int]): [Cantidad de jugadores del juego]
            tipo_oponente[Int]: Vale 1 si el resto de los jugadores son maquina. Vale 2 si el resto son humanos 
        """
            
        
        if cantidad_jugadores == 2:
            if tipo_oponente == 1:
                
                jugador_humano = Jugador.crear_jugador_real()
                jugador_maquina = Jugador.crear_jugador_maquina()
                
            
                lista_jugadores =[jugador_maquina,jugador_humano]
            
                for i in lista_jugadores:
                    self.jugadores.append(i)
            
            elif tipo_oponente == 2:
                
                for i in range(cantidad_jugadores):
                    jugador_humano = Jugador.crear_jugador_real()
                    self.jugadores.append(jugador_humano)
                
                
                
        if cantidad_jugadores == 4:
            if tipo_oponente == 1:
                
                jugador_humano = Jugador.crear_jugador_real()
                self.jugadores.append(jugador_humano)
                
                for jugador in range(3):
                    jugador_maquina = Jugador.crear_jugador_maquina()
                    self.jugadores.append(jugador_maquina)
                    
            elif tipo_oponente == 2:
                
                for i in range(4):
                    jugador_humano = Jugador.crear_jugador_real()
                    self.jugadores.append(jugador_humano)  
        
        
        
        
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
        
        envido_aceptado = False
        
        envido_falta_envido_aceptado = False
        envido_falta_envido_rechazado = False
        
        envido_envido_cantado = False
        envido_envido_rechazado = False
        envido_envido_aceptado = False
        
        envido_envido_real_envido_aceptado = False
        envido_envido_real_envido_rechazado = False
        
        envido_envido_real_envido_falta_envido_aceptado = False
        envido_envido_real_envido_falta_envido_rechazado = False
        
        
        
        for jugador in self.jugadores:
            
            if jugador == objeto_jugador:
                continue
            elif jugador.equipo == objeto_jugador.equipo:
                # aca verifico que un un jugador del mismo equipo no tenga la chance de aceptar o rechazar el tanto
                continue
            else:
                # tengo que verificar que al menos un jugador responda# Ver como optimizar esta parte    
                respuesta = self.opciones_envido(1)              
                # Aca pueden aceptar / cantar envido / cantar real envido / cantar falta envido / rechazar              
                if respuesta == 1:
                    #aceptacion
                    envido_aceptado = True
                                   
                elif respuesta == 2:
                    envido_envido_cantado = True
                    jugador_canta = jugador
                    break
                    
                elif respuesta == 5:
                    jugador_ganador = objeto_jugador
                    break
                 
                    
                    
        #print("Resolver el circuito de envido - envido ")
        #self.envido_envido_circuito(objeto_jugador_canta = jugador)            
        
        puntos_disputa = 0
        
        if envido_aceptado == True:
            puntos_disputa = 2
            
        elif envido_aceptado == False:
            puntos_disputa = 1 
            
        elif envido_envido_cantado == True:
            
            respuesta = self.envido_envido_circuito(jugador_canta)
            
            if respuesta[0] == 1:
                puntos_disputa = 4
                #Acepto
              
            elif respuesta[0] == 2:
                print("circuito")
                respuesta = self.real_envido_circuito()
                
            elif respuesta[0] == 3:
                print("Circuito")
                #se canta falta_envido
                #armar este circuito
            elif respuesta == 4:
                puntos_disputa = 2
                #rechazo envido_envido
                
                
                      
        if envido_aceptado == True:
            jugador_ganador = self.mostrar_puntos_envido()
            self.sumar_puntos_envido_partida(objeto_jugador = jugador_ganador, puntos = puntos_disputa)
            
        elif envido_aceptado == False:
            self.sumar_puntos_envido_partida(objeto_jugador = jugador_ganador, puntos = puntos_disputa)
                

    def opciones_envido(self,opcion):
        
        """
        Esta funcion muestra las opciones de envido del jugador,
        
        Args:
            opcion = es el menu de opciones a mostrar 
        """
       
        if opcion == 1: 
            print("Opcion 1: Aceptar")
            print("Opcion 2: Cantar envido")
            print("Opcion 3: Cantar real envido")
            print("Opcion 4: Cantar falta envido")
            print("Opcion 5: Rechazar")
            
            respuesta = input("Elija una opcion: ")
            
            while respuesta != ["1","2","3","4"]:
                print("opcion mal introducida")
                respuesta = input("Elija una opcion: ")
            

    
        elif opcion == 2:
            
            print("Opcion 1: Aceptar")
            print("Opcion 2: Cantar real envido")
            print("Opcion 3: Cantar falta envido")
            print("Opcion 4: Rechazar")
            
            respuesta = input("Elija una opcion: ")
            
            while respuesta != ["1","2","3","4"]:
                print("opcion mal introducida")
                respuesta = input("Elija una opcion: ")
        
        
        elif opcion == 3:
            #real envido
            
            print("Opcion 1: Aceptar")
            print("Opcion 2: Cantar falta envido")
            print("Opcion 3: rechazar")
            
            respuesta = input("Elija una opcion: ")
            
            while respuesta != ["1","2","3","3"]:
                print("opcion mal introducida")
                respuesta = input("Elija una opcion: ")
        
    
                
            

        return respuesta
    
    def rechazo_envido(self,objeto_jugador,puntos):
        
        """
        Asigno los puntos en caso de rechazar el envido
        
        Args:
            Objeto_jugador = Es el jugador que rechaza el envido
        """
        
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
        
    
    def envido_envido_respuesta(self,objeto_jugador_canta):
        """
        Circuito del envido envido

        Args:
            objeto_jugador_canta ([Objeto Jugador]): [Es el jugador que canta el envido-envido]
        """
        # puntos en disputa puede ser un parametro siendo 4 por defecto
        
        # Preguntarle al jugador que quiere hacer
        # Tengo que recorrer de una forma mas optima a los jugadores de tal forma de poder obtener al jugador que rechaza
        
                   
    def envido_envido_circuito(self,jugador_canta):  
        """
        Esta funcion es el corazon del envido envido
        
        Args:
            Jugador_canta = Es un objeto de la clase jugador que canta
        """              
    
        for jugador in self.jugadores:
            if jugador == jugador_canta:
                continue
            elif jugador.equipo == jugador_canta.equipo:
                continue
            else:
                respuesta = self.opciones_envido(2)
                if respuesta != 4:
                    jugador_canta = jugador
                break
        
        if respuesta == 1:
            #Acepto el envido_envido
            return (1,jugador_canta)
        elif respuesta == 4:
            #rechazo el envido_envido
            return (4,jugador_canta)
        elif respuesta == 2:
            #Se canta real envido
            return (2,jugador_canta)
        elif respuesta == 3:
            # se canta falta_envido
            return (3,jugador_canta)
            
    def real_envido_circuito(self,jugador_canta):
        """Es el circuito de los real envido

        Args:
            jugador_canta ([Objeto_Jugador]): Es el objeto de la clase jugador que canta el real envido
            tipo ([Tipo de real envido cantado]): [Tipo de real envido cantado]
        
        Return:
            Retorna una tupla con el resultado de este circuito
        """
        
        try:
            type(tipo) == type(1)
        except:
            raise TypeError("El tipo de real envido no es un numero entero, corregir")
        
        
        for jugador in self.jugadores:
            if jugador == jugador_canta:
                continue
            elif jugador.equipo == jugador_canta.equipo:
                continue
            else:
                respuesta = self.opciones_envido(3)
        
        
        
        
        if respuesta == 1:
            return 1
            #real envido aceptado
        elif respuesta == 2:
            return 2
        elif respuesta == 3:
            return 3
    
            
                  
        
                    
    @classmethod
    def jugar(cls):
        """
        Este metodo ejecuta la partida del juego
        """            

        cantidad_jugadores = input("De cuantos jugadores queres hacer la partida")
        
        while cantidad_jugadores != ["2","4"]:
            print("Jugadores mal introducidos, puede jugar de a 2 o de a 4")
            cantidad_jugadores = input("De cuantos jugadores queres hacer la partida")
        
        tipo_oponente = input("¿Desea jugador contra el sistema o contra la maquina?,Marque 1 para sistema o Marque 2 para jugar contra personas")
        
        while tipo_oponente not in  ["1","2"]:
            print("Tipo mal colocado, es 1 o 2")
            tipo_oponente = input("¿Desea jugador contra el sistema o contra la maquina?,Marque 1 para sistema o Marque 2 para jugar contra personas")
        
        tipo_oponente = int(tipo_oponente)
        
        partida = Partida.crear_partida()
        
        mesa = Mesa()
        
        mazo = Mazo.Mazo()
        
        mazo.crear_mazo()
        
        partida.crear_jugadores(cantidad_jugadores,tipo_oponente)
        
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
                                print("Logica de jugar la carta")

            else:
                print("En construccion")