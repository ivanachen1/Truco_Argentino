import numpy as np
import Mazo 


class Card():
    
    path = "C:\Users\iachenbach\Documents\GitHub\Truco_Argentino\valores_cartas"    
    
    def __init__(self,palo,number,valor_envido,nombre_carta,valor_truco):
        """
        Genero los atributos de la clase carta
        que son el palo, el numero, y la cantidad

        Args:
            palo ([list]): [lista de palos]
            number ([list]): [lista de numeros]
            cantidad ([type]): [description]
        """
        # Una sola carta tiene 1 atributo, el mazo tiene este init
        self.palo = palo
        self.number = number
        self.valor_truco = valor_truco
        self.valor_envido = valor_envido
        
        self.nombre_carta = nombre_carta 
                 
    
    @staticmethod
    def sumar_una_carta(objeto_jugador,carta):
        """
        [El metodo otorga 1 carta a la mano]
        
        """
        
        objeto_jugador.cartas.append(carta)
    
    @staticmethod
    # Al redefinir la clase carta hay que reescribir el metodo
    def disminuir_una_carta(objeto_jugador,carta):
        """
        [El metodo disminuye la cantidad de cartas de la mano
        """
        objeto_jugador.cartas.remove(carta)
    
    # Al redefinir la clase carta hay que reescribir el metodo
    def crear_mano(self,objeto_jugador,objeto_mazo):
        """
        Crea la mano de cartas
        """
        
        while objeto_jugador.cartas < 4:
            
            carta_tomada = np.random.choice(objeto_mazo.cartas)
            
            self.sumar_una_carta(carta_tomada)
            
            Mazo.objeto_mazo.quitar_carta()
            
            objeto_jugador.cartas.append(carta_tomada)
    
    # Al redefinir la clase carta hay que reescribir el metodo   
    def jugar_carta(self,carta_jugador):        
        """
        Juego la carta en la mesa.Disminuyo del jugador y aumento en la mesa
        
        """       
        
        #Le quito la carta al jugador de la mano
        carta.carta.remove(carta_jugador)
        
        self.disminuir_una_carta()
        
    

        
        
        