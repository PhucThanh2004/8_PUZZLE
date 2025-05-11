# core/config.py
WIDTH, HEIGHT = 1000, 750
GRID_SIZE = 3
PUZZLE_SIZE = 300
CELL_SIZE = PUZZLE_SIZE // GRID_SIZE

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (173, 216, 230)
RED = (255, 0, 0)
GRAY = (220, 220, 220)
GREEN = (144, 238, 144)
BUTTON_COLOR = (100, 149, 237)
BUTTON_HOVER = (65, 105, 225)
TEXT_COLOR = (255, 255, 255)

FONT_SIZE = 40

# Kích thước lưới (sử dụng cho một số thuật toán cụ thể)
GRID_SIZE1 = 3

# Trạng thái ban đầu và đích
start_state = [[8, 6, 7], [2, 5, 4], [3, 0, 1]]  # mức độ xáo trộn rất cao
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

#start_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]  # solvable DFS