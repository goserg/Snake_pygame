from typing import Tuple

import pygame

from window_manager import window
import utils.settings as s
import utils.controller as controller


def message_display(text: str, color: Tuple[int, int, int], n: int) -> None:
    size = int(s.font_size * s.scale)
    font = pygame.font.Font(s.font, size)
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect()
    text_rect.center = ((s.window_size * s.scale / 2), (s.window_size * s.scale / 2) + n * size)
    window.blit(text_surf, text_rect)
    pygame.display.update()


class Menu:
    def __init__(self) -> None:
        self.state = 0

    def draw(self) -> None:
        message_display(
            'PLAY',
            s.m_selected_color if self.state == 0 else s.m_shaded_color,
            -1,
        )
        message_display(
            'grid: {}'.format("On" if s.grid else "Off"),
            s.m_selected_color if self.state == 1 else s.m_shaded_color,
            0,
        )
        message_display(
            'scale: x{}'.format(s.scale),
            s.m_selected_color if self.state == 2 else s.m_shaded_color,
            1,
        )
        message_display(
            'quit',
            s.m_selected_color if self.state == 3 else s.m_shaded_color,
            2,
        )

    def switch(self) -> bool:
        if controller.get_direction()[1] == -1:
            self.switch_up()
            return True
        elif controller.get_direction()[1] == 1:
            self.switch_down()
            return True

    def switch_up(self) -> None:
        if self.state == 0:
            self.state = 3
        else:
            self.state -= 1

    def switch_down(self) -> None:
        if self.state == 3:
            self.state = 0
        else:
            self.state += 1

    def get_state(self) -> int:
        return self.state
