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

def load_image(nom, width, height):
    #Téléchargement de notre obstacle
    obstacle = pygame.image.load(nom).convert_alpha()
    obstacle_taille = pygame.transform.scale(obstacle, (width, height))
    return obstacle_taille

def obstacle_rect(obstacle, x, y, width, height):
    #Création d'un rectangle qui va contenir notre image obstacle                                          
    obs = obstacle.get_rect()
    obs.x = x
    obs.y = y
    obs.width = width
    obs.height = height
    return obs
