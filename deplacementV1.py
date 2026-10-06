import pygame 

pygame.init()

fenetre = pygame.display.set_mode((800,600))
horloge = pygame.time.Clock()
fps = 60





# joueur
personnage1 = pygame.Rect(400, 300, 50, 50)

# bloque
sol1 = pygame.Rect(0, 450, 300, 150)
sol2 = pygame.Rect(400, 450, 400, 150)




#statistique
vitesse = 10
vitesse_y = 0

saut = -15

gravite = 0.5



#couleur 
vert = (0,255,0)
noir = (0,0,0)
rouge = (255,0,0)
blanc = (255,255,255)
marron = (100,100,100)  # n'as rien d'un marron





ouvert = True 

while ouvert : 

    # boucle pour la fermeture de la page 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ouvert = False

        # on enclanche le saut 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                vitesse_y = saut

    touches = pygame.key.get_pressed()
    
    # creation des image a afficher 
    fenetre.fill(noir)


    #calcule de la vitesse de chute 
    vitesse_y += gravite

    personnage1.y += vitesse_y

    
         
    
    
    



    if touches[pygame.K_LEFT] or touches[pygame.K_q] :
        personnage1.x -= vitesse

    if touches[pygame.K_RIGHT] or touches[pygame.K_d] :
            personnage1.x += vitesse

    
    pygame.draw.rect(fenetre, marron,sol1)
    pygame.draw.rect(fenetre, marron,sol2)
    pygame.draw.rect(fenetre, vert,personnage1)



    # affichage du resultat
    pygame.display.flip()
    horloge.tick(fps)



pygame.quit()