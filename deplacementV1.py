import pygame 
import fct_collisionsv1
import backgroundV1

pygame.init()

fenetre = pygame.display.set_mode((800,600))
horloge = pygame.time.Clock()
fps = 60




# joueur
personnage1 = pygame.Rect(0, 0, 50, 50)

# bloque
sol1 = pygame.Rect(0, 450, 300, 150)
sol2 = pygame.Rect(400, 450, 400, 150)
bloc1 = pygame.Rect(400, 150, 400, 150)

liste_bloc = [sol1, sol2, bloc1]




#statistique
vitesse = 10
vitesse_y = 0

saut = -15
nb_saut_perso = 2        # nombre de saut qu'as un personnage
nb_saut = nb_saut_perso  # nombre de saut restant au personnage

gravite = 0.75



#couleur 
vert = (0,255,0)
noir = (0,0,0)
rouge = (255,0,0)
blanc = (255,255,255)
marron = (100,100,100)  # n'as rien d'un marron


background = backgroundV1.creation_fond('samples/Backgroundv1.png')


ouvert = True 

while ouvert : 

    # boucle pour la fermeture de la page 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ouvert = False

        # on enclanche le saut si l'espace ou la fleche du haut est apuier et si il reste des saut
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and nb_saut > 0) or (event.type == pygame.KEYDOWN and event.key == pygame.K_UP and nb_saut > 0) :
                vitesse_y = saut
                nb_saut -= 1

    touches = pygame.key.get_pressed()
    
    # creation des image a afficher 
    #fenetre.fill(noir)
    backgroundV1.insertion_fond(fenetre, background)

    


    #calcule de la vitesse de chute 
    vitesse_y += gravite
    personnage1.y += vitesse_y
    

    
    bloc = fct_collisionsv1.colision_dessus (liste_bloc, personnage1, vitesse_y)
    if bloc != None:
            vitesse_y = 0
            personnage1.bottom = bloc.top
            nb_saut = nb_saut_perso

    bloc = fct_collisionsv1.colision_dessous (liste_bloc, personnage1, vitesse_y)
    if bloc != None:
        vitesse_y = 0
        personnage1.top = bloc.bottom


    if touches[pygame.K_LEFT] or touches[pygame.K_q] :
        personnage1.x -= vitesse
        

    if touches[pygame.K_RIGHT] or touches[pygame.K_d] :
            personnage1.x += vitesse

    
    pygame.draw.rect(fenetre, marron,sol1)
    pygame.draw.rect(fenetre, marron,sol2)
    pygame.draw.rect(fenetre, marron,bloc1)
    pygame.draw.rect(fenetre, vert,personnage1)

    #Activation du dash vers la droite
    if touches[pygame.K_LSHIFT] and touches[pygame.K_RIGHT]:
        personnage1.x += vitesse*2

    #Activation du dash vers la gauche
    if touches[pygame.K_LSHIFT] and touches[pygame.K_LEFT]:
        personnage1.x -= vitesse*2

    #Activation du rebond 

    # affichage du resultat
    pygame.display.flip()
    horloge.tick(fps)



pygame.quit()