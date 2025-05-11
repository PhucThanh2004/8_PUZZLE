import pygame
from core.config import WIDTH, GREEN, GRAY, BLACK

def draw_progress(step, total_steps, screen): # Thêm tham số screen
    bar_width = 400
    bar_height = 20
    x = WIDTH // 2 - bar_width // 2
    y = 530
    progress = step / total_steps
    pygame.draw.rect(screen, GRAY, (x, y, bar_width, bar_height), border_radius=10)
    pygame.draw.rect(screen, GREEN, (x, y, int(bar_width * progress), bar_height), border_radius=10)
    pygame.draw.rect(screen, BLACK, (x, y, bar_width, bar_height), 2, border_radius=10)

def draw_path(path, box_rect, screen): # Thêm tham số screen
    pygame.draw.rect(screen, GRAY, box_rect)
    pygame.draw.rect(screen, BLACK, box_rect, 2)
    font = pygame.font.Font(None, 24)
    y_offset = 10
    line_height = 25

    for idx, state in enumerate(path):
        text = font.render(f"Step {idx}:", True, BLACK)
        screen.blit(text, (box_rect.x + 10, box_rect.y + y_offset))
        y_offset += line_height

        for row in state:
            row_text = ' '.join(str(num) if num != 0 else ' ' for num in row)
            text = font.render(row_text, True, BLACK)
            screen.blit(text, (box_rect.x + 30, box_rect.y + y_offset))
            y_offset += line_height

        y_offset += line_height  # Khoảng cách giữa các bước
        if box_rect.y + y_offset > box_rect.y + box_rect.height - line_height * 3:
            break  # Ngăn ghi đè ra ngoài khung

def draw_time(elapsed_time, rect, screen): # Thêm tham số screen
    pygame.draw.rect(screen, GREEN, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    font = pygame.font.Font(None, 28)
    text = font.render(f"Time: {elapsed_time:.2f}s", True, BLACK)
    screen.blit(text, (rect.x + 10, rect.y + 10))