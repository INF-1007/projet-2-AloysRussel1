from composante import Composante

# TODO : Créer la classe Roue

class Roue(Composante):
    # TODO : Compléter la classe
    def __init__(self, nom,poids, coefficient_friction,poids_supporte,nb_roues=1):
        super().__init__(nom, poids)
        self.__poids_supporte = poids_supporte
        self.__coefficient_friction = coefficient_friction
        self.nb_roues = nb_roues
        
    def get_coefficient_friction(self):
        return self.__coefficient_friction
    
    def set_coefficient_friction(self, coefficient_friction):
        self.__coefficient_friction = coefficient_friction
        
    def get_poids_supporte(self):
        return self.__poids_supporte
    
    def set_poids_supporte(self, poids_supporte):
        self.__poids_supporte = poids_supporte

    def __str__(self):
        return f"Roue(nom={self.__nom}, poids={self.__poids}, coefficient_friction={self.__coefficient_friction}, poids_supporte={self.__poids_supporte})"