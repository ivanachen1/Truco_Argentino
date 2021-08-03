import numpy as np 


class Card():
    def __init__(self,palo,number,cantidad,carta):
        """
        Genero los atributos de la clase carta
        que son el palo, el numero, y la cantidad

        Args:
            palo ([list]): [lista de palos]
            number ([list]): [lista de numeros]
            cantidad ([type]): [description]
        """
        self.palo = ["oro","copa","espada","basto"]
        self.number = list(range(1,8)) + [10,11,12]
        self.cantidad = cantidad
        self.carta = list(carta)
    
    def crear_mazo(self):
        """
        Crea el mazo de cartas
        """
        
        for palo in self.palo:
            for number in self.number:
                carta = str(number) + palo
                self.carta.append(carta)
                self.cantidad += 1
                
        
    
    @staticmethod
    def sumar_una_carta(objeto_jugador):
        """
        [El metodo otorga 1 carta a la mano]
        
        """
        
        objeto_jugador.cantidad += 1
    
    def disminuir_una_carta(self):
        """
        [El metodo disminuye la cantidad de cartas de la mano]
        """
        self.cantidad -= 1
    
    def crear_mano(self,objeto_jugador):
        """
        Crea la mano de cartas
        """
        
        while objeto_jugador.cantidad < 4:
            carta_tomada = np.random.choice(mazo.carta)
            Card.sumar_una_carta(objeto_jugador)
            mazo.disminuir_una_carta()
            objeto_jugador.cartas.append(carta_tomada)
    
        
    def jugar_carta(self,carta_jugador):        
        """
        Juego la carta en la mesa.Disminuyo del jugador y aumento en la mesa
        
        """       
        
        #Le quito la carta al jugador de la mano
        carta.carta.remove(carta_jugador)
        
        self.sumar_una_carta()
        
    

        
        
        