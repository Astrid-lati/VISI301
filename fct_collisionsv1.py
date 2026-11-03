


def colision_dessus (liste_bloc, personnage, vitesse_y):
    """cette fonction dit si il y a une colision sur le haut d'un bloc
    entree : liste_bloc, liste des bloc
             personnage,  element avec le quelle il y a la colision
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
             personnage,  element avec le quelle il y a la colision
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






def colision_droite (liste_bloc, personnage, vitesse_x):
    """cette fonction dit si il y a une colision sur la droite d'un bloc
    entree : liste_bloc, liste des bloc
             personnage,  element avec le quelle il y a la colision
             vitesse_x, int qui indique si le personnage vas a droite ou a gauche
    sortie :  bloc_colisioner egale a un bloc si il y a une colision et a None sinon       
    """           
    bloc_colisioner = None
    bloc = 0
    while bloc_colisioner == None and bloc < len(liste_bloc):
        if personnage.colliderect(liste_bloc[bloc]) and vitesse_x < 0 :
            bloc_colisioner = liste_bloc[bloc]
            # vitesse_x = 0
            # personnage.left = bloc_colisioner.right
        bloc += 1

    return bloc_colisioner

    




def colision_gauche (liste_bloc, personnage, vitesse_x):
    """cette fonction dit si il y a une colision sur la gauche d'un bloc
    entree : liste_bloc, liste des bloc
             personnage,  element avec le quelle il y a la colision
             vitesse_x, int qui indique si le personnage vas a droite ou a gauche
    sortie :  bloc_colisioner egale a un bloc si il y a une colision et a None sinon       
    """           
    bloc_colisioner = None
    bloc = 0
    while bloc_colisioner == None and bloc < len(liste_bloc):
        if personnage.colliderect(liste_bloc[bloc]) and vitesse_x > 0 :
            bloc_colisioner = liste_bloc[bloc]
            # vitesse_x = 0
            # personnage.right = bloc_colisioner.left
        bloc += 1

    return bloc_colisioner
