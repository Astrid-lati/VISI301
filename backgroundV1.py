import pygame

pygame.init()
running = True
#Création de la fenêtre du jeu
screen = pygame.display.set_mode((800,600))

#On télécharge notre image de fond 
background = pygame.image.load('samples/Backgroundv1.png').convert_alpha()

#On redimensionne l'image pour qu'elle soit de la même taille que la fenêtre 
background = pygame.transform.scale(background, (800,600))

#Ouverture et condition de la fenêtre de jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Insertion de l'image dans la fenêtre
    screen.blit(background,(0,0))

    #Mise à jour de la fenêtre
    pygame.display.update()


pygame.quit()