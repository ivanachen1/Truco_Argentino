import pandas as pd

class Mesa():
    """
    Es la clase mesa del juego
    """
    def __init__(self,cantidad_cartas):
        """[summary]

        Args:
            cantidad_cartas ([int]): [Es la cantidad de cartas que posee la mesa,siendo un numero int]
            cartas ([List]): [Son las cartas que posee la mesa]
        """
        self.cantidad_cartas = cantidad_cartas
        self.cartas = pd.DataFrame({"Ronda":[],"Carta Tirada":[],"Jugador":[],"Valor_carta":[]})
        
    def agregar_carta_mesa(self,ronda,carta_tirada,jugador,valor_carta):
        """
        Esta función agrega la carta al Dataframe Pandas de las cartas para luego usarlo para filtrar para
        los cambios de ronda y de turno entre una ronda y otra

        Args:
            ronda ([int]): [Es el numero de ronda donde fue tirada la carta]
            carta_tirada([Card_Object]): [Es la carta que se tiró a la mesa]
            jugador([Jugador_Object]): [Es el jugador que tiró la carta a la mesa]
            valor_carta ([type]): [Es el valor de la carta, dice que carta es mejor que otra. Por ejemplo, 
            El ancho de espada vale mas que el ancho de basto. Esto surge del dataframe que se carga en la clase Card]        
        
        """
        
        self.cartas = self.cartas.append({"Ronda":ronda,"Carta Tirada":carta_tirada,"Jugador":jugador,"Valor_carta":valor_carta})
    
    