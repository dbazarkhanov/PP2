import pygame, time, random, pickle, json

pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255,255,102)
GREEN = (0,255,0)
GREY = (128,128,128)
LIGHT_GREY = (211,211,211)

COLOR = COLORp1 = COLORp2 = COLORe = COLORm = COLORh = GREY

screenX = 800
screenY = 600

screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption('Snake game')

FPS = 30
fps = pygame.time.Clock()

score = 0
numberOfPlayers = 0
difficulty = 0
wall_rect = [[random.randrange(0, screenX//2, 10), 10], [10, random.randrange(0, screenY//2, 10)]]

font_gameover = pygame.font.SysFont('Verdana' , 70)
score_font = pygame.font.SysFont('Verdana', 35)
font_start = pygame.font.SysFont('Times New Roman', 45)
font_diff = pygame.font.SysFont('Times New Roman', 20)

run = False
isGameOver = False
menu = True
'''
def load_settings():
    global data
    with open('save.json', 'r') as f:
        data = json.load(f)
'''
def Start(rect, x, y):
    if rect.left <= x <= rect.right and rect.top <= y <= rect.bottom and numberOfPlayers != 0:
        global menu, run
        menu = False
        run = True
'''
def load():
    global score, all_sptites, walls
'''
def numOfPlayers(rect1, rect2, x, y):
    global numberOfPlayers, COLORp1, COLORp2
    if rect1.left <= x <= rect1.right and rect1.top <= y <= rect1.bottom:
        numberOfPlayers = 1
        COLORp1 = LIGHT_GREY
        COLORp2 = GREY
    elif rect2.left <= x <= rect2.right and rect2.top <= y <= rect2.bottom:
        numberOfPlayers = 2
        COLORp2 = LIGHT_GREY
        COLORp1 = GREY

def diff(rect1, rect2, rect3, x, y):
    global difficulty, COLORe, COLORm, COLORh
    if rect1.left <= x <= rect1.right and rect1.top <= y <= rect1.bottom:
        difficulty = 1
        COLORe = LIGHT_GREY
        COLORm = COLORh = GREY
    elif rect2.left <= x <= rect2.right and rect2.top <= y <= rect2.bottom:
        difficulty = 2
        COLORm = LIGHT_GREY
        COLORe = COLORh = GREY
    elif rect3.left <= x <= rect3.right and rect3.top <= y <= rect3.bottom:
        difficulty = 3
        COLORh = LIGHT_GREY
        COLORe = COLORm = GREY

def render(surface, text, size, x, y):
    font = pygame.font.SysFont('Times New Roman', size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def back(surface, w, h, x, y, clr):#upgrade this shit
    backg = pygame.Surface((w, h)).get_rect(center=(x, y))
    pygame.draw.rect(surface, clr, backg)

while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Start(back_start, event.pos[0], event.pos[1])
                numOfPlayers(back_player1, back_player2, event.pos[0], event.pos[1])
                diff(back_ez, back_med, back_hard, event.pos[0], event.pos[1])

    back_start = pygame.Surface((225, 40)).get_rect(center=(screenX//2, 150))
    back_player1 = pygame.Surface((225, 40)).get_rect(center=(screenX//2, 250))
    back_player2 = pygame.Surface((225, 40)).get_rect(center=(screenX//2, 300))
    back_ez = pygame.Surface((60, 30)).get_rect(center=(screenX//3*1.2, 340))
    back_med = pygame.Surface((90, 30)).get_rect(center=(screenX//3*1.5, 340))
    back_hard = pygame.Surface((60, 30)).get_rect(center=(screenX//3*1.8, 340))
    back_load = pygame.Surface((232, 40)).get_rect(center=(screenX//2, 200))

    pygame.draw.rect(screen, COLOR, back_start)
    pygame.draw.rect(screen, COLOR, back_load)
    pygame.draw.rect(screen, COLORp1, back_player1)
    pygame.draw.rect(screen, COLORp2, back_player2)
    pygame.draw.rect(screen, COLORe, back_ez)
    pygame.draw.rect(screen, COLORm, back_med)
    pygame.draw.rect(screen, COLORh, back_hard)

    render(screen, 'START', 45, screenX//2, 150)
    render(screen, 'CONTINUE', 45, screenX//2, 200)
    render(screen, '1 PLAYER', 45, screenX//2, 250)
    render(screen, '2 PLAYER', 45, screenX//2, 300)
    render(screen, 'EASY', 20, screenX//3*1.2, 340)
    render(screen, 'MEDIUM', 20, screenX//3*1.5, 340)
    render(screen, 'HARD', 20, screenX//3*1.8, 340)

    pygame.display.flip()

class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.head = [x, y]
        self.body = [[x, y]]
        self.surf = pygame.Surface((10, len(self.body)))
        self.rect = self.surf.get_rect(topleft=self.head)
        self.speed = 10
        self.direction = 'STOP'

    def update(self):
        if self.direction == 'UP' or self.direction == 'w':
            self.head[1] -= self.speed
        if self.direction == 'DOWN' or self.direction == 's':
            self.head[1] += self.speed
        if self.direction == 'LEFT' or self.direction == 'a':
            self.head[0] -= self.speed
        if self.direction == 'RIGHT' or self.direction == 'd':
            self.head[0] += self.speed

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.rect = self.surf.get_rect(topleft=(random.randrange(0, screenX+10, 10), random.randrange(0, screenY+10, 10)))

    def update(self):
        self.surf.fill(RED)
        screen.blit(self.surf, self.rect)

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(wall_rect[random.randint(0, 1)])
        self.rect = self.surf.get_rect(topleft=(random.randrange(0, screenX//2, 10), random.randrange(0, screenY//2, 10)))

    def update(self):
        self.surf.fill(YELLOW)
        screen.blit(self.surf, self.rect)

walls = pygame.sprite.Group()
all_sptites = pygame.sprite.Group()
players = pygame.sprite.Group()

if numberOfPlayers == 1:
    P1 = Snake(200, 100)
    all_sptites.add(P1)
    players.add(P1)
elif numberOfPlayers == 2:
    P1 = Snake(200, 100)
    P2 = Snake(600, 400)
    all_sptites.add(P1)
    all_sptites.add(P2)
    players.add(P1)
    players.add(P2)

F1 = Food()
all_sptites.add(F1)

for i in ['W1', 'W2', 'W3', 'W4', 'W5']:
    i = Wall()
    walls.add(i)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if numberOfPlayers == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    P1.direction = 'UP'
                if event.key == pygame.K_DOWN:
                    P1.direction = 'DOWN'
                if event.key == pygame.K_LEFT:
                    P1.direction = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    P1.direction = 'RIGHT'
        elif numberOfPlayers == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    P1.direction = 'UP'
                if event.key == pygame.K_DOWN:
                    P1.direction = 'DOWN'
                if event.key == pygame.K_LEFT:
                    P1.direction = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    P1.direction = 'RIGHT'
                if event.key == pygame.K_w:
                    P2.direction = 'w'
                if event.key == pygame.K_s:
                    P2.direction = 's'
                if event.key == pygame.K_a:
                    P2.direction = 'a'
                if event.key == pygame.K_d:
                    P2.direction = 'd'

    screen.fill(BLACK)
   
    if difficulty == 2:
        walls.update()

    if difficulty == 3:
        walls.update()
        FPS = 60

    all_sptites.update()
    
    if numberOfPlayers == 2:
        for pos in P2.body:
            pygame.draw.rect(screen, BLUE, (pos[0], pos[1], 10, 10))

        P2.body.insert(0, list(P2.head))
        if P2.head[0] == F1.rect.x and P2.head[1] == F1.rect.y:
            score += 1
            F1.__init__()
        else:
            P2.body.pop()

    for pos in P1.body:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], 10, 10))

    P1.body.insert(0, list(P1.head))
    if P1.head[0] == F1.rect.x and P1.head[1] == F1.rect.y:
        score += 1
        F1.__init__()
    else:
        P1.body.pop()

    Score = score_font.render(str(score), True, WHITE)
    game_over = font_gameover.render('GAME OVER', True, RED)
    screen.blit(Score, (10, 10))
    
    if isGameOver:
            time.sleep(1)
            run = False
    
    if numberOfPlayers == 2:
        if P2.head[0] > screenX or P2.head[1] > screenY or P2.head[0] < -10 or P2.head[1] < -10:
            P2.kill() 

    if P1.head[0] > screenX or P1.head[1] > screenY or P1.head[0] < -10 or P1.head[1] < -10:
        P1.kill()
        
    if numberOfPlayers == 2:
        if not players.has(P1) and not players.has(P2):
            screen.fill(BLACK)
            screen.blit(game_over, (180, 250))
            screen.blit(Score, (10, 10))
            isGameOver = True
    elif numberOfPlayers == 1:
        if not players.has(P1):
            screen.fill(BLACK)
            screen.blit(game_over, (180, 250))
            screen.blit(Score, (10, 10))
            isGameOver = True
    
    print(pygame.sprite.groupcollide(players, walls, True, True))

    pygame.display.update()
    fps.tick(FPS)