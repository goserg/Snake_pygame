window_caption = "Snake v0.2"
window_size = 500
scale = 1
cell_size = 20
grid = True

font_size = 50
font = 'freesansbold.ttf'

gap = 2  # 1=1, 2=3, 3=5, 4=7...

# Colors
snake_color = (0, 0, 150)
grid_color = (50, 50, 50)
food_color = (0, 150, 0)
border_color = (100, 100, 100)
m_selected_color = (200, 200, 200)
m_shaded_color = (100, 100, 100)
# ============

main_loop_delay = 10
game_update_delay = 10


def switch_scale() -> None:
    global scale
    scale = 1.5 if scale == 1 else 1
