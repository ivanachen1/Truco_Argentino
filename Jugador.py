import numpy as np

class Jugador():
    def __init__(self,mano,cartas,equipo,posicion,nombre,turno,es_maquina):
        """[summary]

        Args:
            cantidad ([int]): [Cantidad de jugadores]
            cartas ([list]): [Son las cartas del jugador]
        """
        self.cartas = list(cartas)
        self.mano = list(mano)
        self.equipo = equipo
        self.posicion = posicion
        self.turno = turno
        self.nombre = nombre
        self.maquina = es_maquina
        
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
                  
    @property
    def puntos_envido(self):
        """
        Este metodo calcula los puntos de envido del jugador.Lo denomino como propiedad
        para acceder mas facil
        
        #Los puntos de envido que se calculen antes de tirar la primera carta asi quedan
        """      
        
        palo_puntos = []
        for carta in self.cartas:
            palo_puntos.append((carta.nombre_carta,carta.palo,carta.valor_envido))
        
        lista_valores = [palo_puntos[0][2],palo_puntos[1][2],palo_puntos[2][2]]
            
        if (palo_puntos[0][1] == palo_puntos[1][1]) and (palo_puntos[1][1] == palo_puntos[2][1]):
            #Tengo flor pero por ahora no me meto en ese tema. Calculo el mayor tanto
            
            valor_minimo = min(lista_valores)
            
            lista_valores.remove(valor_minimo)
            
            valor_envido = sum(lista_valores) + 20
            
            return  valor_envido
        
        elif (palo_puntos[0][1] != palo_puntos[1][1]) and (palo_puntos[1][1] != palo_puntos[2][1]) and (palo_puntos[0][1] != palo_puntos[2][1]):
            
            return max(lista_valores)
        
        elif (palo_puntos[0][1] != palo_puntos[1][1]) and (palo_puntos[1][1] == palo_puntos[2][1]):
            
            valor_quitar = palo_puntos[0][1]
            
            lista_valores.remove(valor_quitar)
            
            valor_envido = sum(lista_valores) + 20
            
            return valor_envido
        
        elif (palo_puntos[0][1] == palo_puntos[1][1]) and (palo_puntos[1][1] != palo_puntos[2][1]):
            
            valor_quitar = palo_puntos[2][1]
            
            lista_valores.remove(valor_quitar)
            
            valor_envido = sum(lista_valores) + 20
            
            return valor_envido
        
        elif (palo_puntos[0][1] == palo_puntos[2][1]) and (palo_puntos[1][1] != palo_puntos[2][1]):
            
            valor_quitar = palo_puntos[1][1]
            
            lista_valores.remove(valor_quitar)
            
            valor_envido = sum(lista_valores) + 20
            
            return valor_envido
            
    @classmethod
    def crear_jugador_real(cls):
        """
        Este metodo crea un objeto de la clase jugador del tipo humano,con los datos del ser humano
        """        
        
        mano = []
        cartas = []
        equipo = None
        posicion = 0
        turno = False
        nombre = input("Escriba su nombre de jugador")
        es_maquina = False

        
        jugador = Jugador(mano = mano, cartas = cartas, equipo = equipo, posicion = posicion, nombre = nombre, turno = turno, es_maquina= es_maquina)
        
        return jugador
    
    @classmethod 
    def crear_jugador_maquina(cls):
        """
        Este metodo crea un objeto de la clase jugador del tipo maquina
        
        """
        
        mano = []
        cartas = []
        equipo = None
        posicion = 0
        turno = False
        nombre = np.random.choice(['John', 'Juan', 'Jane', 'Jack', 'Jill', 'Jean',"Eva","Vicky","Sabrina","Chopa","Luisa"])
        es_maquina = True

        
        jugador = Jugador(mano = mano, cartas = cartas, equipo = equipo, posicion = posicion, nombre = nombre, turno = turno, es_maquina= es_maquina)
        
        return jugador    
        
            
            
        