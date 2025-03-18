import pygame, sys , random
from pygame.math import Vector2
from PIL import Image
# Classe du serpent
class SNAKE:
    def __init__(self):
        self.corps = [Vector2(5, 5), Vector2(4, 5), Vector2(3, 5)]  
        self.direction = Vector2(1, 0)

    def afficher_serpent(self):
        for blocks in self.corps:
            serpent_rect = pygame.Rect(blocks.x * case_size, blocks.y * case_size, case_size, case_size)
            pygame.draw.rect(ecran, (200, 0, 200), serpent_rect)

    def deplacement(self):
        if snake.corps[0] != fruit.position:
            corps_copie = self.corps[:-1]   
            corps_copie.insert(0, corps_copie[0] + self.direction) 
            self.corps = corps_copie[:]

    def collision(self):
    # Vérifie si la tête du serpent touche le fruit
        if snake.corps[0] == fruit.position:
            corps_copie = self.corps[:]  # Crée une copie du corps du serpent
            corps_copie.append(corps_copie[-1])  # Ajoute un nouveau bloc à la fin du serpent
            self.corps = corps_copie[:]  # Met à jour le corps du serpent avec la nouvelle copie
            fruit.reinitialiser_position(snake.corps)
            game.score_value += 1  # Augmente le score de 1
          
        
        # Vérifie si la tête du serpent touche les murs
        if snake.corps[0].x < 0 or snake.corps[0].x >= nb_de_cases or snake.corps[0].y < 0 or snake.corps[0].y >= nb_de_cases:
            pygame.quit()
            sys.exit()

        # Vérifie si la tête du serpent touche son propre corps
        for block2 in self.corps[1:]:  # Compare la tête avec chaque autre segment
           if self.corps[0] == block2:
               pygame.quit()
               sys.exit()

# Classe du fruit
class FRUIT:
    def __init__(self):
        self.position = self.generer_position([])  # Initialise avec une position générée aléatoirement

    def generer_position(self, snake_positions):
        while True:
            # Générer une nouvelle position aléatoire
            x = random.randint(0, nb_de_cases - 1)
            y = random.randint(0, nb_de_cases - 1)
            new_position = Vector2(x, y)

            # S'assurer que la nouvelle position ne se trouve pas sur le serpent
            if new_position not in snake_positions:
                return new_position  # Retourne la position valide

    def reinitialiser_position(self, snake_positions):
        # Réinitialise la position du fruit en évitant le serpent
        self.position = self.generer_position(snake_positions)

    def afficher_fruit(self):
        fruit_rect = pygame.Rect(
            int(self.position.x * case_size), 
            int(self.position.y * case_size), 
            case_size, 
            case_size
        )
        ecran.blit(apple , fruit_rect)
        #pygame.draw.ellipse(ecran, (255, 0, 0), fruit_rect)

class game :
    #ndiro fiha game over 
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.score_value = 0 ; 
    def mode_échiquier(self):
        for y in range(nb_de_cases):
            for x in range(nb_de_cases):
                # Alternance de couleurs en fonction de la somme des indices x et y
                color = (0, 180, 0) if (x + y) % 2 == 0 else (0, 255, 0)
                pygame.draw.rect(ecran, color, (x * case_size, y * case_size, case_size, case_size))
    def score(self):
        score_texte = str(self.score_value)  # Utilise la variable score_value
        score_surface = game_font.render(score_texte, True, (200, 70, 10))
        score_x = int(case_size * nb_de_cases - 60)
        score_y = int(case_size * nb_de_cases - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
        ecran.blit(score_surface, score_rect)
       
# Initialisation de pygame
pygame.init()

case_size = 30 
nb_de_cases = 20  
ecran = pygame.display.set_mode((nb_de_cases * case_size, nb_de_cases * case_size))  # Taille de l'écran
clock = pygame.time.Clock()
fruit = FRUIT()
snake = SNAKE()
game = game()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE , 120)

image_path = 'apple-pin.png'
image = Image.open(image_path)

# Resize the image to 30x30 pixels
resized_image = image.resize((30, 30))

# Save the resized image
resized_image_path = 'apple-pin.png'
resized_image.save(resized_image_path)

resized_image_path

apple = pygame.image.load('apple-pin.png').convert_alpha()

game_font = pygame.font.Font(None , 25)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.deplacement()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and snake.direction != Vector2(0, 1):
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_s and snake.direction != Vector2(0, -1):
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_d and snake.direction != Vector2(-1, 0):
                snake.direction = Vector2(1, 0)
            if event.key == pygame.K_q and snake.direction != Vector2(1, 0):
                snake.direction = Vector2(-1, 0)

    # Dessiner l'échiquier
    game.mode_échiquier()
    
    fruit.afficher_fruit()
    game.score()
    snake.collision()  # Vérifie les collisions
    snake.afficher_serpent()  # Affiche le serpent
    pygame.display.update()
    clock.tick(60)