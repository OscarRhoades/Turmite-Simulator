import pygame
import turmites
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1600, 1600
GRID_SIZE = 20  # Adjust the grid size as needed
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

TURMITE = (102, 255, 0)
# Create the display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Grid")

# Create a 2D array to represent the grid
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

import pygame
import time

# values_and_coordinates = list(turmites.run_turmite(grid, 40, 40))

# Main game loop
running = True

turmite = turmites.run_turmite(grid, 40, 40, GRID_HEIGHT, GRID_WIDTH)
while running:
    screen.fill(WHITE)  # Fill the screen with white

    # Draw grid lines
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

    # Draw on the grid array based on values_and_coordinates list
    
    value, (yt, xt) = next(turmite)
    yt %= GRID_HEIGHT
    xt %= GRID_WIDTH
    grid[yt][xt] = value  # Update the grid with the value at the specified coordinates
     

    # pygame.draw.rect(screen, TURMITE, (xt * GRID_SIZE + 1, yt * GRID_SIZE + 1, GRID_SIZE - 2, GRID_SIZE - 2)) 
    # Draw the updated grid with boundaries
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(screen, BLACK, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
            if grid[y][x] == 1:
                pygame.draw.rect(screen, RED, (x * GRID_SIZE + 1, y * GRID_SIZE + 1, GRID_SIZE - 2, GRID_SIZE - 2))
            
    pygame.draw.rect(screen, TURMITE, (xt * GRID_SIZE + 1, yt * GRID_SIZE + 1, GRID_SIZE - 2, GRID_SIZE - 2)) 
                

    pygame.display.flip()  # Update the display
    time.sleep(0.005)  # Introduce a delay of 0.2 seconds to visualize the drawing

    # Event handling (same as before)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()