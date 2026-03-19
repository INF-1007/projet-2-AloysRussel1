class Composante:
    # TODO: Compléter la classe
    def __init__(self, nom, poids):
        self.__nom = nom
        self.__poids = poids
        
    def get_poids(self):
        return self.__poids
    
    def get_nom(self):
        return self.__nom
    
    def set_poids(self, poids):
        self.__poids = poids
        
    def set_nom(self, nom):
        self.__nom = nom

    def __str__(self):
        return f"Composante(nom={self.__nom}, poids={self.__poids})"