import pygame 

vitesse_dash = 20        # pixels par image pendant le dash
duree_dash = 10          # nombre d'images du dash 
dash_restant = 0         # images de dash qu'il reste à faire
direction_dash = 0       # 1 = droite, -1 = gauche, 0 = pas de dash 

nb_dash_perso = 1
nb_dash = nb_dash_perso


def activation_dash(droite,gauche,nb_dash,duree_dash):
    """cette fontion sert a donner lesence du dash et a en retirer u quand on l'active 
    entree :droite : booleane qui indique si da touche pour aller a droite est presser 
            gauche : booleane qui indique si da touche pour aller a gauche est presser
            nb_dash : int indicant ne nombre de dash restant
    sortie :nb_dash : int indicant ne nombre de dash restant
            direction_dash : int qui indique si il y a un dash et sa direction (1 = droite, -1 = gauche, 0 = pas de dash)
            dash_restant : int indique le nombre de dash restant 
    """
    direction_dash = 0
    dash_restant = 0
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT and nb_dash > 0 and not direction_dash:

        if droite and not gauche:
            direction_dash = 1

        elif gauche and not droite:
            direction_dash = -1

    # si on dash a droite ou a gauche 
    if direction_dash != 0:
        dash_restant = duree_dash
        nb_dash -= 1

    return nb_dash, direction_dash, dash_restant
# nb_dash, direction_dash = activation_dash(droite,gauche,nb_dash,direction_dash)



# reste a faire les deplacement du dash 
