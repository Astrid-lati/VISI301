


def colision_dessus (liste_bloc, personnage, vitesse_y):
    """cette fonction dit si il y a une colision sur le haut d'un bloc
    entree : liste_bloc, liste des bloc
             personnage,  element avec le quelle il y a le contact
             vitesse_y, int qui indique si le personnage descent ou monte
    sortie :  bloc_colisioner egale a un bloc si il y a une colision et a None sinon       
    """           
    bloc_colisioner = None
    bloc = 0
    while bloc_colisioner == None and bloc < len(liste_bloc):
        if personnage.colliderect(liste_bloc[bloc]) and vitesse_y >= 0 :
            bloc_colisioner = liste_bloc[bloc]
            # vitesse_y = 0
            # personnage.bottom = bloc_colisioner.top
        bloc += 1

    return bloc_colisioner

    




def colision_dessous (liste_bloc, personnage, vitesse_y):
    """cette fonction dit si il y a une colision sur le haut d'un bloc
    entree : liste_bloc, liste des bloc
             personnage,  element avec le quelle il y a le contact
             vitesse_y, int qui indique si le personnage descent ou monte
    sortie :  bloc_colisioner egale a un bloc si il y a une colision et a None sinon       
    """           
    bloc_colisioner = None
    bloc = 0
    while bloc_colisioner == None and bloc < len(liste_bloc):
        if personnage.colliderect(liste_bloc[bloc]) and vitesse_y < 0 :
            bloc_colisioner = liste_bloc[bloc]
            # vitesse_y = 0
            # personnage.top = bloc_colisioner.bottom
        bloc += 1

    return bloc_colisioner
