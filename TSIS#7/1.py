from numpy import around
import pygame, math

pygame.init()
pygame.display.set_caption('Graph')
screen = pygame.display.set_mode((1080, 600))

run = True
sinx, siny = 0, 300
cosx, cosy = 0, 600
start_sin_line_pts = []
start_cos_line_pts = []
end_sin_line_pts = []
end_cos_line_pts = []

for i in range(-539, 541):
    start_cos_line_pts.append((cosx, cosy))
    start_sin_line_pts.append((sinx, siny))
    sinx += 1
    cosx += 1
    siny = 300 - 300 * math.sin(i*math.pi/180)
    cosy = 300 - 300 * math.cos(i*math.pi/180)
    end_sin_line_pts.append((sinx, siny))
    #start_cos_line_pts.append((cosx, cosy)) для пунктирной линии
    end_cos_line_pts.append((cosx, cosy))

pygame.draw.line(screen, (255, 255, 255), (540, 0), (540, 600))    
pygame.draw.line(screen, (255, 255, 255), (0, 300), (1080, 300))
for i in range(len(start_sin_line_pts)):
    pygame.draw.aaline(screen, (0, 0, 255), start_sin_line_pts[i], end_sin_line_pts[i])
    pygame.draw.aaline(screen, (0, 255, 0), start_cos_line_pts[i], end_cos_line_pts[i])

pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False