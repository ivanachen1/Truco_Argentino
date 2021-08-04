from numpy import concatenate
import Card

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
                