from core.Structures import String
from pygame.locals import *
from core import Globals

target_i = None

def load_menu(game):

    game.objects.append(String('new_game', 'Новая игра', (4, game.render_map_y // 2.5), (255, 255, 255)))
    game.draw_queue.append(game.objects[0])

    game.objects.append(String('continue', 'Продолжить', (4, game.render_map_y // 2.5 + 1), (255, 255, 255)))
    game.draw_queue.append(game.objects[1])

    game.objects.append(String('settings', 'Настройки', (4, game.render_map_y // 2.5 + 2), (255, 255, 255)))
    game.draw_queue.append(game.objects[2])

    game.objects.append(String('help', 'Помощь', (4, game.render_map_y // 2.5 + 3), (255, 255, 255)))
    game.draw_queue.append(game.objects[3])

    game.objects.append(String('quit', 'Выход', (4, game.render_map_y // 2.5 + 4), (255, 255, 255)))
    game.draw_queue.append(game.objects[4])


def menu_process(game, key):

    if not (key[0] & Globals.K_MENU or key[0] & Globals.E_RESIZE): return 'main_menu', False

    global target_i
    if key[0] & Globals.E_RESIZE:
        game.objects.clear()
        load_menu(game)
        if target_i is None: target_i = 0

        game.objects[target_i].make_patch(game)
        game.objects[target_i].color = (255, 0, 0)
        game.draw_queue.append(game.objects[target_i])


    if key[1] == K_w:
        game.objects[target_i].make_patch(game)
        game.objects[target_i].color = (255, 255, 255)
        game.draw_queue.append(game.objects[target_i])
        if target_i == 0:
            target_i = 4
        else:
            target_i -= 1

        game.objects[target_i].make_patch(game)
        game.objects[target_i].color = (255, 0, 0)
        game.draw_queue.append(game.objects[target_i])

    elif key[1] == K_s:
        game.objects[target_i].make_patch(game)
        game.objects[target_i].color = (255, 255, 255)
        game.draw_queue.append(game.objects[target_i])
        if target_i == 4:
            target_i = 0
        else:
            target_i += 1

        game.objects[target_i].make_patch(game)
        game.objects[target_i].color = (255, 0, 0)
        game.draw_queue.append(game.objects[target_i])

    elif key[1] == K_SPACE:
        if   target_i == 0:
            target_i = None
            return 'game', True

        elif target_i == 1:
            target_i = None
            return 'continue', True

        elif target_i == 2: pass
        elif target_i == 3: pass
        elif target_i == 4: pass

    return 'main_menu', False

def text_screen(game, text, color):
    txt = String('', text, (game.render_map_x // 4 + len(text) // 2, game.render_map_y // 2), color)
    txt.draw(game)