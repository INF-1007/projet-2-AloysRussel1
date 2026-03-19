import random
import pygame

class Confetti: 
    # TODO : Compléter la classe
    def __init__(self, x_position, couleur, taille, vitesse):
        self.__position = [x_position, -10] 
        self.__couleur = couleur
        self.__taille = taille
        self.__vitesse = vitesse

    def tomber(self):
        """Fait descendre le confetti vers le bas de l'écran."""
        self.__position[1] += self.__vitesse

    def afficher(self, screen):
        pygame.draw.rect(screen, self.__couleur, (self.__position[0], self.__position[1], self.__taille, self.__taille))

    def est_hors_ecran(self, hauteur_ecran):
        return self.__position[1] > hauteur_ecran
    
    def gerer_la_fete(self, liste, screen, largeur, hauteur):
        # 1. On crée de nouveaux confettis (on utilise la classe elle-même)
        if len(liste) < 150:
            x = random.randint(0, largeur)
            t = random.randint(5, 10)
            v = random.uniform(2, 5)
            c = random.choice([(255,0,0), (0,255,0), (0,0,255), (255,255,0)])
            # On ajoute une nouvelle instance à la liste
            liste.append(Confetti(x, c, t, v))

        # 2. On anime et on affiche toute la liste
        for c in liste[:]:
            c.tomber()
            c.afficher(screen)
            if c.est_hors_ecran(hauteur):
                liste.remove(c)
            
            