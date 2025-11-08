import pygame
from settings import WHITE, GREY, BLACK

def draw_key_effect(screen, rect, is_pressed=False):
    """Малює клавішу з ефектом"""
    base_color = (220, 220, 220) if not is_pressed else (170, 220, 255)  # блакитний відтінок при натисканні
    border_color = BLACK

    # фон клавіші
    pygame.draw.rect(screen, base_color, rect, border_radius=8)
    # рамка
    pygame.draw.rect(screen, border_color, rect, 2, border_radius=8)
