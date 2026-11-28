import sys

import pygame

WIDTH, HEIGHT = 480, 720
FPS = 60
BANK = 60                      

GRASS = (95, 185, 95)
RIVER = (55, 145, 215)
RIPPLE = (120, 185, 235)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Nouka Runner")
    clock = pygame.time.Clock()

    offset = 0                  
    running = True
    while running:
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        offset = (offset + 3) % 40

        screen.fill(GRASS)                                                  # banks
        pygame.draw.rect(screen, RIVER, (BANK, 0, WIDTH - 2 * BANK, HEIGHT))  # river
        for y in range(-40 + offset, HEIGHT, 40):                           # ripples
            pygame.draw.line(screen, RIPPLE, (BANK + 30, y), (BANK + 60, y), 2)
            pygame.draw.line(screen, RIPPLE, (WIDTH - BANK - 90, y + 20), (WIDTH - BANK - 60, y + 20), 2)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()