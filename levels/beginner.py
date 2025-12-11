import pygame as pg
import os
from settings import BLACK, WHITE, BROWN, LIGHT_BROWN, GREEN, LIGHT_GREEN


class Beginner:
    def __init__(self, width, height, change_state):
        self.width = width
        self.height = height
        self.change_state = change_state

        #CARGAR FONDO
        base_path = os.path.dirname(os.path.dirname(__file__))  # sube desde /states/
        bg_path = os.path.join(base_path, "assets", "images", "background_beginner2.png")
        self.background = pg.image.load(bg_path).convert()
        self.background = pg.transform.scale(self.background, (width, height)) #AJUSTA LA IMAGEN AL TAMAÑO DE LA VENTANA

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

        

