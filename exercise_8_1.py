def flood_array(some_file):
    with open(some_file, "r") as flood_file:
        flood_list = []
        for line in flood_file:
            file_list = []
            for char in line[:-1]:
                file_list.append(char)
            flood_list.append(file_list)

    return flood_list


def flood_fill(x, y, old_color, new_color, surface=flood_array("flood.txt")):

    surface_width = len(surface[0])
    surface_height = len(surface)

    if surface[x][y] != old_color:
        return

    surface[x][y] = new_color

    if x > 0: # go up
        flood_fill(x - 1, y, old_color, new_color, surface)
    if y > 0: #left
        flood_fill(x, y - 1, old_color, new_color, surface)
    if x < surface_height - 1: #down
        flood_fill(x + 1, y, old_color, new_color, surface)
    if y < surface_width - 1: #right
        flood_fill(x, y + 1, old_color, new_color, surface)

    return surface


print(flood_fill(5, 1, '.', 's'))