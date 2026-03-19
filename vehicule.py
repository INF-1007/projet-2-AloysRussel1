from cmath import rect

import numpy as np
import pygame
from specifications import DENSITE_AIR

# TODO : Créer la classe Vehicule

# Cette classe doit contenir les attributs **privés** suivants: 
# - `nom`
# - `position`: un numpy array avec format [x, y]
# - `vitesse` : un numpy array avec format [0, 0]
# - `roues`
# - `moteur`
# - `chassis`
# - `poids_total`: la somme du poids des composantes

class Vehicule:

    # TODO : Créer le constructeur 
    def __init__(self, nom, position_dep, roues, moteur, chassis, Specs, image_path):
        # TODO : ajouter les attributs
        self.__nom = nom
        self.__position = np.array(position_dep, dtype=float)
        self.__vitesse = np.array([0.0, 0.0], dtype=float)
        self.__roues = roues
        self.__moteur = moteur
        self.__chassis = chassis
        self.__specs = Specs
        
        self.__poids_total = self.calculer_poids_total()

        # TODO : ajouter un attribut pour l'image du véhicule
        self.__taille_image = (Specs.image_width, Specs.image_height)
        image_brute = pygame.image.load(image_path).convert_alpha()
        self.__image = pygame.transform.scale(image_brute, self.__taille_image)
        
    def get_position(self):
        return self.__position
    

        
    
    def affichage_vehicule(self, screen):
        # TODO : compléter la méthode 
        position_x = int(self.__position[0]) - self.__taille_image[0]
        position_y = int(self.__position[1])
        
        rect = self.__image.get_rect(midleft=(position_x, position_y))
        screen.blit(self.__image, rect)
        
    
    def calculer_poids_total(self):
        # TODO : compléter la méthode
        poids_roues = self.__roues.get_poids() * 4
        poids_moteur = self.__moteur.get_poids()
        poids_chassis = self.__chassis.get_poids()
        
        self.__poids_total = poids_roues + poids_moteur + poids_chassis
        return self.__poids_total

    def calculer_traction(self):
        # TODO : compléter la méthode 
        return self.__poids_total * self.__moteur.get_acceleration() 
        
        

    def calculer_friction(self):
        # TODO : compléter la méthode 
        coeff_friction = self.__roues.get_coefficient_friction()
        friction_totale = coeff_friction * self.__vitesse
        return friction_totale
        
    def calculer_trainee(self):
        # TODO : compléter la méthode 
        
        coefficient_trainee = self.__chassis.get_coefficient_trainee()
        aire_frontale = self.__chassis.get_aire_frontale()
        # 1/2 * coefficient_trainee * aire_frontale * densite_air * vitesse^2
        trainee = 0.5 * coefficient_trainee * aire_frontale * DENSITE_AIR * (self.__vitesse**2)
        return trainee
        
        

    def accelerer(self, dt):
        # TODO : compléter la méthode 
        traction = self.calculer_traction()
        trainee = self.calculer_trainee()
        friction = self.calculer_friction()
        
        traction_vecteur = np.array([traction, 0.0])
        
        acceleration = (traction_vecteur - trainee - friction) / self.__poids_total
        
        self.__vitesse += acceleration * dt
        self.__position += self.__vitesse * dt

    def celebrer(self):
        # TODO : compléter la méthode 
        return f"{self.__nom} remporte la course !"