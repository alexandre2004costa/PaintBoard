import pygame
from func import draw_text
from func import draw_top
from func import hover_button

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
DARK_GREEN = (0, 100, 0)
DARK_RED = (139, 0, 0)
DARK_BLUE = (0, 0, 139)
NEON_GREEN = (57, 255, 20)


colors = [WHITE, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, PURPLE, BROWN, DARK_GREEN, DARK_BLUE, DARK_RED]

pygame.font.init()
font = pygame.font.SysFont(None, 20)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint Board")

screen.fill(BLACK)
draw_top(screen, colors)
hover_button(screen, 60 + len(colors) * 20 + 30 * (2 // 2 - 1), 15, 20, 20, NEON_GREEN) # size button
hover_button(screen, 30 + 0 * 20, 15, 20, 20, NEON_GREEN)# color button



pygame.display.flip()

running = True
drawing = False
erasing = False
paintColor = WHITE
drawSize = 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                pygame.draw.rect(screen, BLACK, pygame.Rect(0, 50, 800, 600))
            elif event.key == pygame.K_s:
                pygame.image.save(screen, "screenshot.png")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y <= 50:
                if x >= 30 and x <= 30 + len(colors) * 20 and y >= 15 and y <= 35:
                    index = (x - 30) // 20
                    paintColor = colors[index]
                    draw_top(screen, colors)
                    hover_button(screen, 60 + len(colors) * 20 + 30 * (drawSize // 2 - 1), 15, 20, 20, NEON_GREEN) # size button
                    hover_button(screen, 30 + index * 20, 15, 20, 20, NEON_GREEN)# color button
                elif y >= 15 and y <= 35 and x >= 60 + len(colors) * 20 and x <= 60 + len(colors) * 20 + 9*30:
                    index = (x - 360) // 30
                    if (x - 360) % 30 < 20:
                        drawSize = (index + 1) * 2
                        draw_top(screen, colors)
                        hover_button(screen, 30 + colors.index(paintColor)*20 , 15, 20, 20, NEON_GREEN) # color button
                        hover_button(screen, 60 + len(colors) * 20 + 30 * index, 15, 20, 20, NEON_GREEN) # size button
            elif event.button == 1:
                drawing = True
            elif event.button == 3:
                erasing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
            elif event.button == 3:
                erasing = False
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if y <= 50 + drawSize:
                continue
            if drawing:
                pygame.draw.circle(screen, paintColor, (x, y), drawSize)
            elif erasing:
                pygame.draw.circle(screen, BLACK, (x, y), drawSize)                
        pygame.display.flip()
    



pygame.quit()
