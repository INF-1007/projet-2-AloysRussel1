from composante import Composante

class Chassis(Composante):
    # TODO : Compléter la classe
    def __init__(self, nom, poids, aire_frontale, coefficient_trainee):
        super().__init__(nom, poids)
        self.__aire_frontale = aire_frontale
        self.__coefficient_trainee = coefficient_trainee
    
    def get_aire_frontale(self):
        return self.__aire_frontale
    
    def set_aire_frontale(self, aire_frontale):
        self.__aire_frontale = aire_frontale
        
    def get_coefficient_trainee(self):
        return self.__coefficient_trainee
    
    def set_coefficient_trainee(self, coefficient_trainee):
        self.__coefficient_trainee = coefficient_trainee
        
    def __str__(self):
        return f"Chassis(nom={self.__nom}, poids={self.__poids}, aire_frontale={self.__aire_frontale}, coefficient_trainee={self.__coefficient_trainee})"