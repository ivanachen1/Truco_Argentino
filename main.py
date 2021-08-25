import numpy
from Card import *
from Jugador import Jugador
from Mesa import Mesa 
from Mazo import Mazo

class Partida():
    
    def __init__(self,turnos,sub_partidas,ronda,jugadores,puntos):
        self.turnos = turnos
        self.jugadores = list(jugadores)
        # Esta tupla de self.equipos no tiene uso, podria analizar quitarla
        self.equipos = (1,2)
        self.puntos = dict(puntos)
        self.sub_partidas = sub_partidas
        self.ronda = ronda
        
    @classmethod 
    def crear_partida(cls):
        """
        Este metodo crea un objeto de la clase partida y lo retorna
        """
        
        partida = Partida(turnos = 1, sub_partidas = 1, ronda = 1, puntos = {1: 0,2:0},jugadores = [])
        
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
        
        if self.sub_partidas == 1 and self.ronda == 1 and self.turno == 1:
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
        
        
        if len(self.jugadores) == 2:
            orden_de_partida.append(self.jugadores[1])
        
        elif len(self.jugadores) == 4:
            
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
    
    
    def opciones_de_juego(self):
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
        print("3 - Cantar Real envido")
        print("4 - Cantar Falta envido")
        print("5 - Cantar truco")
        
        opcion = input("¿Que desea hacer?")
        
        while opcion not in ["1","2","3","4","5"]:
            print("opcion mal introducida")
            opcion = input("¿Que desea hacer?")

        opcion = int(opcion)
        
        return opcion
        
        
        ###################################
        ## METO LAS FUNCIONES DEL ENVIDO ##
        ###################################   
    
    def circuito_envido(self,objeto_jugador, opcion = 2):
        """
        Esta funcion es la Padre del envido, arma el circuito completo de esta
        parte del juego
        
        
        Args:
            objeto_jugador ([Obj]): [Es un objeto de la clase jugador, es el jugador que canta el envido]
        
        """

        # me fijo si algun jugador del equipo contrario acepta o no
        
        
        envido_aceptado = False
        envido_rechazado = False
           
        envido_envido_cantado = False
      
        real_envido_cantado = False
        
        falta_envido_cantado = False
        falta_envido_aceptado = False
        
        if opcion == 2:
            #se comenzó cantando envido
            
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
                        #se canta envido-envido
                        envido_envido_cantado = True
                        jugador_canta = jugador
                        break
                    
                    elif respuesta == 3:
                        #se canta real envido
                        real_envido_cantado = True
                        jugador_canta = jugador
                        break
                    
                    elif respuesta == 4:
                        # se canta falta envido
                        falta_envido_cantado = True
                        jugador_canta = jugador
                        break
                                
                        
                    elif respuesta == 5:
                        #rechazo el envido cantado
                        jugador_ganador = objeto_jugador
                        envido_rechazado = True
                        break
        
        
        elif opcion == 3:
            #se comenzó cantando real envido
            respuesta = self.real_envido_circuito(objeto_jugador)
            if respuesta[0] == 1:
                #acepto real envido
                puntos_disputa = 3
            elif respuesta[0] == 2:
                #falta envido cantado
                respuesta = self.falta_envido_circuito(respuesta[1])
                if respuesta[0] == 1:
                    falta_envido_cantado = True
                    resultado = self.falta_envido_circuito(respuesta[1])
                    if resultado == 1:
                        #se acepta el falta envido
                        falta_envido_aceptado = True
                    else:
                        # envido - envido - real envido - falta envido rechazado
                        puntos_disputa = 3
                        envido_aceptado = False
                        envido_rechazado = True
                        jugador_ganador = respuesta[1] 
        
        elif opcion == 4:
            # falta envido cantado de una
            respuesta = self.falta_envido_circuito(objeto_jugador)
            if respuesta[0] == 1:
                #se acepta el falta envido
                falta_envido_aceptado = True
            elif respuesta[0] == 2:
                # se rechaza el falta envido cantado
                jugador_ganador = respuesta[1]
                puntos_disputa = 1 
        
                 
     # Segunda parta de la función
       
        puntos_disputa = 0
        
        if envido_aceptado == True:
            puntos_disputa = 2
          
        elif envido_rechazado == True:
            puntos_disputa = 1
        
        elif real_envido_cantado == True:
            respuesta = self.real_envido_circuito(jugador_canta)
            if respuesta[0] == 1:
                #acepto real envido
                puntos_disputa = 3
            elif respuesta[0] == 2:
                #falta envido cantado
                respuesta = self.falta_envido_circuito(jugador_canta)
                if respuesta[0] == 1:
                    falta_envido_cantado = True
                    resultado = self.falta_envido_circuito(respuesta[1])
                    if resultado == 1:
                        #se acepta el falta envido
                        falta_envido_aceptado = True
                    else:
                        # envido - envido - real envido - falta envido rechazado
                        puntos_disputa = 3
                        envido_aceptado = False
                        envido_rechazado = True
                        jugador_ganador = respuesta[1]
                    
            elif respuesta[0] == 3:
                #real envido rechazado
                puntos_disputa = 2
                jugador_ganador = respuesta[1]
                envido_rechazado = True
            
        elif envido_envido_cantado == True:
            
            respuesta = self.envido_envido_circuito(jugador_canta)
            
            if respuesta[0] == 1:
                puntos_disputa = 4
                #Acepto
              
            elif respuesta[0] == 2:
                # envido - envido - real envido cantado
                print("circuito")
                respuesta = self.real_envido_circuito()
                if respuesta[0] == 1:
                    # real envido aceptado
                    puntos_disputa = 7
                
                elif respuesta[0] == 2:
                    #falta envido cantado
                    falta_envido_cantado = True
                    resultado = self.falta_envido_circuito(respuesta[1])
                    if resultado == 1:
                        #se acepta el falta envido
                        falta_envido_aceptado = True
                    else:
                        # envido - envido - real envido - falta envido rechazado
                        puntos_disputa = 7
                        envido_aceptado = False
                        envido_rechazado = True
                        jugador_ganador = respuesta[1]
                         
                
                elif respuesta[0] == 3:
                    #real envido rechazado
                    puntos_disputa = 4
                    envido_aceptado = False
                    envido_rechazado = True
                    jugador_ganador = respuesta[1]   
                    
                    
                
            elif respuesta[0] == 3:
                print("Circuito")
                #se canta falta_envido
                #armar este circuito
            elif respuesta == 4:
                puntos_disputa = 2
                #rechazo envido_envido
                
        elif falta_envido_cantado == True:
            respuesta = self.falta_envido_circuito()
            if respuesta[0] == 1:
                #se acepta el falta envido
                falta_envido_aceptado = True
            elif respuesta[0] == 2:
                jugador_ganador = respuesta[1]
            
            # se puede aceptar o rechazar, calcular los puntos en disputa        
                      
        if envido_aceptado == True:
            jugador_ganador = self.mostrar_puntos_envido()
            self.sumar_puntos_envido_partida(objeto_jugador = jugador_ganador, puntos = puntos_disputa)
            
        elif envido_rechazado == True:
            self.sumar_puntos_envido_partida(objeto_jugador = jugador_ganador, puntos = puntos_disputa)
        
        elif falta_envido_aceptado == True:
            jugador_ganador = self.mostrar_puntos_envido()
            puntos_disputa = self.calculo_puntos_falta_envido(jugador_ganador= jugador_ganador)
            self.sumar_puntos_envido_partida(objeto_jugador = jugador_ganador, puntos = puntos_disputa)
                       

    def opciones_envido(self,opcion):
        
        """
        Esta funcion muestra las opciones de envido del jugador,
        
        Args:
            opcion = es el menu de opciones a mostrar 
        """
       
        if opcion == 1:
            #envido cantado 
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
            #envido envido
            
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
        
        elif opcion == 4:
            #falta envido cantado
            
            print("Opcion 1: Aceptar")
            print("Opcion 2: rechazar")
            
            respuesta = input("Elija una opcion: ")
            
            while respuesta != ["1","2"]:
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
        
        
        
        
        for jugador in self.jugadores:
            if jugador == jugador_canta:
                continue
            elif jugador.equipo == jugador_canta.equipo:
                continue
            else:
                respuesta = self.opciones_envido(3)
                jugador_aux = jugador
        
        
        
        
        if respuesta == 1:
            return (1,jugador_aux)
            #real envido aceptado
        elif respuesta == 2:
            #falta envido cantado
            return (2,jugador_aux)
        elif respuesta == 3:
            #real envido rechazado
            return (3,jugador_aux)
    
    def falta_envido_circuito(self,jugador_canta):
        """
        Este es el circuito del falta envido,tambien otorga los puntos en disputa.
        """        
        
        for jugador in self.jugadores:
            if jugador == jugador_canta:
                continue
            elif jugador.equipo == jugador_canta.equipo:
                continue
            else:
                respuesta = self.opciones_envido(4)
                ultimo_jugador = jugador
                break
                  
        if respuesta == 1:
            #falta envido aceptado
            return (1,None)
                
        elif respuesta == 2:
            return (2,jugador_canta)
            
    def calculo_puntos_falta_envido(self,jugador_ganador):
        """
        Esta funcion calcula los puntos que se le suman al equipo del jugador ganador del falta envido
        """    
        
        for equipo,puntos in self.puntos:
            if equipo == jugador_ganador.equipo:
                continue
            else:
                puntos_otro_equipo = puntos
        
        puntos_obtenidos = 30-puntos_otro_equipo
        
        return puntos_obtenidos
    
    ##############################
    ##  FUNCIONES DEL TRUCO     ##              
    ##############################
    
    def circuito_truco(self,objeto_jugador,tipo_truco_partida = 1 ,respuesta = 3,cartel_opciones = 1):
        """
        Es el circuito padre del truco, esta funcion verifica si los jugadores mantienen el truco de 2 puntos
        o a lo largo de la partida se va cantando Re-Truco o vale 4. 
        
        Args:
            objeto_jugador = Es un objeto de la clase jugador. Es el jugador que canta.
             
            tipo_truco_partida = es un valor int que nos dice:
                1 = se cantó truco comun
                2 = Se canto Re truco
                3 = Se canto Vale 4
            
            respuesta = es un calor int que nos dice:
                1 - Rechazado
                2 - Aceptado
                3 - Sin respuesta
            
            cartel_opciones = Es el cartel a mostrarle al jugador
        Return:
            Devuelve una tupla con el objeto jugador que acepta, con el valor de recanto si lo existe y con la respuesta     
        """    
        
        for jugador in self.jugadores:
            
            if jugador == objeto_jugador:
                continue
            elif jugador.equipo == objeto_jugador.equipo:
                continue
            
            else:
                
                print("crear una funcion con el menu de respuestas de truco")
                respuesta_jugador = self.opciones_truco(cartel_opciones)
                if respuesta_jugador == 1:
                    tipo_truco_partida = 1
                    respuesta = 2
                    objeto_jugador = jugador
                    break
            
                elif respuesta_jugador == 2:
                    # se canta re truco ----> Como necesito una nueva respuesta de que si se acepta o no, tengo que volver a ejecutar la funcion      
                    tipo_truco_partida = 2
                    respuesta = 3
                    objeto_jugador = jugador
                    break
                
                elif respuesta_jugador == 3:
                    # se canta Vale 4 ----> De acá tambien necesito una nueva respuesta     
                    tipo_truco_partida = 4
                    respuesta = 3
                    objeto_jugador = jugador
                    break
                
                elif respuesta_jugador == 4:
                    # Se rechaza el truco cantado
                    tipo_truco_partida = 1
                    respuesta = 1
                    objeto_jugador = jugador
                       
                    
            
            
            return (objeto_jugador,tipo_truco_partida,respuesta)
                    
                    
    def opciones_truco(self,opcion_mostrar):
        """
        Este es el panel de opciones que se le mostrará al jugador para elegir si quiere o no el truco
        
        Args:
            opcion_mostrar = Es el panel a mostrar al jugador, dependiendo del tipo de truco en el cual esté la partida y el jugador que pueda cantar
        
        """                
                    
           
        print("1 - Aceptar")
        
        if opcion_mostrar == 1:
            # Primer panel de truco mostrado  
            print("2 - Cantar Retruco")
        
        elif opcion_mostrar == 2:
            # panel de Re truco
            print("2 - Cantar Vale 4")
        
        print("3 - Rechazar")
        
        respuesta = input("Elija la opción: ")
        
        while respuesta not in ["1","2","3"]:
            print("valor introducido incorrecatamente")
            respuesta = input("Elija la opción: ")
        
        respuesta = int(respuesta)
        
        return respuesta
        
    def cambio_turno(self,objeto_jugador,objeto_mesa):
        """
        Esta funcion tira la carta, le quita el turno al jugador y se la asigna a otro
        
        """   
        
        carta = Jugador.objeto_jugador.elegir_carta_a_tirar()
                                
        Jugador.jugar_carta_elegida(objeto_jugador,objeto_mesa = objeto_mesa,carta_del_jugador = carta)
        
        Mesa.agregar_carta_mesa(objeto_mesa, ronda = self.ronda, carta_tirada = carta, jugador = objeto_jugador, valor_carta= carta.valor_envido)
                                
        Jugador.perder_turno(objeto_jugador)
        
        #verificacion_cambio_ronda = 
                                
        
        for idx,jugador in enumerate(self.jugadores):
            if jugador == objeto_jugador:
                indice = idx
                continue
            elif len(self.jugadores - 1) == idx:
                jugador_nuevo_turno = self.jugadores[0]
                Jugador.ganar_turno(jugador_nuevo_turno)
                
            elif indice + 1 == idx:
                jugador_nuevo_turno = self.jugadores[idx + 1]
                Jugador.ganar_turno(jugador_nuevo_turno)
            
                            
        self.turnos += 1
        
        if self.cantidad_jugadores_partida() == 2:
            
            if self.turnos == 2:
                self.turnos = 1
                self.ronda += 1
                self.sub_partidas += 1
                jugador_ganador = Mesa.jugador_ganador_ronda(objeto_mesa, objeto_partida_jugadores= self.cantidad_jugadores_partida(), numero_ronda= self.ronda)
                Jugador.ganar_turno(jugador_ganador) 
            else:
                self.turnos = 1
                
        elif self.cantidad_jugadores_partida() == 4:
            
            if self.turnos == 4:
                self.turnos = 1
                self.ronda += 1
                self.sub_partidas += 1
                jugador_ganador = Mesa.jugador_ganador_ronda(objeto_mesa, objeto_partida_jugadores= self.cantidad_jugadores_partida(), numero_ronda= self.ronda)
                Jugador.ganar_turno(jugador_ganador) 
            else:
                self.turnos = 1
                 
    def asignacion_puntos_truco(self,equipo,tipo_truco_partida,respuesta):
        """
        Este metodo asigna los puntos del truco independientemente de si fue rechazado o aceptado
        """                
        
        if respuesta == 1:
            # rechazo 
            if tipo_truco_partida == 1:
                # rechazo del truco comun
                
                if equipo == 1:
                    self.puntos[1] += 1
                else:
                    self.puntos[2] += 1
                    
            elif tipo_truco_partida == 2:
                # rechazo el re truco
                
                if equipo == 1:
                    self.puntos[1] += 2
                else:
                    self.puntos[2] += 2
                    
            elif tipo_truco_partida == 3:
                # rechazo el vale 4
                if equipo == 1:
                    self.puntos[1] += 3
                else:
                    self.puntos[2] += 3                
                                    
        elif respuesta == 2:    
            if tipo_truco_partida == 1:
                # acepto del truco comun
                
                if equipo == 1:
                    self.puntos[1] += 2
                else:
                    self.puntos[2] += 2
                    
            elif tipo_truco_partida == 2:
                # acepto el re truco
                
                if equipo == 1:
                    self.puntos[1] += 3
                else:
                    self.puntos[2] += 3
                    
            elif tipo_truco_partida == 3:
                # acepto el vale 4
                if equipo == 1:
                    self.puntos[1] += 4
                else:
                    self.puntos[2] += 4     
                                    
                                    
                                  
                
        
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
        
        partida.crear_jugadores(cantidad_jugadores,tipo_oponente)
        
        mesa = Mesa()
        
        mazo = Mazo.Mazo()
        
        mazo.crear_mazo() 
        
        partida.asignar_primer_turno_aleatoriamente()
        
        partida.armar_equipo()
        
        in_game = True
        
        partida.orden_de_juego_primer_partida() 
        
        
        while in_game == True:
            
            
            if partida.cantidad_jugadores_partida() == 2:
                
                if partida.primer_turno() == True:
                    
                    for jugador in partida.jugadores:
                        #verifico de quien es el turno
                        if partida.turnos == 1:
                            if jugador.turno == True:
                                #Le pido al jugador que carta quiere tirar a la mesa ---> Crear un método que busque la carta en la mano y la tire.
                                
                                partida.cambio_turno(objeto_jugador= jugador, objeto_mesa= mesa)
                        
                        elif partida.turno == 2:
                            # puede cantar envido / cantar truco / jugar callado
                            opcion = partida.opciones_de_juego()
                            
                            if opcion == 1:
                                #jugar callado
                                
                                partida.cambio_turno(objeto_jugador= jugador, objeto_mesa= mesa)
                             
                            elif opcion == 2:
                                # envido cantado
                                
                                partida.circuito_envido(objeto_jugador= jugador, opcion = 2)
                                
                                partida.cambio_turno(objeto_jugador= jugador, objeto_mesa= mesa)    
                                      
                            elif opcion == 3:
                                # real envido cantado de una
                                partida.circuito_envido(objeto_jugador= jugador, opcion = 3) 
                                
                                partida.cambio_turno(objeto_jugador= jugador, objeto_mesa= mesa)

                            elif opcion == 4:
                                # falta envido cantado de una
                                partida.circuito_envido(objeto_jugador = jugador, opcion = 4) 
                                
                            elif opcion == 5:
                                #se canta truco
                                
                                jugador_responde,tipo_truco_partida,respuesta = partida.circuito_truco(objeto_jugador= jugador)
                                # el resto de los params estan por defecto
                                
                                if respuesta == 1:
                                    
                                    if jugador_responde.equipo == 1:
                                        equipo = 2
                                    else:
                                        equipo = 1
                                    
                                    partida.asignacion_puntos_truco(equipo = equipo, tipo_truco_partida = tipo_truco_partida, respuesta = respuesta)
                                    
                                    # Aca tengo que devolver las cartas al mazo y quitarselas a los jugadores y resetear la partida
            
                                # aceptacion de truco / re truco / vale 4
                                elif respuesta == 2:
                                    
                                    if jugador_responde.equipo == 1 and tipo_truco_partida == 1:
                                        # Se acepto el truco comun
                                        print("ver como sigue el flujo acá")
                                        print("los siguientes jugadores en el resto de la partida pueden cantar mas")
                                        partida.cambio_turno(objeto_jugador= jugador, objeto_mesa= mesa)
                                    
                                    if jugador_responde.equipo == 1 and tipo_truco_partida == 2:
                                        # Se acepto el re truco
                                        print("ver como sigue el flujo acá")
                                        print("los siguientes jugadores en el resto de la partida pueden cantar mas")
                                        partida.cambio_turno(objeto_jugador= jugador, objeto_mesa= mesa)
                                             
                                        
                                elif respuesta == 3:
                                    # Aqui no hay una respuesta adicional y sigue la partida
                                    
                                    partida.cambio_turno(objeto_jugador= jugador, objeto_mesa= mesa)
                                    

                #elif partida.ronda > 1:
                                        
                                    
                      
                                    
                                
            
            else:
                print("En construccion")
                
                
                
                # Tengo que resolver:
                # Problema
                # 1) El cambio de ronda
                # para resolver el cambio de ronda tengo que resolver el tema de que jugador gano la ronda asi se quien tiene el primer turno de la segunda ronda
                # tengo que mirar en la mesa que cartas hay y cuales valen mas que otras
                #Solucion
                # En la clase Mesa voy a crear un diccionario que tenga como clave el numero de ronda y como valor la lista de cartas tiradas y los jugadores que las tiraron
                # DataFrame = (nro_ronda,carta_tirada,jugador que tiro la carta, y su valor) ---> De aca filtro quien gano la ronda y seteo el turno en True
                
                # sub partidas ---> Es cada partida conformada por 3 rondas y cada ronda tiene sus turnos
                
                # En la primer partida, debo otorgarle al jugador en posicion 1 el turno en True. Para el resto tengo que rotar a la derecha