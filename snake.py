import pygame, sys , random
from   pygame.math import Vector2
#here
class SNAKE:
    def __init__(self):
        self.corps = [Vector2(5, 5), Vector2(4, 5), Vector2(3, 5)]  
        self.direction = Vector2(1, 0)
     
    
    def afficher_serpent(self):
        for blocks in self.corps :
            serpent_rect = pygame.Rect( int(blocks.x * case_size), int(blocks.y * case_size) ,case_size,case_size)
            pygame.draw.rect(ecran , (200,0,200), serpent_rect)

    def deplacement(self):
        corps_copie = self.corps[:-1]   
        corps_copie.insert(0,corps_copie[0]+ self.direction) 
        self.corps = corps_copie[:] 
  

        

class FRUIT :
    def __init__(self) :
        self.x = random.randint(0 , nb_de_cases-1)
        self.y = random.randint(0, nb_de_cases-1)
        self.position = Vector2(self.x , self.y)

    def afficher_fruit(self):
        fruit_rect = pygame.Rect(int(self.position.x *case_size ), int(self.position.y *  case_size), case_size , case_size)
        pygame.draw.ellipse(ecran , (255,0,0) , fruit_rect)

pygame.init()

case_size = 30 
nb_de_cases = 20  
ecran = pygame.display.set_mode((nb_de_cases * case_size, nb_de_cases * case_size))  # Taille de l'écran
clock = pygame.time.Clock()
fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE , 150)
#150 ms

# Fonction pour dessiner l'échiquier
def mode_échiquier():
    for y in range(nb_de_cases):
        for x in range(nb_de_cases):
            # Alternance de couleurs en fonction de la somme des indices x et y
            color = (0, 180, 0) if (x + y) % 2 == 0 else (0, 255, 0)
            pygame.draw.rect(ecran, color, (x * case_size, y * case_size, case_size, case_size))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.deplacement()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != Vector2(0, 1):
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and snake.direction != Vector2(0, -1):
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT and snake.direction != Vector2(-1, 0):
                snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT and snake.direction != Vector2(1, 0):
                snake.direction = Vector2(-1, 0)

    # Dessiner l'échiquier
    mode_échiquier()
    fruit.afficher_fruit()
    snake.afficher_serpent()
    pygame.display.update()
    clock.tick(60)
