def is_free(world, x, y):
    free = True
    for obj in world.objects[1:]:
        free &= x != obj.x or y != obj.y
    free &= x < world.map.width
    free &= x >= 0
    free &= y < world.map.height
    free &= y >= 0
    if free:
        free &= not world.map.map[x][y].blocked

    return free
