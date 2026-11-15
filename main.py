import pygame 
import fct_collisions
import background
import fct_dash

pygame.init()

fenetre = pygame.display.set_mode((800,600))
horloge = pygame.time.Clock()
fps = 60


largeur_fenetre = 800
largeur_niveau = 2400     
camera_x = 0

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

obs6 = background.load_image('samples/sol6.png', 224, 80)
obs6_rect = background.obstacle_rect(obs6, 800, 520, 224, 80)

obs7 = background.load_image('samples/plateforme_1.png', 128, 48)
obs7_rect = background.obstacle_rect(obs7, 1100, 400, 128, 48)

obs8 = background.load_image('samples/sol6.png', 224, 80)
obs8_rect = background.obstacle_rect(obs8, 1400, 520, 224, 80)


liste_bloc = [obs1_rect, obs2_rect, obs3_rect, obs4_rect, obs5_rect, obs6_rect, obs7_rect, obs8_rect]
liste_images = [obs1, obs2, obs3, obs4, obs5, obs6, obs7, obs8]




#statistique
vitesse_y = 0
vitesse_x = 0


saut = -10
nb_saut_perso = 5        # nombre de saut qu'as un personnage
nb_saut = nb_saut_perso  # nombre de saut restant au personnage


vitesse_dash = 40        # pixels par image pendant le dash
duree_dash = 5           # nombre d'images du dash 
dash_restant = 0         # images de dash qu'il reste à faire
direction_dash = 0       # 1 = droite, -1 = gauche, 0 = pas de dash 
nb_dash_perso = 1
nb_dash = nb_dash_perso


gravite = 0.75
vitesse_max = 10
velocite = 2             # accélération
frottement = 2           # freinage quand on relâche


#couleur 
vert = (0,255,0)
noir = (0,0,0)
rouge = (255,0,0)
blanc = (255,255,255)
marron = (100,100,100)  # n'as rien d'un marron


fond = background.creation_fond('samples/Backgroundv1.png')


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
        nb_dash, direction_dash, dash_restant = fct_dash.activation_dash(event, droite, gauche, nb_dash, direction_dash, dash_restant, duree_dash)

    
    
  


      
    # calcul de la vitesse horizontale si l'on presse une touche de deplacement 
    if direction_dash != 0:
        vitesse_x, vitesse_y, dash_restant, direction_dash = fct_dash.mise_a_jour_dash(direction_dash, dash_restant, vitesse_dash, vitesse_max)
    else:    
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
    bloc = fct_collisions.colision_droite (liste_bloc, personnage1, vitesse_x)
    if bloc != None:
        vitesse_x = 0
        personnage1.left = bloc.right
    
    
    bloc = fct_collisions.colision_gauche (liste_bloc, personnage1, vitesse_x)
    if bloc != None:
        vitesse_x = 0
        personnage1.right = bloc.left
    
   

    # calcule de la vitesse de chute 
    vitesse_y += gravite
    # déplacement vertical
    personnage1.y += vitesse_y



   # on aplique les colision en y
    bloc = fct_collisions.colision_dessus (liste_bloc, personnage1, vitesse_y)
    if bloc != None:
        vitesse_y = 0
        personnage1.bottom = bloc.top
        nb_saut = nb_saut_perso
        nb_dash = nb_dash_perso
            

    bloc = fct_collisions.colision_dessous (liste_bloc, personnage1, vitesse_y)
    if bloc != None:
        vitesse_y = 0
        personnage1.top = bloc.bottom






    # respawn
    if touches[pygame.K_j]:
        personnage1.y = 0
        personnage1.x = 100
        vitesse_y = 100

    # position de la camera
    camera_x = personnage1.centerx - largeur_fenetre // 2
    camera_x = max(0, min(camera_x, largeur_niveau - largeur_fenetre))


    fenetre.fill(noir)
    background.insertion_fond(fenetre, fond)   # on met le fond

    for image, rect in zip(liste_images, liste_bloc):
        fenetre.blit(image, rect.move(-camera_x, 0))

    pygame.draw.rect(fenetre, vert, personnage1.move(-camera_x, 0))

    
    #pygame.draw.rect(fenetre, marron,sol1)
    #pygame.draw.rect(fenetre, marron,sol2)
    #pygame.draw.rect(fenetre, marron,bloc1)
   

   

    #Activation du rebond 

    # affichage du resultat
    pygame.display.flip()
    horloge.tick(fps)



pygame.quit()