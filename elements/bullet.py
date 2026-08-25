if __name__ == "__main__":
    raise RuntimeError("\033c❌ ESTE ARCHIVO NO DEBE EJECUTARSE. EJECUTA main.py")

import pygame
from pygame.math import Vector2

# TODO (2.1): Cargar imagen de la bala


class Bullet(pygame.sprite.Sprite):
    # TODO (2.2): Agregar parametros al constructor
    def __init__(self):

        # ? super().__init__() inicializa la clase padre (Sprite)
        super().__init__()

        # TODO (2.1): Aspecto inicial de nuestra bala

        # TODO (2.2): Posicionar la bala en la posición inicial

        # TODO (2.2): Variables requeridas por nuestra bala

        # TODO (3.1): Rotar la bala para que apunte en la dirección correcta

    def update(self):
        # TODO (2.3): Mover la bala

        # TODO (2.3): Eliminar la bala si sale de la pantalla
        pass
