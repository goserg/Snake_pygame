window_size = 500
scale = 1
cell_size = 20

snake_color = (0, 0, 150)
grid_color = (50, 50, 50)
food_color = (0, 150, 0)
border_color = (100, 100, 100)


def switch_scale():
    global scale
    scale = 1.5 if scale == 1 else 1