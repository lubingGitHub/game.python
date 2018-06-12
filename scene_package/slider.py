import pygame


def slider_button(screen, active_colour, x_scroll):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.line(screen, active_colour, (10, 270), (110, 270))
    if 110 > cur[0] > 10 and 284 > cur[1] > 258:
        if click[0] == 1:
            x_scroll = cur[0]
    return x_scroll

def timer(screen, button_scroll):
    x_scroll1 = slider_button(screen, (190, 190, 190), button_scroll)
    button_scroll = x_scroll1
    pygame.draw.rect(screen, ((190, 190, 190)), [x_scroll1 - 5, 258, 10, 24])
    fps_clock = pygame.time.Clock()
    fps_clock.tick(x_scroll1 - 10)
    return button_scroll

