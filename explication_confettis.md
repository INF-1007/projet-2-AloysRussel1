"""
Fichier : explication_confettis.py
Description : Documentation simple de l'implémentation des confettis pour le projet.
"""

# 1. Conception de la classe Confetti
# Chaque confetti est un objet indépendant avec sa propre position (x, y), 
# sa couleur, sa taille et sa vitesse de chute. Les attributs sont privés 
# pour respecter les principes de la POO.

# 2. Logique de mouvement et d'affichage
# - La méthode tomber() : Ajoute la vitesse à la position Y pour faire descendre le carré.
# - La méthode afficher() : Dessine le carré sur l'écran avec pygame.draw.rect.
# - La méthode est_hors_ecran() : Vérifie si le confetti a dépassé le bas de la fenêtre.

# 3. Gestion de l'animation (gerer_la_fete)
# Cette méthode gère la liste globale des confettis :
# - Création : On génère des confettis avec des caractéristiques aléatoires 
#   (couleurs, tailles entre 5-10px, vitesses entre 2-5) pour un effet naturel.
# - Limite : On limite la liste à 150 confettis pour garder le jeu fluide.
# - Nettoyage : On supprime les confettis de la liste dès qu'ils sortent de l'écran 
#   pour économiser la mémoire.

# 4. Intégration
# L'animation est appelée dans la boucle principale du fichier main.py 
# uniquement lorsqu'un véhicule franchit la ligne d'arrivée.