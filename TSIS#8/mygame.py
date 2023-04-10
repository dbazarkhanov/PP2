import pygame as pg, time, random

pg.init()

FPS = 60
fps = pg.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCORE = 0
COINS = 0

font = pg.font.SysFont('Verdana', 60)
game_over = font.render('Game Over', True, BLACK)

font_small = pg.font.SysFont('Verdana', 20)
background = pg.image.load('AnimatedStreet.png')

screen = pg.display.set_mode((400,600))
screen.fill(WHITE)
pg.display.set_caption('Game')

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('Enemy.png')
        self.surf = pg.Surface((42, 70))
        self.rect = self.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), -100))
        self.speed = random.randint(1, 5)

    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > SCREEN_HEIGHT + 70:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            self.speed = random.randint(1, 5)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load('Player.png')
        self.surf = pg.Surface((40, 75))
        self.rect = self.surf.get_rect(center=(160, 520))
       
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT] and self.rect.x in range(SCREEN_WIDTH - 40):
            self.rect.move_ip(5, 0)
        if keys[pg.K_LEFT] and self.rect.x in range(5, SCREEN_WIDTH):
            self.rect.move_ip(-5, 0)

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('coin.png')
        self.surf = pg.Surface((50, 50))
        self.rect = self.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), -70))

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT + 50:
            self.rect = self.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), -70))
    
    def collect(self):
        if pg.sprite.spritecollideany(P1, coins):
            global COINS, SCORE
            self.rect = self.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), -70))
            COINS += 1
            SCORE += 2

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pg.sprite.Group()
enemies.add(E1)

coins = pg.sprite.Group()
coins.add(C1)

all_sprites = pg.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

pg.mixer.music.load('background.wav')
pg.mixer.music.play(-1)

run = True

while run: 
    for event in pg.event.get():  
        if event.type == pg.QUIT:
            run = False

    screen.blit(background, (0, 0))
    scores = font_small.render('SCORE: ' + str(SCORE), True, BLACK)
    coins_font = font_small.render(str(COINS), True, BLACK)
    screen.blit(scores, (10, 10))   
    screen.blit(coins_font, (370, 10))
    screen.blit(pg.transform.scale(pg.image.load('coin.png'), (20, 20)), (345, 13))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if C1.rect.x in range(E1.rect.x - 50, E1.rect.x + 51):
        C1.rect = C1.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), -70))

    for coin in coins:
        coin.collect()

    if pg.sprite.spritecollideany(P1, enemies):
        pg.mixer.Sound('crash.wav').play()
        time.sleep(1)
                   
        font_small = pg.font.SysFont('Verdana', 35)
        scores = font_small.render('SCORE: ' + str(SCORE), True, BLACK)
        coins_font = font_small.render(str(COINS), True, BLACK)

        screen.fill(RED)
        screen.blit(scores, (100, 330))   
        screen.blit(coins_font, (200, 380))
        screen.blit(pg.transform.scale(pg.image.load('coin.png'), (40, 40)), (150, 380))
        screen.blit(game_over, (30,250))
          
        pg.display.update()
        for entity in all_sprites:
            entity.kill() 
                
        time.sleep(2)
        run = False      
        
    pg.display.update()
    fps.tick(FPS)