class Jugador():
    def __init__(self,cantidad,cartas,equipo,posicion):
        """[summary]

        Args:
            cantidad ([int]): [Cantidad de jugadores]
            cartas ([list]): [Son las cartas del jugador]
        """
        self.mano = mano
        self.cartas = list(cartas)
        self.equipo = equipo
        self.posicion = posicion
    
    def show_mano_del_jugador(self,mano):
        """
        Muestro la mano del jugador
        
        """
        if len(self.cartas) == 0:
            print("El jugador no tiene cartas")
        else:
            for i in self.cartas:
                print(i,end = "")