import pygame as pg
import os
from settings import BLACK, WHITE, BROWN, DARK_BROWN, GREEN, LIGHT_GREEN


class LevelSelector:
    def __init__(self, width, height, change_state):
        self.width = width
        self.height = height
        self.change_state = change_state

        #CARGAR FONDO
        base_path = os.path.dirname(os.path.dirname(__file__))  # sube desde /states/
        bg_path = os.path.join(base_path, "assets", "images", "background2.png")
        self.background = pg.image.load(bg_path).convert()
        self.background = pg.transform.scale(self.background, (width, height)) #AJUSTA LA IMAGEN AL TAMAÑO DE LA VENTANA

        #CARGAR LA TIPOGRAFÍA PIXEL
        font_path = os.path.join(base_path, "assets", "fonts", "FontPixel.ttf")

        #TIPOGRAFÍA DEL TÍTULO Y DE LOS BOTONES DE LOS NIVELES
        self.font_title = pg.font.Font(font_path, 30) #TÍTULO
        self.font_button = pg.font.Font(font_path, 15) #NIVELES

        
        '''-----BOTÓN PARA RETROCEDER-----'''

        #DEFINIR LA FORMA Y POSICIÓN DEL BOTÓN PARA RETROCEDER
        self.button_back = [(120, 130),(105, 140),(120, 150),(120, 145),(140, 145),(140, 135),(120, 135)]
        self.button_back_rect = pg.Rect(105, 125, 40, 30)

        #DEFINIR COLORES DEL BOTÓN PARA RETROCEDER
        self.button_back_color = GREEN #ESTADO NORMAL
        self.button_back_color_hover = LIGHT_GREEN #CUANDO SE PASA EL PUNTERO


        '''-----BOTÓN DE LOS NIVELES-----'''

        #DEFINIR LA FORMA Y POSICIÓN DEL BOTÓN PRINCIPIANTE
        self.button_beginner = pg.Rect(160, 250, 190, 65)  # (x, y, ancho, alto)

        #DEFINIR LA FORMA Y POSICIÓN DEL BOTÓN INTERMEDIO
        self.button_intermediate = pg.Rect(370, 250, 190, 65) # (x, y, ancho, alto)

        #DEFINIR LA FORMA Y POSICIÓN DEL BOTÓN AVANZADO
        self.button_advanced = pg.Rect(580, 250, 180, 65) # (x, y, ancho, alto)

        #DEFINIR COLORES DEL BOTÓN
        self.button_level_color = BROWN
        self.button_lever_color_hover = DARK_BROWN


    #FUNCIÓN PARA VOLVER AL MENÚ AL PRESIONAR EL BOTÓN DE RETROCEDER
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            #FUNCIÓN PARA RETROCEDER
            if self.button_back_rect.collidepoint(event.pos):
                self.change_state("menu")

            #FUNCIÓN PARA IR AL NIVEL PRINCIPIANTE
            if self.button_beginner.collidepoint(event.pos):
                print('Botón para el nivel principiante')

            #FUNCIÓN PARA IR AL NIVEL INTERMEDIO
            if self.button_intermediate.collidepoint(event.pos):
                print('Botón para el nivel intermedio')

            #FUNCIÓN PARA IR AL NIVEL AVANZADO
            if self.button_advanced.collidepoint(event.pos):
                print('Botón para el nivel avanzado')

    def update(self):
            pass

    def draw(self, screen):
        #DIBUJA EL FONDO 
        screen.blit(self.background, (0, 0))

        #TÍTULO
        title_surface = self.font_title.render("NIVEL", True, BLACK)
        title_rect = title_surface.get_rect(center=(self.width // 2, self.height // 2 - 40))
        screen.blit(title_surface, title_rect)

        #BOTÓN DE RETROCEDER
        mouse_pos = pg.mouse.get_pos()
        color_back = self.button_back_color_hover if self.button_back_rect.collidepoint(mouse_pos) else self.button_back_color
        pg.draw.polygon(screen, color_back, self.button_back)

        mouse_pos = pg.mouse.get_pos()
 
        #BOTÓN PARA SELECCIONAR NIVEL PRINCIPIANTE
        level_color_beginner = self.button_lever_color_hover if self.button_beginner.collidepoint(mouse_pos) else self.button_level_color
        pg.draw.ellipse(screen, level_color_beginner, self.button_beginner)

        #TEXTO DEL BOTÓN NIVEL PRINCIPIANTE
        button_text_beginner = self.font_button.render("PRINCIPIANTE", True, WHITE)
        button_text_beginner_rect = button_text_beginner.get_rect(center=self.button_beginner.center)
        screen.blit(button_text_beginner, button_text_beginner_rect)

        #BOTÓN PARA SELECCIONAR NIVEL INTERMEDIO
        level_color_intermediate = self.button_lever_color_hover if self.button_intermediate.collidepoint(mouse_pos) else self.button_level_color
        pg.draw.ellipse(screen, level_color_intermediate, self.button_intermediate)

        #TEXTO DEL BOTÓN NIVEL INTERMEDIO
        button_text_intermediate = self.font_button.render("INTERMEDIO", True, WHITE)
        button_text_intermediate_rect = button_text_intermediate.get_rect(center=self.button_intermediate.center)
        screen.blit(button_text_intermediate, button_text_intermediate_rect)

        #BOTÓN PARA SELECCIONAR NIVEL AVANZADO
        level_color_advanced = self.button_lever_color_hover if self.button_advanced.collidepoint(mouse_pos) else self.button_level_color
        pg.draw.ellipse(screen, level_color_advanced, self.button_advanced)

        #TEXTO DEL BOTÓN NIVEL AVANZADO
        button_text_advanced = self.font_button.render("AVANZADO", True, WHITE)
        button_text_advanced_rect = button_text_advanced.get_rect(center=self.button_advanced.center)
        screen.blit(button_text_advanced, button_text_advanced_rect)


        