# main.py
import pygame
import time
import sys
import imageio
import os  # Để quản lý file

from core.config import WIDTH, HEIGHT, start_state, goal_state, WHITE
from ui.drawer import draw_puzzle, draw_status, draw_background, draw_buttons
from ui.utils import draw_progress, draw_time
from algorithms import (
    bfs, dfs, uniform_cost, greedy, ids, a_star, ida_star,
    hill_climbing, simulated_annealing, beam_search, genetic_algorithm,
    uncertain_bfs, search_no_obs, po_dfs, backtracking
)

sys.setrecursionlimit(10000)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-Puzzle Solver")
clock = pygame.time.Clock()

def run_algorithm(algo_func, algo_name): # Thêm algo_name làm tham số
    screen.fill(WHITE)
    draw_background(screen)
    draw_puzzle(start_state, 100, 50, screen)
    draw_puzzle(goal_state, 600, 50, screen)
    pygame.display.flip()

    start_time = time.time()
    path = None
    if algo_name == "Backtracking":
        path = algo_func(start_state, screen, clock) # Truyền screen và clock
    else:
        path = algo_func(start_state)
    elapsed_time = time.time() - start_time

    image_frames = []
    output_gif_path = f"assets/{algo_name}.gif"
    frame_delay = 0.2 # Thời gian hiển thị mỗi frame trong GIF (giây)

    # Tạo thư mục assets nếu chưa tồn tại
    if not os.path.exists("assets"):
        os.makedirs("assets")

    if path:
        total_steps = len(path)
        for idx, state in enumerate(path):
            screen.fill(WHITE)
            draw_background(screen)
            draw_puzzle(start_state, 100, 50, screen)
            draw_puzzle(state, 600, 50, screen)
            draw_time(elapsed_time, pygame.Rect(720, 400, 180, 80), screen)
            draw_status(f"Step {idx + 1}/{total_steps}", 580, screen)
            draw_progress(idx + 1, total_steps, screen)
            pygame.display.flip()

            # Chuyển đổi bề mặt Pygame thành mảng numpy để lưu vào GIF
            pygame_bytes = pygame.surfarray.array3d(screen).transpose((1, 0, 2))
            image_frames.append(pygame_bytes)

            time.sleep(0.1) # Giảm thời gian sleep để tạo GIF nhanh hơn
            clock.tick(60)

        # Tạo ảnh GIF
        imageio.mimsave(output_gif_path, image_frames, duration=frame_delay)
        print(f"Đa luu anh GIF: {output_gif_path}")
        draw_status(f"Đa luu GIF: {algo_name}", 630, screen) # Thêm thông báo
        pygame.display.flip()
        time.sleep(2)
    else:
        screen.fill(WHITE)
        draw_background(screen)
        draw_puzzle(start_state, 100, 50, screen)
        draw_puzzle(goal_state, 600, 50, screen)
        draw_status("No solution found!", 580, screen)
        pygame.display.flip()
        time.sleep(2)

    # Đợi click quay lại
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                wait = False

# Giao diện chính
def main():
    buttons = [
        ("IDS", ids),
        ("Greedy", greedy),
        ("UC", uniform_cost),
        ("BFS", bfs),
        ("DFS", dfs),
        ("A_Star", a_star),
        ("IDA_Star", ida_star),
        ("Simple HC", hill_climbing.simple_hill_climbing),
        ("Steepest HC", hill_climbing.steepest_ascent_hill_climbing),
        ("Stochastic HC", hill_climbing.stochastic_hill_climbing),
        ("SA", simulated_annealing),
        ("Beam Search", lambda s: beam_search(s, k=5)), # Cần xử lý state
        ("GA", genetic_algorithm),
        ("BFS Uncertain", uncertain_bfs),
        ("No Observations", search_no_obs.search_with_no_observations),
        ("PO", po_dfs.partially_observable_dfs),
        ("Backtracking", backtracking.backtracking_search)
    ]

    button_rects = []
    total_buttons = len(buttons)
    buttons_per_row = 5
    button_width = 150
    button_height = 45
    spacing_x = 20
    spacing_y = 20

    total_buttons = len(buttons)
    total_row_width = buttons_per_row * button_width + (buttons_per_row - 1) * spacing_x
    start_x = WIDTH // 2 - total_row_width // 2
    start_y = 500

    button_rects = []
    for idx in range(total_buttons):
        row = idx // buttons_per_row
        col = idx % buttons_per_row
        x = start_x + col * (button_width + spacing_x)
        y = start_y + row * (button_height + spacing_y)
        button_rects.append(pygame.Rect(x, y, button_width, button_height))

    running = True
    while running:
        screen.fill(WHITE)
        draw_background(screen)
        draw_puzzle(start_state, 100, 50, screen)
        draw_puzzle(goal_state, 600, 50, screen)
        draw_status("Select Algorithm", 400, screen)

        mouse_pos = pygame.mouse.get_pos()
        draw_buttons(buttons, button_rects, mouse_pos, screen)

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for idx, rect in enumerate(button_rects):
                    if rect.collidepoint(event.pos):
                        algo_name, algo_func = buttons[idx]
                        run_algorithm(algo_func, algo_name) # Truyền algo_name
    pygame.quit()

if __name__ == "__main__":
    main()


