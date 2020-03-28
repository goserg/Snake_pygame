import pygame
import utils.Controller as Controller


class Menu:
    def __init__(self, window_size, scale):
        self.scale = scale
        self.window_size = window_size
        self.selected_color = (200, 200, 200)
        self.shaded_color = (100, 100, 100)
        self.state = 0
        self.grid = "On"
        self.scale = 1

    def draw(self, surface):
        self.message_display('PLAY', surface,
                             self.selected_color if self.state == 0 else self.shaded_color, -1)
        self.message_display('grid: {}'.format(self.grid), surface,
                             self.selected_color if self.state == 1 else self.shaded_color, 0)
        self.message_display('scale: x{}'.format(self.scale), surface,
                             self.selected_color if self.state == 2 else self.shaded_color, 1)
        self.message_display('quit', surface,
                             self.selected_color if self.state == 3 else self.shaded_color, 2)

    def message_display(self, text, surface, color, n):
        size = int(50 * self.scale)
        font = pygame.font.Font('freesansbold.ttf', size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect()
        text_rect.center = ((self.window_size * self.scale/ 2), (self.window_size * self.scale / 2) + n * size)
        surface.blit(text_surf, text_rect)
        pygame.display.update()

    def switch(self):
        if Controller.get_direction()[1] == -1:
            self.switch_up()
            return True
        elif Controller.get_direction()[1] == 1:
            self.switch_down()
            return True

    def switch_grid(self):
        if self.grid == "On":
            self.grid = "Off"
            return
        self.grid = "On"

    def switch_scale(self):
        self.scale = 1 if self.scale == 1.5 else 1.5

    def switch_up(self):
        if self.state == 0:
            self.state = 3
        else:
            self.state -= 1

    def switch_down(self):
        if self.state == 3:
            self.state = 0
        else:
            self.state += 1

    def get_state(self):
        return self.state
