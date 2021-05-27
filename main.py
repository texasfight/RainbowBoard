import pygame
import pygame_menu


class keyLight():
    def __init__(self, keyValue):
        keyLight.key = keyValue


def start_the_game():
    display = pygame.display.set_mode((1080, 720))
    hue = 0
    sat = 100
    lumin = 50
    alpha = 100
    color = pygame.Color(255, 255, 255)
    color.hsla = (hue, sat, lumin, alpha)
    display.fill(color)
    pygame.display.flip()
    # Create main loop variable and game loop
    running = True
    keyDown = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_a:
                #     hue = (hue + 5) % 360
                # if event.key == pygame.K_0:
                keyDown = True
            if event.type == pygame.KEYUP:
                keyDown = False
            if event.type == pygame.QUIT:
                running = False
        if keyDown:
            hue = (hue - .04) % 360
            pygame.display.update()
        color.hsla = (hue, sat, lumin, alpha)
        display.fill(color)
        pygame.display.update()
    pass


def main():
    pygame.init()

    logo = pygame.image.load("logo_32_32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Rainbow Keyboard Game")

    screen = pygame.display.set_mode((1080, 720))

    menu = pygame_menu.Menu('RainbowBoard', 1080, 720,
                            theme=pygame_menu.themes.THEME_DARK)

    menu.add.text_input('Name: ', default='Matthew')
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)


if __name__ == "__main__":
    main()
