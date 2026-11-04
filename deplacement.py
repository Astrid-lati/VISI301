import pygame 
import fct_collisionsv1
import background

pygame.init()

fenetre = pygame.display.set_mode((800,600))
horloge = pygame.time.Clock()
fps = 60

class personnage:
    def __init__(self,nom):
          self.nom = nom
          self.vitesse = 10
          self.saut = 2
          self.saut_restant = self.saut

    def dash(self):
         pass

    def changer_personnage():
         pass


# joueur
personnage1 = pygame.Rect(0, 0, 30, 30)

# bloque
#sol1 = pygame.Rect(0, 450, 300, 150)
#sol2 = pygame.Rect(400, 450, 400, 150)
#bloc1 = pygame.Rect(400, 150, 400, 150)

#liste_bloc = [sol1, sol2, bloc1]


obs1 = background.load_image('samples/sol6.png', 224, 80)
obs1_rect = background.obstacle_rect(obs1, 0, 520, 224, 80)

obs2 = background.load_image('samples/sol6.png', 224, 80)
obs2_rect = background.obstacle_rect(obs2, 400, 520, 224, 80)

obs3 = background.load_image('samples/plateforme_1.png', 128, 48)
obs3_rect = background.obstacle_rect(obs3, 450, 300, 128, 48)

obs4 = background.load_image('samples/plateforme_2.png', 128, 48)
obs4_rect = background.obstacle_rect(obs4, 0, 220, 128, 48)

obs5 = background.load_image('samples/plateforme_3.png', 128, 48)
obs5_rect = background.obstacle_rect(obs5, 400, 520, 128, 48)


liste_bloc = [obs1_rect, obs2_rect, obs3_rect, obs4_rect, obs5_rect]




#statistique
vitesse_y = 0
vitesse_x = 0


saut = -15
nb_saut_perso = 2        # nombre de saut qu'as un personnage
nb_saut = nb_saut_perso  # nombre de saut restant au personnage

dash = 200               # distance du dash
nb_dash_perso = 1        # nombre de dash qu'as un personnage
nb_dash = nb_dash_perso  # nombre de dash restant au personnage

gravite = 0.75
vitesse_max = 15
velocite = 5             # accélération
frottement = 2           # freinage quand on relâche


#couleur 
vert = (0,255,0)
noir = (0,0,0)
rouge = (255,0,0)
blanc = (255,255,255)
marron = (100,100,100)  # n'as rien d'un marron


background = background.creation_fond('samples/Backgroundv1.png')


ouvert = True 

while ouvert : 

    touches = pygame.key.get_pressed()
     
    # touche de deplacement 
    gauche = touches[pygame.K_LEFT] or touches[pygame.K_q]
    droite = touches[pygame.K_RIGHT] or touches[pygame.K_d]

    


    # boucle pour la fermeture de la page 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ouvert = False

        # on enclanche le saut si l'espace ou la fleche du haut est apuier et si il reste des saut
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and nb_saut > 0) or (event.type == pygame.KEYDOWN and event.key == pygame.K_UP and nb_saut > 0) :
            vitesse_y = saut
            nb_saut -= 1

         #Activation du dash vers la droite
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT and touches[pygame.K_RIGHT] and nb_dash > 0) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT and touches[pygame.K_d] and nb_dash > 0):
            personnage1.x += dash
            nb_dash -= 1
        
            #Activation du dash vers la gauche
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT and touches[pygame.K_LEFT] and nb_dash > 0) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT and touches[pygame.K_q] and nb_dash > 0):
            personnage1.x -= dash
            nb_dash -= 1

    
    
    # creation des image a afficher 
    fenetre.fill(noir)
    background.insertion_fond(fenetre, background)
    fenetre.blit(obs1,obs1_rect)
    fenetre.blit(obs2,obs2_rect)
    fenetre.blit(obs3,obs3_rect)
    fenetre.blit(obs4,obs4_rect)
    
      
    # calcul de la vitesse horizontale si l'on presse une touche de deplacement 
    if gauche and not droite:
        vitesse_x = max(vitesse_x - velocite, -vitesse_max)

    elif droite and not gauche:
        vitesse_x = min(vitesse_x + velocite, vitesse_max)

    else:
        # aucune touche ou les deux on ralentit vers 0
        if vitesse_x > 0:
            vitesse_x = max(vitesse_x - frottement, 0)

        elif vitesse_x < 0:
            vitesse_x = min(vitesse_x + frottement, 0)

    # déplacement horizontal
    personnage1.x += vitesse_x


    # on aplique les colision en x
    bloc = fct_collisionsv1.colision_droite (liste_bloc, personnage1, vitesse_x)
    if bloc != None:
        vitesse_x = 0
        personnage1.left = bloc.right
    
    
    bloc = fct_collisionsv1.colision_gauche (liste_bloc, personnage1, vitesse_x)
    if bloc != None:
        vitesse_x = 0
        personnage1.right = bloc.left
    
   

    # calcule de la vitesse de chute 
    vitesse_y += gravite
    # déplacement vertical
    personnage1.y += vitesse_y



   # on aplique les colision en y
    bloc = fct_collisionsv1.colision_dessus (liste_bloc, personnage1, vitesse_y)
    if bloc != None:
        vitesse_y = 0
        personnage1.bottom = bloc.top
        nb_saut = nb_saut_perso
        nb_dash = nb_dash_perso
            

    bloc = fct_collisionsv1.colision_dessous (liste_bloc, personnage1, vitesse_y)
    if bloc != None:
        vitesse_y = 0
        personnage1.top = bloc.bottom






    # respone
    if touches[pygame.K_j]:
        personnage1.y = 0
        personnage1.x = 100
        vitesse_y = 100



    
    #pygame.draw.rect(fenetre, marron,sol1)
    #pygame.draw.rect(fenetre, marron,sol2)
    #pygame.draw.rect(fenetre, marron,bloc1)
    pygame.draw.rect(fenetre, vert,personnage1)

   

    #Activation du rebond 

    # affichage du resultat
    pygame.display.flip()
    horloge.tick(fps)



pygame.quit()