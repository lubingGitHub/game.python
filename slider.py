import pygame



def slider_button(screen, active_colour, x_scroll):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.line(screen, active_colour, (10, 270), (110, 270))
    if 110 > cur[0] > 10 and 284 > cur[1] > 258:
        if click[0] == 1:
            x_scroll = cur[0]
    return x_scroll



