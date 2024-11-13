from environment import Environment 
from agent import Agent
import pygame

pygame.init()

# Set up the environment
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
environment = Environment(WINDOW_WIDTH, WINDOW_HEIGHT)

# Create the agent position
agent = Agent(x=WINDOW_WIDTH // 10, y=WINDOW_HEIGHT // 10, speed=10, environment=environment)

# create  the Pygame window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Agent-Environment Simulation")

# Set up font for displaying coordinates
font = pygame.font.Font(None, 30)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        agent.move("up")
    if keys[pygame.K_DOWN]:
        agent.move("down")
    if keys[pygame.K_LEFT]:
        agent.move("left")
    if keys[pygame.K_RIGHT]:
        agent.move("right")

    # Fill the screen with a background color
    window.fill((255,255,255))

    # Draw the agent as a circle
    pygame.draw.rect(window, (0, 255, 255, 255), (agent.x, agent.y,30, 30))

    # Display the agent's position
    position_text = font.render(f"Position: ({agent.x}, {agent.y})", True, (0, 255, 0, 255))
    window.blit(position_text, (20, 20))
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(10)

# Quit Pygame
pygame.quit()

