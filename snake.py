import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.corps = [Vector2(5, 5), Vector2(4, 5), Vector2(3, 5)]
        self.direction = Vector2(1, 0)

    def afficher_serpent(self):
        for blocks in self.corps:
            serpent_rect = pygame.Rect(blocks.x * case_size, blocks.y * case_size, case_size, case_size)
            pygame.draw.rect(ecran, (200, 0, 200), serpent_rect)

    def deplacement(self):
        if self.corps[0] != fruit.position:
            corps_copie = self.corps[:-1]
            corps_copie.insert(0, corps_copie[0] + self.direction)
            self.corps = corps_copie[:]

    def collision(self):
        if self.corps[0] == fruit.position:
            corps_copie = self.corps[:]
            corps_copie.insert(0, corps_copie[0] + self.direction)
            self.corps = corps_copie[:]
            fruit.reinitialiser_position(self.corps)

        if self.corps[0].x < 0 or self.corps[0].x >= nb_de_cases or self.corps[0].y < 0 or self.corps[0].y >= nb_de_cases:
            pygame.quit()
            sys.exit()

        for block2 in self.corps[1:]:
            if self.corps[0] == block2:
                pygame.quit()
                sys.exit()

class FRUIT:
    def __init__(self):
        self.position = self.generer_position([])
        self.image = pygame.image.load("apple-pin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (case_size, case_size))

    def generer_position(self, snake_positions):
        while True:
            x = random.randint(0, nb_de_cases - 1)
            y = random.randint(0, nb_de_cases - 1)
            new_position = Vector2(x, y)
            if new_position not in snake_positions:
                return new_position

    def reinitialiser_position(self, snake_positions):
        self.position = self.generer_position(snake_positions)

    
    def afficher_fruit(self):
        fruit_rect = pygame.Rect(
        int(self.position.x * case_size),
        int(self.position.y * case_size),
        case_size,
        case_size
        )
    
        # Charger l'image du fruit (à faire UNE SEULE FOIS dans __init__)
        ecran.blit(self.image, fruit_rect)


pygame.init()

case_size = 30
nb_de_cases = 20
ecran = pygame.display.set_mode((nb_de_cases * case_size, nb_de_cases * case_size))
clock = pygame.time.Clock()
fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

def mode_échiquier():
    for y in range(nb_de_cases):
        for x in range(nb_de_cases):
            color = (0, 180, 0) if (x + y) % 2 == 0 else (0, 255, 0)
            pygame.draw.rect(ecran, color, (x * case_size, y * case_size, case_size, case_size))

def afficher_score(surface, score):
    font = pygame.font.SysFont("arial", 24, True)
    texte = font.render(f"Score : {score}", True, (255, 255, 255))
    surface.blit(texte, (10, 10))

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

    mode_échiquier()
    fruit.afficher_fruit()
    snake.collision()
    snake.afficher_serpent()
    afficher_score(ecran, len(snake.corps) - 2)

    pygame.display.update()
    clock.tick(60)

