import pygame
import sys

# Initialize Pygame
pygame.init()

# Setup screen to match any device display dimension
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w if info.current_w > 0 else 800
SCREEN_HEIGHT = info.current_h if info.current_h > 0 else 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Flawless Ninja")
clock = pygame.time.Clock()

# Ninja properties
player_w, player_h = 50, 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 150
player_speed = 7

# On-screen control areas (Left half of screen moves left, Right half moves right)
# This removes the need for physical keyboards on a mobile device!
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Checking for finger touches
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN:
            # Simple touch position detection
            touch_x = pygame.mouse.get_pos()[0] if event.type == pygame.MOUSEBUTTONDOWN else event.x * SCREEN_WIDTH
            if touch_x < SCREEN_WIDTH / 2:
                player_x -= player_speed * 4
            else:
                player_x += player_speed * 4

    # Keep player on screen boundary
    player_x = max(0, min(SCREEN_WIDTH - player_w, player_x))

    # Render graphics
    screen.fill((20, 24, 30))  # Slate background
    pygame.draw.rect(screen, (0, 150, 255), (player_x, player_y, player_w, player_h))  # Blue Ninja Box
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
