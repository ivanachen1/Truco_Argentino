class Mesa():
    """
    Es la clase mesa del juego
    """
    def __init__(self,cantidad_cartas,cartas):
        """[summary]

        Args:
            cantidad_cartas ([int]): [Es la cantidad de cartas que posee la mesa,siendo un numero int]
            cartas ([List]): [Son las cartas que posee la mesa]
        """
        self.cantidad_cartas = cantidad_cartas
        self.cartas = []