
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_text(screen, text, x, y, color, font_size = 20):
    font = pygame.font.SysFont(None, font_size)  # Define a fonte e o tamanho
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def draw_top(screen, colors):
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 0, 800, 50))
    # colors
    ix = 30
    for c in colors:
        pygame.draw.rect(screen, c, pygame.Rect(ix, 15, 20, 20))
        ix += 20

    # sizes
    ix += 30
    for pos in range(1,10):
        pygame.draw.rect(screen, BLACK, pygame.Rect(ix, 15, 20, 20))
        draw_text(screen, str(pos), ix + 7, 20, WHITE)
        ix += 30

def hover_button(screen, x, y, w, h, color):
    w += x
    h += y
    for i in range(x, w + 1):
        for j in range(y, h + 1):
            if i == x or j == y or i == w or j == h:
                screen.set_at((i, j), color)