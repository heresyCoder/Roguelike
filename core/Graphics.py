from core import Funcs
from core import Globals

def get_color(name):
    colors = {
        'bg': (5, 26, 56),
        'player': (126, 167, 137),
        'npc': (175, 131, 159),
        'dark_wall': (76, 102, 140),
        'dark_ground': (45, 72, 111),
        'highlight': (70, 70, 70)
    }

    return colors[name]

textures = {}

def draw_Tile(Tile, game, x, y):

    cords = Funcs.ind2cord(x, y)
    if Tile.on_view:
        game.screen.blit(textures[Tile.type + '_l'], cords)
    else:
        game.screen.blit(textures[Tile.type], cords)

def draw_all(game):

    if game.link == 'main_menu':
        for obj in game.draw_queue:
            obj.draw(game)

    elif game.link == 'game':
        from core.Structures import Tile

        if game.draw_queue:
            if game.world.map.width  < game.render_map_x: game.render_map_x = game.world.map.width
            if game.world.map.height < game.render_map_y: game.render_map_y = game.world.map.height

            for i in range(game.render_map_x):
                for j in range(game.render_map_y):
                    map_obj = game.draw_queue[i * game.render_map_y + j]

                    if map_obj.on_view:
                        map_obj.draw(game, i, j)
                        map_obj.on_view = False
                    else:
                        if type(map_obj) is Tile:
                            if map_obj.explored:
                                map_obj.draw(game, i, j)
                        else:
                            if map_obj.stand_on.explored:
                                map_obj.stand_on.draw(game, i, j)

    game.draw_queue.clear()