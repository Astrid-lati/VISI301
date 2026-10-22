import pygame

def creation_fond(image):
    #On télécharge notre image de fond 
    nom = pygame.image.load(image).convert_alpha()

    #On redimensionne l'image pour qu'elle soit de la même taille que la fenêtre 
    nom = pygame.transform.scale(nom, (800,600))

    return nom

def insertion_fond(fenetre, fond):
        #Insertion de l'image dans la fenêtre
        fenetre.blit(fond,(0,0))