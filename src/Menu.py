import pygame


class Menu:
    def __init__(self, window_size, scale):
        self.scale = scale
        self.window_size = window_size

    def text_objects(self, text, font):
        text_surface = font.render(text, True, (200, 200, 200))
        return text_surface, text_surface.get_rect()

    def draw(self, surface):
        self.message_display('Press Space to play', surface)

    def message_display(self, text, surface):
        large_text = pygame.font.Font('freesansbold.ttf', int(50 * self.scale))
        text_surf, text_rect = self.text_objects(text, large_text)
        text_rect.center = ((self.window_size / 2), (self.window_size / 2))
        surface.blit(text_surf, text_rect)
        pygame.display.update()
