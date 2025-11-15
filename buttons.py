import pygame
from settings import BLACK, GREY, WHITE

class Button:
    def __init__(
        self,
        x, y, width, height,
        text: str = "",
        action=None,
        img_idle=None,
        img_hover=None,
        center: bool = False
    ):
        self.text = text
        self.action = action
        self.img_idle = img_idle
        self.img_hover = img_hover
        self.use_image = img_idle is not None

        self.color_idle = (200, 200, 200)
        self.color_hover = (180, 180, 180)
        self.color_border = (0, 0, 0)
        self.text_color = (0, 0, 0)

        if self.use_image and (width is None or height is None):
            iw, ih = self.img_idle.get_size()
            width = width or iw
            height = height or ih

        if center:
            self.rect = pygame.Rect(0, 0, width, height)
            self.rect.center = (x, y)
        else:
            self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, font):
        mouse_pos = pygame.mouse.get_pos()
        # підсвітка при наведенні
        color = self.color_hover if self.rect.collidepoint(mouse_pos) else self.color_idle
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, self.color_border, self.rect, 2)

        # текст кнопки
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.action:
                self.action()
