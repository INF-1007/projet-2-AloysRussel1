from composante import Composante

class Moteur(Composante):
    # TODO : Compléter la classe
    def __init__(self, nom, poids, acceleration):
        super().__init__(nom, poids)
        self.__acceleration = acceleration

    def get_acceleration(self):
        return self.__acceleration
    
    def set_acceleration(self, acceleration):
        self.__acceleration = acceleration

    def __str__(self):
        return f"Moteur(nom={self.__nom}, poids={self.__poids}, acceleration={self.__acceleration}))"