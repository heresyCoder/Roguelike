from core.Structures import String
from pygame.locals import *
from core import Globals

target_i = None

def load_menu(self):

    self.objects.clear()
    self.draw_queue.clear()

    self.objects.append(String('new_game'))
    self.objects[0].set_text('Новая игра')
    self.objects[0].x = 4                   #Globals.RENDER_NUM_X // 4
    self.objects[0].y = Globals.RENDER_NUM_Y // 2.5
    self.draw_queue.append(self.objects[0])

    self.objects.append(String('continue'))
    self.objects[1].set_text('Продолжить')
    self.objects[1].x = 4
    self.objects[1].y = Globals.RENDER_NUM_Y // 2.5 + 1
    self.draw_queue.append(self.objects[1])

    self.objects.append(String('settings'))
    self.objects[2].set_text('Настройки')
    self.objects[2].x = 4
    self.objects[2].y = Globals.RENDER_NUM_Y // 2.5 + 2
    self.draw_queue.append(self.objects[2])

    self.objects.append(String('help'))
    self.objects[3].set_text('Помощь')
    self.objects[3].x = 4
    self.objects[3].y = Globals.RENDER_NUM_Y // 2.5 + 3
    self.draw_queue.append(self.objects[3])

    self.objects.append(String('quit'))
    self.objects[4].set_text('Выход')
    self.objects[4].x = 4
    self.objects[4].y = Globals.RENDER_NUM_Y // 2.5 + 4
    self.draw_queue.append(self.objects[4])


def menu_process(self, key):

    if not (key[0] & Globals.K_MENU or key[0] & Globals.E_RESIZE): return 'main_menu', False

    global target_i
    if key[0] & Globals.E_RESIZE:
        load_menu(self)
        if target_i is None: target_i = 0

        self.objects[target_i].set_color((255, 0, 0))
        self.draw_queue.append(self.objects[target_i])


    if key[1] == K_w:
        self.objects[target_i].set_color((255, 255, 255))
        self.draw_queue.append(self.objects[target_i])
        if target_i == 0:
            target_i = 4
        else:
            target_i -= 1

        self.objects[target_i].set_color((255, 0, 0))
        self.draw_queue.append(self.objects[target_i])

    elif key[1] == K_s:
        self.objects[target_i].set_color((255, 255, 255))
        self.draw_queue.append(self.objects[target_i])
        if target_i == 4:
            target_i = 0
        else:
            target_i += 1

        self.objects[target_i].set_color((255, 0, 0))
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