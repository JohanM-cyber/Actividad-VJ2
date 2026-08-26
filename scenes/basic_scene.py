if __name__ == "__main__":
    raise RuntimeError("\033c❌ ESTE ARCHIVO NO DEBE EJECUTARSE. EJECUTA main.py")

import pygame
from pygame.locals import K_RETURN, KEYDOWN, QUIT


def gameloop(screen):

    # Inicializamos el reloj
    clock = pygame.time.Clock()

    running = True

    # Definimos la fuente y texto a usar
    font = pygame.font.Font(None, 48)
    line1 = font.render("EXPERIENCIA VJ-2", True, (255, 255, 255), (0, 0, 0))
    line2 = font.render("Aprieta ENTER para iniciar el juego", True, (255, 255, 255), (0, 0, 0))
    line3 = font.render("¡COOLDOWN DE 5 SEGUNDOS!", True, (255, 255, 255), (0, 0, 0))

    # Definimos las posiciones de los textos
    line1_rect = line1.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 - 25)
    )

    line2_rect = line2.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 25)
    )

    line3_rect = line3.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 75)
    )

    # Iniciamos el loop principal de la escena inicial
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    running = False
            elif event.type == QUIT:
                running = False

        # Fondo de pantalla
        fondo = pygame.image.load("assets/carga.png")
        fondo_scaled = pygame.transform.scale(fondo, (screen.get_width(), screen.get_height()))
        screen.blit(fondo_scaled, (0, 0))

        # Dibujar textos
        screen.blit(line1, line1_rect)
        screen.blit(line2, line2_rect)
        screen.blit(line3, line3_rect)

        # Actualizar pantalla
        pygame.display.flip()

        # Limitar FPS
        clock.tick(30)
