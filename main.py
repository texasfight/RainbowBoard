import pygame


def main():
    pygame.init()

    logo = pygame.image.load("logo_32_32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Rainbow Keyboard Game")

    screen = pygame.display.set_mode((1080, 720))
    hue = 0
    sat = 50
    lumin = 50
    alpha = 100
    color = pygame.Color(255, 255, 255)
    color.hsla = (hue, sat, lumin, alpha)
    screen.fill(color)
    pygame.display.flip()
    # Create main loop variable and game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    hue = (hue + 5) % 360
                if event.key == pygame.K_0:
                    hue = (hue - 5) % 360
            color.hsla = (hue, sat, lumin, alpha)
            screen.fill(color)
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == "__main__":
    main()