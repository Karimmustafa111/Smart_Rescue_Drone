import pygame
import random
import sys

# 1. Basic Settings
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Smart Rescue Drone - Manual Play")

# Fonts and Colors
font_title = pygame.font.SysFont("Arial", 45, bold=True)
font_small = pygame.font.SysFont("Arial", 24, bold=True)
BLACK = (20, 20, 20)
GREEN = (50, 255, 50)
BLUE = (0, 200, 255)
RED = (255, 50, 50)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0) # Gold color for win message

# 2. Game variable
current_screen = "MENU" 
TILE = 40
COLS = 800 // TILE
ROWS = 600 // TILE

base_x, base_y = 10, 7
drone_x, drone_y = 10, 7
battery = 100
score = 0
fires = [(3, 3), (15, 2), (5, 12), (18, 10)]
WIN_SCORE = 20 

# Timer (Adjusted to not exceed 60)
TIME_LIMIT = 60 
time_left = TIME_LIMIT
TIMER_EVENT = pygame.USEREVENT + 1 
pygame.time.set_timer(TIMER_EVENT, 1000) 

clock = pygame.time.Clock()

# 3. Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # ==================================
        # Alarm (Triggers exactly every second)
        # ==================================
        if event.type == TIMER_EVENT:
            if current_screen == "PLAYING" and battery > 0 and score < WIN_SCORE and time_left > 0:
                time_left -= 1
                
        # keyboard controls
        if event.type == pygame.KEYDOWN:
            # Transition from menu to game or restart
            if event.key == pygame.K_SPACE and (current_screen == "MENU" or battery <= 0 or time_left <= 0 or score >= WIN_SCORE):
                current_screen = "PLAYING"
                time_left = TIME_LIMIT 
                battery = 100
                score = 0
                drone_x, drone_y = base_x, base_y
                fires = [(3, 3), (15, 2), (5, 12), (18, 10)] 
            
            # Drone movement
            elif current_screen == "PLAYING" and battery > 0 and time_left > 0 and score < WIN_SCORE:
                old_x, old_y = drone_x, drone_y
                
                if event.key == pygame.K_LEFT and drone_x > 0:
                    drone_x -= 1
                elif event.key == pygame.K_RIGHT and drone_x < COLS - 1:
                    drone_x += 1
                elif event.key == pygame.K_UP and drone_y > 0:
                    drone_y -= 1
                elif event.key == pygame.K_DOWN and drone_y < ROWS - 1:
                    drone_y += 1
                
                # Bettry consumption (decreases by 1 with each step outside the station)
                if (drone_x, drone_y) != (old_x, old_y): 
                    if (drone_x, drone_y) != (base_x, base_y):
                        battery -= 1

    screen.fill(BLACK)

    # ==========================================
    # Menu Screen (MENU UI)
    # ==========================================
    if current_screen == "MENU":
        title_text = font_title.render("Smart Rescue Drone Game", True, BLUE)
        screen.blit(title_text, (120, 200))
        
        start_text = font_small.render("Press SPACE to Start...", True, WHITE)
        screen.blit(start_text, (280, 300))

    # ==========================================
    # Playing Screen (PLAYING)
    # ==========================================
    elif current_screen == "PLAYING":

        # Environment interaction
        if battery > 0 and time_left > 0 and score < WIN_SCORE:
            # Fully charge battery when returning to station
            if (drone_x, drone_y) == (base_x, base_y):
                battery = 100

            # Extinguish fire
            if (drone_x, drone_y) in fires:
                fires.remove((drone_x, drone_y))
                score += 1
                # Timer increases by 3 seconds as a reward, but will never exceed 60
                time_left = min(TIME_LIMIT, time_left + 3)  

            # Rondom fire generation
            if random.random() < 0.05 and len(fires) < 10:
                new_fire = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
                if new_fire != (base_x, base_y) and new_fire not in fires:
                    fires.append(new_fire)

        # Actual Drawing
        pygame.draw.rect(screen, GREEN, (base_x * TILE, base_y * TILE, TILE, TILE))

        for fx, fy in fires:
            pygame.draw.circle(screen, RED, (fx * TILE + 20, fy * TILE + 20), 15)

        pygame.draw.rect(screen, BLUE, (drone_x * TILE + 5, drone_y * TILE + 5, 30, 30))

        text = font_small.render(f"Score: {score}/{WIN_SCORE}  |  Battery: {battery}%  |  Time: {time_left}s", True, WHITE)
        screen.blit(text, (10, 10))
        
        # Eng Game Message
        if score >= WIN_SCORE:
            win_text = font_title.render("YOU WIN! MISSION ACCOMPLISHED", True, GOLD)
            screen.blit(win_text, (40, 220))
            restart_text = font_small.render("Press SPACE to play again", True, WHITE)
            screen.blit(restart_text, (260, 280))
            
        elif battery <= 0 or time_left <= 0:
            msg = "GAME OVER! Battery Empty" if battery <= 0 else "TIME'S UP!"
            game_over_text = font_title.render(msg, True, RED)
            screen.blit(game_over_text, (120, 220))
            restart_text = font_small.render("Press SPACE to try again", True, WHITE)
            screen.blit(restart_text, (270, 280))

    pygame.display.flip()
    clock.tick(15)