# auto.py
# auto.py
from vehicule import Vehicule
from specifications import AutoSpecs
from roue import Roue
from moteur import Moteur
from chassis import Chassis

class Auto(Vehicule):

    # TODO : Compléter la classe
    def __init__(self, nom, position_dep):
        specs = AutoSpecs()
        nb_roues = 4
        mes_roues = Roue(specs.roue_nom, specs.roue_poids*nb_roues, specs.roue_friction, specs.roue_support*nb_roues)
        mon_moteur = Moteur(specs.moteur_nom, specs.moteur_puissance, specs.moteur_acceleration)
        mon_chassis = Chassis(specs.chassis_nom, specs.chassis_poids, specs.chassis_aire, specs.chassis_trainee)
        super().__init__(
            nom=nom, 
            position_dep=position_dep, 
            roues=mes_roues, 
            moteur=mon_moteur, 
            chassis=mon_chassis, 
            Specs=specs, 
            image_path="images/auto.png"
        )