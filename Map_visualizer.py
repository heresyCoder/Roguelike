import pygame
import sys
import Config
import random
from pygame.locals import *


class Visual:

    def __init__(self):
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), pygame.RESIZABLE)
        self.render_x = Config.SCREEN_WIDTH   // Config.SQUARE_SIZE
        self.render_y = Config.SCREEN_HEIGHT  // Config.SQUARE_SIZE
        self.event_flag = True
        self.world = None
        self.draw_queue = []

    def run_game(self):
        mainloop = True
        on_load  = True

        while mainloop:
            pygame.time.wait(Config.TIME_DELAY)

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


def event_handler(Vis, events):

    for event in events:
        if event.type == pygame.KEYDOWN:
            if   event.key == K_MINUS:

                Config.SQUARE_SIZE -= 1
                return True

            elif   event.key == K_EQUALS:

                Config.SQUARE_SIZE += 1
                return True

            elif event.key == K_ESCAPE:

                pygame.quit()
                sys.exit(0)

        elif event.type == VIDEORESIZE:

            Vis.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), pygame.RESIZABLE)

    return False