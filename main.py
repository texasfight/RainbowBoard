import pygame
import pygame_menu


class keyLight():
    def __init__(self, keyValue):
        keyLight.key = keyValue


def start_the_game():
    # Set up surfaces
    screen = pygame.display.set_mode((1080, 720))
    canvas = pygame.Surface((1080, 720))
    left_side = pygame.Rect(0, 0, 540, 720)
    right_side = pygame.Rect(540, 0, 540, 720)
    sub_left = canvas.subsurface(left_side)
    sub_right = canvas.subsurface(right_side)

    screen.blit(canvas, [0,0])
    screen.blit(sub_right, [540, 0])
    screen.blit(sub_left, [0, 0])

    left_hue = 0
    right_hue = 0
    sat = 100
    lumin = 50
    alpha = 100
    left_color = pygame.Color(255, 255, 255)
    left_color.hsla = (left_hue, sat, lumin, alpha)
    sub_left.fill(left_color)
    right_color = pygame.Color(255, 255, 255)
    right_color.hsla = (right_hue, sat, lumin, alpha)
    sub_right.fill(right_color)

    pygame.display.flip()

    # Create main loop variable and game loop
    running = True
    left_key_down = False
    right_key_down = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                left_key_down = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_q:
                left_key_down = False
            elif event.type == pygame.KEYDOWN:
                right_key_down = True
            elif event.type == pygame.KEYUP:
                right_key_down = False

            if event.type == pygame.QUIT:
                running = False

        if left_key_down:
            left_hue = (left_hue - .12) % 360
            left_color.hsla = (left_hue, sat, lumin, alpha)
            sub_left.fill(left_color)
        if right_key_down:
            right_hue = (right_hue - .12) % 360
            right_color.hsla = (right_hue, sat, lumin, alpha)
            sub_right.fill(right_color)
        screen.blit(canvas, [0, 0])
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
