import pygame as pg
import os
import random
from settings import BLACK, WHITE, GREEN, LIGHT_GREEN, BROWN, DARK_BROWN

# --- CLASE PRINCIPAL ---
class BeginnerLevel1:
    def __init__(self, width, height, change_state, lives=3):
        self.width = width
        self.height = height
        self.change_state = change_state
        self.lives = lives
        self.game_over = False


        
        # 1. CARGA DE ASSETS Y TIPOGRAFÍA
        base_path = os.path.dirname(os.path.dirname(__file__))
        #CARGAR FONDO
        bg_path = os.path.join(base_path, "assets", "images", "background_beginner_levels.png")
        self.background = pg.image.load(bg_path).convert()
        self.background = pg.transform.scale(self.background, (width, height)) #AJUSTA LA IMAGEN AL TAMAÑO DE LA VENTANA
        #CARGAR TIPOGRAFÍA
        font_path = os.path.join(base_path, "assets", "fonts", "FontPixel.ttf")
        self.font_title = pg.font.Font(font_path, 25)
        self.font_title2 = pg.font.Font(font_path, 15)
        self.font_text = pg.font.Font(font_path, 20)
        self.font_button = pg.font.Font(font_path, 15)
       
        # 2. SISTEMA DE PREGUNTAS (EN ESPAÑOL Y SU TRADUCCIÓN WILLICHE)
        self.questions = [
            {"pregunta": "MADRE", "respuesta": "ÑUKE"},
            {"pregunta": "PADRE", "respuesta": "CHACHA"},
            {"pregunta": "HERMANO", "respuesta": "PEÑI"},
            {"pregunta": "HERMANA", "respuesta": "SEIYA"},
            # Agrega más preguntas aquí
        ]
        self.current_question_index = 0
        self.load_question()

        # 3. CONFIGURACIÓN DE DRAG AND DROP
        self.dragging = None # Almacena la opción que se está arrastrando
       
        # Área donde la opción debe ser soltada (será el centro del texto de la pregunta)
        self.drop_target_rect = pg.Rect(0, 0, 180, 50)
        self.drop_target_rect.center = (width // 2, 200)

        #DEFINIR LA FORMA Y POSICIÓN DEL BOTÓN PARA RETROCEDER
        self.button_back = [(120, 130),(105, 140),(120, 150),(120, 145),(140, 145),(140, 135),(120, 135)]
        self.button_back_rect = pg.Rect(105, 125, 40, 30)

        #DEFINIR COLORES DEL BOTÓN PARA RETROCEDER
        self.button_back_color = GREEN #ESTADO NORMAL
        self.button_back_color_hover = LIGHT_GREEN #CUANDO SE PASA EL PUNTERO

        #CARGAR SPRITE DEL CORAZON
        bg_path2 = os.path.join(base_path, "assets", "sprites", "corazon.png")
        self.candado = pg.image.load(bg_path2).convert_alpha()
        self.candado_pequeno = pg.transform.scale(self.candado, (65, 65))



    def load_question(self):
        """Carga la pregunta actual y mezcla las opciones."""
        if self.current_question_index >= len(self.questions):
            # Lógica para terminar el nivel o ir a la siguiente pantalla
            print("¡Nivel 1 completado!")
            self.change_state("beginner_selector")
            return
           
        current_data = self.questions[self.current_question_index]
        self.current_question = current_data["pregunta"]
        self.correct_answer = current_data["respuesta"]
       
        # Obtener 3 opciones incorrectas (o todas las incorrectas si no hay 3)
        all_answers = [q["respuesta"] for q in self.questions]
       
        incorrect_answers = [
            a for a in all_answers if a != self.correct_answer
        ]
        # Selecciona al azar 2 opciones incorrectas (para tener 3 en total)
        # Se asegura de no seleccionar más de las disponibles
        num_incorrect = min(2, len(incorrect_answers))
       
        # Mezcla la lista y toma las primeras 'num_incorrect'
        random.shuffle(incorrect_answers)
        selected_incorrect = incorrect_answers[:num_incorrect]
       
        # Opciones a mostrar: la correcta y las incorrectas seleccionadas
        options_texts = [self.correct_answer] + selected_incorrect
        random.shuffle(options_texts) # Mezcla el orden de presentación
       
        self.options = []
        # Crea los rectángulos para las opciones en la parte inferior de la pantalla
        option_width = 150
        option_height = 40
        start_x = (self.width - len(options_texts) * (option_width + 20) + 20) // 2
        y_pos = self.height - 80

        for i, text in enumerate(options_texts):
            rect = pg.Rect(start_x + i * (option_width + 20), y_pos, option_width, option_height)
            self.options.append({
                "text": text,
                "rect": rect,
                "original_rect": rect.copy(), # Para regresar a la posición original
                "is_dragging": False
            })

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
           
            # 1. Manejo del botón de retroceso
            if self.is_point_in_polygon(mouse_pos, self.button_back):
                self.change_state("beginner_selector")
                return

            # 2. Inicio del arrastre
            for option in self.options:
                if option["rect"].collidepoint(mouse_pos):
                    self.dragging = option
                    option["is_dragging"] = True
                    break

        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            if self.dragging:
                # 3. Fin del arrastre
                if self.drop_target_rect.colliderect(self.dragging["rect"]):
                    self.check_answer() # Verifica la respuesta
                else:
                    # Regresa a la posición original si no se soltó en el área
                    self.dragging["rect"] = self.dragging["original_rect"].copy()
               
                self.dragging["is_dragging"] = False
                self.dragging = None
               
        elif event.type == pg.MOUSEMOTION:
            if self.dragging:
                # 4. Mueve la opción arrastrada
                self.dragging["rect"].move_ip(event.rel)

    def is_point_in_polygon(self, point, polygon):
        """Verifica si un punto está dentro de un polígono (para el botón de retroceso)."""
        x, y = point
        n = len(polygon)
        inside = False
        p1x, p1y = polygon[0]
        for i in range(n + 1):
            p2x, p2y = polygon[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside
   
    def check_answer(self):
        """Verifica si la opción soltada es la correcta."""
        if self.dragging["text"] == self.correct_answer:
            print(f"¡Respuesta correcta! {self.current_question} = {self.correct_answer}")
            self.current_question_index += 1
            self.load_question() # Carga la siguiente pregunta
        else:
            self.lives -= 1
            print(f"Respuesta incorrecta. Vidas restantes: {self.lives}")
            # Vuelve a la posición original
            self.dragging["rect"] = self.dragging["original_rect"].copy()
            if self.lives <= 0:
                self.game_over = True
                print("Game Over")
                # Aquí podrías cambiar a una pantalla de Game Over
                # self.change_state("game_over")

    def update(self):
        pass

    def draw(self, screen):
        # 1. FONDO
        screen.blit(self.background, (0, 0))

        # 2. TÍTULO Y VIDAS
        title_principiante = self.font_title2.render("PRINCIPIANTE", True, BLACK)
        screen.blit(title_principiante, (self.width // 2 - title_principiante.get_width() // 2, 30))
       
        title_nivel1 = self.font_title.render("NIVEL 1", True, BLACK)
        screen.blit(title_nivel1, (self.width // 2 - title_nivel1.get_width() // 2, 50))

        title_tema = self.font_title2.render("FAMILIA/REÑMA", True, BLACK)
        screen.blit(title_tema, (self.width // 2 - title_tema.get_width() // 2, 80))

        lives_text = self.font_text.render(f"VIDAS: {'❤️' * max(0, self.lives)}", True, DARK_BROWN)
        screen.blit(lives_text, (self.width - lives_text.get_width() - 50, 50))

        #BOTÓN DE RETROCEDER
        mouse_pos = pg.mouse.get_pos()
        color_back = self.button_back_color_hover if self.button_back_rect.collidepoint(mouse_pos) else self.button_back_color
        pg.draw.polygon(screen, color_back, self.button_back)


        # 4. PREGUNTA (el concepto en español)
        question_surface = self.font_title.render(self.current_question, True, BLACK)
        question_rect = question_surface.get_rect(center=(self.width // 2, 140))
        screen.blit(question_surface, question_rect)

        # 5. ÁREA DE SOLTADO (Drop Target)
        # Dibuja un área visible donde debe soltar la respuesta
        drop_color = LIGHT_GREEN if self.drop_target_rect.collidepoint(pg.mouse.get_pos()) and self.dragging else GREEN
        pg.draw.rect(screen, drop_color, self.drop_target_rect, border_radius=10)
       
        # Texto auxiliar en el área de soltado
        target_text = self.font_text.render("Arrastra aquí", True, BLACK)
        target_rect = target_text.get_rect(center=self.drop_target_rect.center)
        screen.blit(target_text, target_rect)
       
        # 6. OPCIONES ARRASTRABLES
        # Dibuja las opciones que no se están arrastrando primero
        for option in [o for o in self.options if not o["is_dragging"]]:
            # Color base
            color = BROWN
           
            # Si el mouse está sobre la opción, cambia el color
            if option["rect"].collidepoint(pg.mouse.get_pos()):
                color = BROWN
               
            pg.draw.rect(screen, color, option["rect"], border_radius=10)
            option_surface = self.font_button.render(option["text"], True, WHITE)
            option_rect = option_surface.get_rect(center=option["rect"].center)
            screen.blit(option_surface, option_rect)

        # Dibuja la opción que se está arrastrando al final (para que esté encima de todo)
        if self.dragging:
            pg.draw.rect(screen, BROWN, self.dragging["rect"], border_radius=10)
            option_surface = self.font_button.render(self.dragging["text"], True, WHITE)
            option_rect = option_surface.get_rect(center=self.dragging["rect"].center)
            screen.blit(option_surface, option_rect)