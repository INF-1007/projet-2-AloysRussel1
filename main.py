from logging import config

import pygame
import random
from moto import Moto
from auto import Auto
from camion import Camion
from confettis import Confetti
from config import WIDTH, HEIGHT, START_LINE_X, FINISH_LINE_X, START_MOTO_Y, START_AUTO_Y, START_CAMION_Y 


def main():

    liste_confettis = []
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulation de course")

    background = pygame.image.load("images/background.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    # TODO : Créer une liste de véhicules qui contient une instance pour chaque
    # type de véhicule : une moto, une auto et un camion
    
    une_moto = Moto("Ma Super Moto", [START_LINE_X, START_MOTO_Y])
    une_auto = Auto("Mon Auto Rapide", [START_LINE_X, START_AUTO_Y])
    un_camion = Camion("Mon Gros Camion", [START_LINE_X, START_CAMION_Y])
    confetti = Confetti(500, (255, 0, 0), 10, 3) # Exemple de confetti pour les tests
    
    liste_vehicules = [une_moto, une_auto, un_camion]

    running = True
    course_commencee = False
    gagnant = None

    while running:

        screen.blit(background, (0, 0))

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    course_commencee = True

        # TODO : Gérer le début de la course en appelant la méthode `accelerer` des véhicules
        # Si le véhicule franchit la ligne et qu’on n’a pas encore de gagnant, on le note
        for vehicule in liste_vehicules:
            if course_commencee :
                vehicule.accelerer(dt)
                if vehicule.get_position()[0] >= FINISH_LINE_X and gagnant is None:
                    gagnant = vehicule


        # TODO : Pour chaque véhicule, appeler la méthode `affichage_vehicule`
        for vehicule in liste_vehicules:
            vehicule.affichage_vehicule(screen)
            
        

        if not course_commencee and gagnant is None:
            txt = font.render("Appuyez sur ESPACE pour démarrer", True, (0, 0, 0))
            screen.blit(txt, (350, 35))

        # TODO: Si on a un gagnant, afficher le message qui indique le véhicule gagnant avec la méthode `celebrer`
        if gagnant is not None:
            message_gagnant = gagnant.celebrer()
            txt_gagnant = font.render(message_gagnant, True, (255, 0, 0))
            screen.blit(txt_gagnant, (350, 35))
            
            # Ajouter des confettis
            confetti.gerer_la_fete(liste_confettis, screen, WIDTH, HEIGHT)

            

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()