import pygame
import random
import sys

# 1. Basic Settings
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Smart Rescue Drone - AI UI")

# Fonts and Colors
font_title = pygame.font.SysFont("Arial", 50, bold=True)
font_small = pygame.font.SysFont("Arial", 24, bold=True)
BLACK = (20, 20, 20)
GREEN = (50, 255, 50)
BLUE = (0, 200, 255)
RED = (255, 50, 50)
WHITE = (255, 255, 255)

# 2. Game Variables
current_screen = "MENU"
TILE = 40
base_x, base_y = 10, 7
drone_x, drone_y = 10, 7
battery = 100
score = 0
fires = [(3, 3), (15, 2), (5, 12), (18, 10)]

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

clock = pygame.time.Clock()

# 3. Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Transition from menu to game using SPACE key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and current_screen == "MENU":
                current_screen = "PLAYING"

    screen.fill(BLACK) # Clear The Screen

    # ==========================================
    # MENU UI
    # ==========================================
    if current_screen == "MENU":
        title_text = font_title.render("Smart Rescue Drone AI", True, BLUE)
        screen.blit(title_text, (150, 200))
        
        start_text = font_small.render("Press SPACE to Start...", True, WHITE)
        screen.blit(start_text, (280, 300))

    # ==========================================
    # Game Screen (PLAYING)
    # ==========================================
    elif current_screen == "PLAYING":
        
        # Agent Intelligence (AI Logic)
        target_x, target_y = base_x, base_y
        min_dist = 999

        for fx, fy in fires:
            dist_to_fire = get_distance(drone_x, drone_y, fx, fy)
            dist_fire_to_base = get_distance(fx, fy, base_x, base_y)

            if battery > (dist_to_fire + dist_fire_to_base):
                if dist_to_fire < min_dist:
                    min_dist = dist_to_fire
                    target_x, target_y = fx, fy

        # Movement
        if drone_x < target_x: drone_x += 1
        elif drone_x > target_x: drone_x -= 1
        elif drone_y < target_y: drone_y += 1
        elif drone_y > target_y: drone_y -= 1

        # Battery Consumption
        if (drone_x, drone_y) != (base_x, base_y):
            battery -= 1

        # Environment Interation
        if (drone_x, drone_y) == (base_x, base_y):
            battery = 100

        if (drone_x, drone_y) in fires:
            fires.remove((drone_x, drone_y))
            score += 1

        if random.random() < 0.05:
            new_fire = (random.randint(0, 19), random.randint(0, 14))
            if new_fire != (base_x, base_y) and new_fire not in fires:
                fires.append(new_fire)

        # Actual Game Rendering
        pygame.draw.rect(screen, GREEN, (base_x * TILE, base_y * TILE, TILE, TILE))

        for fx, fy in fires:
            pygame.draw.circle(screen, RED, (fx * TILE + 20, fy * TILE + 20), 15)

        pygame.draw.rect(screen, BLUE, (drone_x * TILE + 5, drone_y * TILE + 5, 30, 30))

        text = font_small.render(f"Score: {score} | Battery: {battery}%", True, WHITE)
        screen.blit(text, (10, 10))

    # Update display and control speed
    pygame.display.flip()
    clock.tick(10)