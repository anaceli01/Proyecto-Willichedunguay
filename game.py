import pygame as pg
from settings import WIDTH, HEIGHT
from states.menu import Menu
from states.level_selector import LevelSelector
from states.beginner_selector import BeginnerSelector
# AÑADIR LA NUEVA IMPORTACIÓN
from states.beginner_level_1 import BeginnerLevel1

class Game():
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption("Kimün")
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        pg.mixer.music.load('assets/sounds/musica.mp3')
        pg.mixer.music.play(-1)
        
        self.current_state = None

    # Esta función será enviada a los estados
    def change_state(self, to):
        if to == "menu":
            self.current_state = Menu(WIDTH, HEIGHT, self.change_state)
        elif to == "level_selector":
            self.current_state = LevelSelector(WIDTH, HEIGHT, self.change_state)
        elif to == 'beginner_selector':
            self.current_state = BeginnerSelector(WIDTH, HEIGHT, self.change_state)
        # AÑADIR LA LÓGICA PARA EL NUEVO NIVEL
        elif to == 'beginner_level_1':
            self.current_state = BeginnerLevel1(WIDTH, HEIGHT, self.change_state)
        # ... otros niveles irán aquí ...


    def run(self):
        # INICIALIZA EL PRIMER ESTADO EN MENÚ
        self.change_state("menu")
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                self.current_state.handle_event(event)

            self.current_state.update()
            self.current_state.draw(self.screen)

            pg.display.flip()
            self.clock.tick(60)

        pg.quit()