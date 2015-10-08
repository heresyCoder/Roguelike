import pygame
from core import Funcs
from core import Graphics
from core import World
from core import Main_menu
from core import Game as g
from core import Globals

class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT), pygame.RESIZABLE)
        self.world = World.World(Globals.FIELD_NUM_X, Globals.FIELD_NUM_Y)
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
                if on_load:
                    self.screen.fill(Graphics.bg_color)
                    if   self.link == 'main_menu':
                        Main_menu.load_menu(self)
                    elif self.link == 'game':
                        g.load_game(self)
                    on_load = False

                if flags_n_key[0] & Globals.E_RESIZE:
                    self.screen = pygame.display.set_mode((Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT), pygame.RESIZABLE)
                self.link, on_load = self.scenes[self.link](self, flags_n_key)
                Graphics.draw_all(self)
                pygame.display.flip()
