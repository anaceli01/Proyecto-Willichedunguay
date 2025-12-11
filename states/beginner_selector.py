import pygame as pg
import os
from settings import BLACK, WHITE, BROWN, LIGHT_BROWN, GREEN, LIGHT_GREEN


class BeginnerSelector:
    def __init__(self, width, height, change_state):
        self.width = width
        self.height = height
        self.change_state = change_state

        #CARGAR FONDO
        base_path = os.path.dirname(os.path.dirname(__file__))  # sube desde /states/
        bg_path1 = os.path.join(base_path, "assets", "images", "background_beginner.png")
        self.background = pg.image.load(bg_path1).convert()
        self.background = pg.transform.scale(self.background, (width, height)) #AJUSTA LA IMAGEN AL TAMAÑO DE LA VENTANA

        #CARGAR SPRITE DEL CANDADO
        bg_path2 = os.path.join(base_path, "assets", "sprites", "candado.png")
        self.candado = pg.image.load(bg_path2).convert_alpha()
        self.candado_pequeno = pg.transform.scale(self.candado, (65, 65))


        #CARGAR LA TIPOGRAFÍA PIXEL
        font_path = os.path.join(base_path, "assets", "fonts", "FontPixel.ttf")

        #TIPOGRAFÍA DEL TÍTULO Y DE LOS BOTONES DE LOS NIVELES
        self.font_title = pg.font.Font(font_path, 20) #TÍTULO
        self.font_button = pg.font.Font(font_path, 15) #NIVELES

        
        '''-----BOTÓN PARA RETROCEDER-----'''

        #DEFINIR LA FORMA Y POSICIÓN DEL BOTÓN PARA RETROCEDER
        self.button_back = [(120, 130),(105, 140),(120, 150),(120, 145),(140, 145),(140, 135),(120, 135)]
        self.button_back_rect = pg.Rect(105, 125, 40, 30)

        #DEFINIR COLORES DEL BOTÓN PARA RETROCEDER
        self.button_back_color = GREEN #ESTADO NORMAL
        self.button_back_color_hover = LIGHT_GREEN #CUANDO SE PASA EL PUNTERO


        '''-----BOTÓN DE LOS NIVELES-----'''

        #DEFINIR LA FORMA Y POSICIÓN DEL BOTÓN NIVEL 1
        self.button_beginner = pg.Rect(170, 160, 75, 75)  # (x, y, ancho, alto)

        #DEFINIR LA FORMA Y POSICIÓN DEL BOTÓN NIVEL 2
        self.button_intermediate = pg.Rect(400, 270, 75, 75) # (x, y, ancho, alto)

        #DEFINIR LA FORMA Y POSICIÓN DEL BOTÓN NIVEL 3
        self.button_advanced = pg.Rect(630, 160, 75, 75) # (x, y, ancho, alto)

        #DEFINIR COLORES DEL BOTÓN
        self.button_level_color = LIGHT_BROWN
        self.button_level_color_hover = BROWN


    #FUNCIÓN PARA VOLVER AL MENÚ AL PRESIONAR EL BOTÓN DE RETROCEDER
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            #FUNCIÓN PARA RETROCEDER
            if self.button_back_rect.collidepoint(event.pos):
                self.change_state("level_selector")

            #FUNCIÓN PARA IR AL NIVEL PRINCIPIANTE
            if self.button_beginner.collidepoint(event.pos):
                self.change_state("beginner_level_1")

            #FUNCIÓN PARA IR AL NIVEL INTERMEDIO
            if self.button_intermediate.collidepoint(event.pos):
                print('Botón para el nivel 2')

            #FUNCIÓN PARA IR AL NIVEL AVANZADO
            if self.button_advanced.collidepoint(event.pos):
                print('Botón para el nivel 3')

    def update(self):
            pass

    def draw(self, screen):
        #DIBUJA EL FONDO 
        screen.blit(self.background, (0, 0))

        #TÍTULO
        title_surface = self.font_title.render("PRINCIPIANTE", True, BLACK)
        title_rect = title_surface.get_rect(center=(self.width // 2, self.height // 2 - 130))
        screen.blit(title_surface, title_rect)

        #BOTÓN DE RETROCEDER
        mouse_pos = pg.mouse.get_pos()
        color_back = self.button_back_color_hover if self.button_back_rect.collidepoint(mouse_pos) else self.button_back_color
        pg.draw.polygon(screen, color_back, self.button_back)

        mouse_pos = pg.mouse.get_pos()
 
        #BOTÓN PARA SELECCIONAR NIVEL 1
        level_color_beginner = self.button_level_color_hover if self.button_beginner.collidepoint(mouse_pos) else self.button_level_color
        pg.draw.rect(screen, level_color_beginner, self.button_beginner, border_radius=12)

        #TEXTO DEL BOTÓN NIVEL 1
        button_text_beginner1 = self.font_button.render("NIVEL", True, BLACK)
        button_text_beginner2 = self.font_button.render("1", True, BLACK)
        button_text_beginner_rect1 = button_text_beginner1.get_rect(center=(self.button_beginner.centerx, self.button_beginner.centery -10))
        button_text_beginner_rect2 = button_text_beginner2.get_rect(center=(self.button_beginner.centerx, self.button_beginner.centery +15))
        screen.blit(button_text_beginner1, button_text_beginner_rect1)
        screen.blit(button_text_beginner2, button_text_beginner_rect2)

        #BOTÓN PARA SELECCIONAR NIVEL 2
        level_color_intermediate = self.button_level_color_hover if self.button_intermediate.collidepoint(mouse_pos) else self.button_level_color
        pg.draw.rect(screen, level_color_intermediate, self.button_intermediate, border_radius=12)

        #CANDADO DEL BOTÓN NIVEL 2
        candado2_rect = self.candado_pequeno.get_rect(center=self.button_intermediate.center)
        screen.blit(self.candado_pequeno, candado2_rect)

        #BOTÓN PARA SELECCIONAR NIVEL 3
        level_color_advanced = self.button_level_color_hover if self.button_advanced.collidepoint(mouse_pos) else self.button_level_color
        pg.draw.rect(screen, level_color_advanced, self.button_advanced, border_radius=12)

        #CANDADO DEL BOTÓN NIVEL 2
        candado3_rect = self.candado_pequeno.get_rect(center=self.button_advanced.center)
        screen.blit(self.candado_pequeno, candado3_rect)

        