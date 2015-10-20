import pygame
import sys
from core import Funcs
from core import Graphics
from core import World
from core import Main_menu
from core import Game as g
from core import Globals

class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT), pygame.RESIZABLE)
        self.render_x = self.screen.get_width()   // Globals.FONT_X
        self.render_y = self.screen.get_height()  // Globals.FONT_Y
        self.world = None
        self.scenes = {'main_menu': Main_menu.menu_process, 'game': g.game_process}
        self.link = 'main_menu'
        self.objects = []
        self.draw_queue = []

    def run_game(self):
        mainloop = True
        on_load  = True

        while mainloop:
            pygame.time.wait(Globals.WAIT_TIME)
            flags_n_key = Funcs.event_handler(pygame.event.get())

            if not flags_n_key[0] & Globals.K_NONE or on_load:

                if flags_n_key[0] & Globals.K_QUIT:
                    World.save_world(self.world)
                    pygame.quit()
                    sys.exit(0)

                if flags_n_key[0] & Globals.E_RESIZE:

                    self.screen = pygame.display.set_mode(flags_n_key[1], pygame.RESIZABLE)
                    self.render_x = self.screen.get_width()   // Globals.FONT_X
                    self.render_y = self.screen.get_height()  // Globals.FONT_Y
                    self.screen.fill(Globals.BG_COLOR)

                if on_load:
                    self.objects.clear()
                    self.draw_queue.clear()
                    self.screen.fill(Globals.BG_COLOR)

                    if   self.link == 'main_menu':
                        #Main_menu.load_menu(self)
                        pass

                    if self.link == 'continue':
                        self.link = 'game'
                        self.world = World.load_world()
                        g.load_game(self)

                    elif self.link == 'game':
                        Main_menu.text_screen(self, 'generating...', (255, 255, 255))
                        pygame.display.flip()
                        self.world = World.World(Globals.FIELD_NUM_X, Globals.FIELD_NUM_Y)
                        g.load_game(self)
                    on_load = False

                self.link, on_load = self.scenes[self.link](self, flags_n_key)
                Graphics.draw_all(self)
                pygame.display.flip()
