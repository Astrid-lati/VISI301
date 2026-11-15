import pygame 




def activation_dash(event, droite, gauche, nb_dash, direction_dash, dash_restant, duree_dash):
    """cette fontion sert a donner le sence du dash et a en retirer un quand on l'active 
    entree :event : événement pygame en cours de traitement
            droite : booleane qui indique si la touche pour aller a droite est presser 
            gauche : booleane qui indique si la touche pour aller a gauche est presser
            nb_dash : int indicant ne nombre de dash restant
            direction_dash : int, direction du dash en cours (1 droite, -1 gauche, 0 aucun)
            dash_restant : int, nombre d'images de dash qu'il reste à faire
            duree_dash : int, durée d'un dash en images
    sortie :nb_dash : int indicant ne nombre de dash restant
            direction_dash : int qui indique si il y a un dash et sa direction (1 = droite, -1 = gauche, 0 = pas de dash)
            dash_restant : int indique le nombre de dash restant 
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT and nb_dash > 0 and direction_dash == 0:

        if droite and not gauche:
            direction_dash = 1
        elif gauche and not droite:
            direction_dash = -1

        # on consomme un dash que si une direction a été choisie
        if direction_dash != 0:
            dash_restant = duree_dash
            nb_dash -= 1

    return nb_dash, direction_dash, dash_restant

#nb_dash, direction_dash, dash_restant = fct_mouvements.activation_dash(event, droite, gauche, nb_dash, direction_dash, dash_restant, duree_dash)


def mise_a_jour_dash(direction_dash, dash_restant, vitesse_dash, vitesse_max):
    """met a joure les information du dash en court .
    entrées : direction_dash : int, direction du dash en cours (1 droite, -1 gauche, 0 aucun)
              dash_restant : int, nombre d'images de dash qu'il reste à faire
              vitesse_dash : int, vitesse pendant le dash
              vitesse_max : int, vitesse horizontale max en temps normal
    sorties : vitesse_x, vitesse_y, dash_restant, direction_dash
    """
    vitesse_x = direction_dash * vitesse_dash
    vitesse_y = 0                      # pas de chute pendant le dash
    dash_restant -= 1

    if dash_restant <= 0:
        vitesse_x = direction_dash * vitesse_max   # fin du dash
        direction_dash = 0

    return vitesse_x, vitesse_y, dash_restant, direction_dash


# reste a faire les deplacement du dash 
