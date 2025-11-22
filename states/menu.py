import pygame as pg
import os
from settings import GREEN, LIGHT_GREEN


class Menu:
    def __init__(self, width, height, change_state):
        self.width = width
        self.height = height
        self.change_state = change_state

        #CARGAR FONDO
        base_path = os.path.dirname(os.path.dirname(__file__))  # sube desde /states/
        bg_path = os.path.join(base_path, "assets", "images", "background.png")
        self.background = pg.image.load(bg_path).convert()
        self.background = pg.transform.scale(self.background, (width, height)) #AJUSTA LA IMAGEN AL TAMAÑO DE LA VENTANA

        #CARGAR LA TIPOGRAFÍA PIXEL
        font_path = os.path.join(base_path, "assets", "fonts", "FontPixel.ttf")

        #TIPOGRAFÍA DEL TÍTULO Y DEL BOTÓN
        self.font_title = pg.font.Font(font_path, 30)
        self.font_button = pg.font.Font(font_path, 20)
        
        #DEFINIR LA FORMA Y POSICIÓN DEL BOTÓN
        self.button_start = pg.Rect(0, 0, 200, 60)
        self.button_start.center = (width // 2, height // 2 + 40)

        #DEFINIR COLORES DEL BOTÓN
        self.button_color = GREEN #ESTADO NORMAL
        self.button_color_hover = LIGHT_GREEN #CUANDO SE PASA EL PUNTERO

    #FUNCIÓN PARA CAMBIAR DE ESTADO AL PRESIONAR EL BOTÓN
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.button_start.collidepoint(event.pos):
                self.change_state("level_selector")

    def update(self):
        pass

    def draw(self, screen):
        #DIBUJAR EL FONDO 
        screen.blit(self.background, (0, 0))

        #TÍTULO
        title_surface = self.font_title.render("WILLICHEDUNGUAY", True, (0, 0, 0))
        title_rect = title_surface.get_rect(center=(self.width // 2, self.height // 2 - 40))
        screen.blit(title_surface, title_rect) #screen.blit() es un método para una superficie encima de otra

        #BOTÓN
        mouse_pos = pg.mouse.get_pos()
        color = self.button_color_hover if self.button_start.collidepoint(mouse_pos) else self.button_color
        pg.draw.rect(screen, color, self.button_start, border_radius=12)

        #TEXTO DEL BOTÓN
        button_text = self.font_button.render("EMPEZAR", True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=self.button_start.center)
        screen.blit(button_text, button_text_rect)