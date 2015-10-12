from core.Structures import String
from pygame.locals import *
from core import Globals
from core.Funcs import ind2cord

target_i = None

def load_menu(self):

    self.objects.append(String('new_game', 'Новая игра', (4, Globals.RENDER_NUM_Y // 2.5), (255, 255, 255)))
    self.draw_queue.append(self.objects[0])

    self.objects.append(String('continue', 'Продолжить', (4, Globals.RENDER_NUM_Y // 2.5 + 1), (255, 255, 255)))
    self.draw_queue.append(self.objects[1])

    self.objects.append(String('settings', 'Настройки', (4, Globals.RENDER_NUM_Y // 2.5 + 2), (255, 255, 255)))
    self.draw_queue.append(self.objects[2])

    self.objects.append(String('help', 'Помощь', (4, Globals.RENDER_NUM_Y // 2.5 + 3), (255, 255, 255)))
    self.draw_queue.append(self.objects[3])

    self.objects.append(String('quit', 'Выход', (4, Globals.RENDER_NUM_Y // 2.5 + 4), (255, 255, 255)))
    self.draw_queue.append(self.objects[4])


def menu_process(self, key):

    if not (key[0] & Globals.K_MENU or key[0] & Globals.E_RESIZE): return 'main_menu', False

    global target_i
    if key[0] & Globals.E_RESIZE:
        load_menu(self)
        if target_i is None: target_i = 0

        self.objects[target_i].make_patch(self)
        self.objects[target_i].color = (255, 0, 0)
        self.draw_queue.append(self.objects[target_i])


    if key[1] == K_w:
        self.objects[target_i].make_patch(self)
        self.objects[target_i].color = (255, 255, 255)
        self.draw_queue.append(self.objects[target_i])
        if target_i == 0:
            target_i = 4
        else:
            target_i -= 1

        self.objects[target_i].make_patch(self)
        self.objects[target_i].color = (255, 0, 0)
        self.draw_queue.append(self.objects[target_i])

    elif key[1] == K_s:
        self.objects[target_i].make_patch(self)
        self.objects[target_i].color = (255, 255, 255)
        self.draw_queue.append(self.objects[target_i])
        if target_i == 4:
            target_i = 0
        else:
            target_i += 1

        self.objects[target_i].make_patch(self)
        self.objects[target_i].color = (255, 0, 0)
        self.draw_queue.append(self.objects[target_i])

    elif key[1] == K_SPACE:
        if   target_i == 0:
            target_i = None
            return 'game', True

        elif target_i == 1: pass
        elif target_i == 2: pass
        elif target_i == 3: pass
        elif target_i == 4: pass

    return 'main_menu', False

def text_screen(game, text, color):
    r_text = Globals.FONT.render(text, True, color)
    game.screen.blit(r_text, ind2cord(Globals.RENDER_NUM_X // 4 + len(text) // 2, Globals.RENDER_NUM_Y // 2))
