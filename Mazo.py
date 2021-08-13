from numpy import concatenate
import Card
import Jugador 
import main 

class Mazo():
    def __init__(self,cartas):
        
        self.cartas = []
        
    def crear_mazo(self):
        """
        Crea el mazo de cartas
        """
        
        import pandas as pd
       
        archivo = pd.read_csv(path)
       
        for row in archivo.itertuples():
            number = row[1]
            
            palo = row[2]
            
            valor_truco = row[3]
            
            valor_envido = row[4]
            
            nombre = str(number) + "De" + str(palo)
            
            card = Card(palo = palo, number = number, valor_envido = valor_envido, valor_truco = valor_truco, nombre_carta = nombre)
            
            self.cartas.append(card)
                
    def quitar_carta(self,carta):
        """
        Este metodo quita una carta del mazo
        
        """
        
        self.cartas.remove(carta)
    
    def mezclar_cartas_jugadores(self,objeto_partida):
        """
        Este metodo toma las cartas de los jugadores y las devuelve
        al mazo

        Args:
            lista_de_jugadores ([List]): [Es la lista de jugadores de la partida]
        """
        # tengo que pasarle el objeto partida para acceder a la lista de jugadores
        for jugador in main.objeto_partida.jugadores:
            #recorro los jugadores
            for carta in jugadores.cartas:
                #recorro los objetos cartas uno por uno
                jugadores.carta.remove(carta)
                #remuevo las cartas de la mano del jugador
                self.cartas.append(carta)
                #agrego las cartas al mazo
                
    def mezclar_cartas_mesa(self,objeto_mesa):
        """
        Este metodo recorre las cartas de la mesa y las coloca nuevamente en el mazo

        Args:
            objeto_mesa ([List]): [Objeto de la clase mesa]
        """
        
        for carta in objeto_mesa.cartas:
            #quito la carta
            objeto_mesa.remove(carta)
            # la meto en el mazo
            self.cartas.append(carta)
            