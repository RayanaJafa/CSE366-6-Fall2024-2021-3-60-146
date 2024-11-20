import pygame
import sys
from agent import Agent
from environment import Environment

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 15
NUM_TASKS = 6
NUM_BARRIERS = 30
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700
GRID_PIXEL_SIZE = 40

# Setup the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pathfinding Simulation')

# Create environment
environment = Environment(GRID_SIZE, NUM_TASKS, NUM_BARRIERS)

# Create two agents
agent_ucs = Agent(environment, GRID_PIXEL_SIZE)
agent_a_star = Agent(environment, GRID_PIXEL_SIZE)

# Distinguish agents by their colors
agent_ucs.image.fill((0,0,255))  # Blue for UCS agent
agent_a_star.image.fill((0, 0, 255))  # Blue for A* agent

# Set different starting positions for the agents
agent_ucs.position = [0, 0]
agent_ucs.rect.topleft = (0, 0)

agent_a_star.position = [0, 0]
agent_a_star.rect.topleft =  (0, 0)

# Buttons
button_ucs = pygame.Rect(WINDOW_WIDTH - 450, 500, 110, 40)
button_astar = pygame.Rect(WINDOW_WIDTH - 250, 500, 110, 40)

def draw_task_info():
    """Draw combined task information for both agents."""
    font = pygame.font.Font(None, 26)
    
  
    # UCS agent stats
    ucs_status = f"Algorithm: UCS"
    ucs_tasks_completed = f"Tasks Completed: {agent_ucs.task_completed}"
    ucs_position = f"Position: {agent_ucs.position}"
    ucs_completed_tasks = "Completed Tasks: " + ", ".join(
        [str(task) for task in agent_ucs.completed_tasks]
    )
    ucs_total_cost = f"Total Path Cost: {sum(agent_ucs.completed_tasks)}"

    # A* agent stats
    astar_status = f"Algorithm: A* Search"
    astar_tasks_completed = f"Tasks Completed: {agent_a_star.task_completed}"
    astar_position = f"Position: {agent_a_star.position}"
    astar_completed_tasks = "Completed Tasks: " + ", ".join(
        [str(task) for task in agent_a_star.completed_tasks]
    )
    astar_total_cost = f"Total Path Cost: {sum(agent_a_star.completed_tasks)}"

    # Combine the stats into a single section
    combined_stats = [
        ucs_status, ucs_tasks_completed, ucs_position, ucs_completed_tasks, ucs_total_cost, "",
        astar_status, astar_tasks_completed, astar_position, astar_completed_tasks, astar_total_cost
    ]

    # Display the stats
    for i, line in enumerate(combined_stats):
        color = (255, 0, 0) if "UCS" in line else ( 255,0,0) if "A*" in line else (0, 0, 0)
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (GRID_SIZE * GRID_PIXEL_SIZE + 20, 20 + i * 30))
  # Function to draw buttons
def draw_buttons():
    font = pygame.font.Font(None, 26)

    # UCS Button
    pygame.draw.rect(screen, (0,255,0), button_ucs)
    ucs_text = font.render(" UC Search", True, (255, 255, 255))
    screen.blit(ucs_text, (button_ucs.x + 10, button_ucs.y + 10))

    # A* Button
    pygame.draw.rect(screen, (0,255,0), button_astar)
    astar_text = font.render("A* Search", True, (255, 255, 255))
    screen.blit(astar_text, (button_astar.x + 10, button_astar.y + 10))

def draw_grid_with_numbers():
    """Draw the grid and tasks with numbers."""
    font = pygame.font.Font(None, 36)
    
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * GRID_PIXEL_SIZE, y * GRID_PIXEL_SIZE, GRID_PIXEL_SIZE, GRID_PIXEL_SIZE)
            if environment.grid[x][y] == 1:
                pygame.draw.rect(screen, (0, 0, 0), rect)  # Barriers are black
            elif environment.grid[x][y] == 2:
                pygame.draw.rect(screen, (0, 200, 0), rect)  # Tasks are green
                task_number = environment.task_locations.get((x, y), None)
                if task_number:
                    task_surface = font.render(str(task_number), True, (0, 0, 0))
                    screen.blit(task_surface, (x * GRID_PIXEL_SIZE + GRID_PIXEL_SIZE // 3, y * GRID_PIXEL_SIZE + GRID_PIXEL_SIZE // 3))
            elif environment.grid[x][y] == 0:
                pygame.draw.rect(screen, (255, 255, 255), rect)  # Completed tasks turn white
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Grid lines

def main():
    clock = pygame.time.Clock()
    simulation_started_ucs = False
    simulation_started_astar = False
    last_move_time = 0
    MOVEMENT_DELAY = 100 # 1 second between moves

    
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_ucs.collidepoint(mouse_pos):
                    simulation_started_ucs = True
                    print("UCS algorithm started")
                elif button_astar.collidepoint(mouse_pos):
                    simulation_started_astar = True
                    print("A* algorithm started")
        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw grid and tasks
        draw_grid_with_numbers()

        # Draw agents
        agent_ucs.draw(screen)
        agent_a_star.draw(screen)

        # Draw task information
        draw_task_info()
        draw_buttons()

        # Update UCS agent
        if simulation_started_ucs:
            current_time = pygame.time.get_ticks()
            if current_time - last_move_time > MOVEMENT_DELAY:
                if not agent_ucs.moving and environment.task_locations:
                    nearest_task_ucs = agent_ucs.find_nearest_task()
                    if nearest_task_ucs:
                        agent_ucs.path = agent_ucs.find_path_to(nearest_task_ucs, algorithm="UCS")
                        agent_ucs.moving = True
                elif agent_ucs.moving:
                    agent_ucs.move()
                last_move_time = current_time

        # Update A* agent
        if simulation_started_astar:
            current_time = pygame.time.get_ticks()
            if current_time - last_move_time > MOVEMENT_DELAY:
                if not agent_a_star.moving and environment.task_locations:
                    nearest_task_astar = agent_a_star.find_nearest_task()
                    if nearest_task_astar:
                        agent_a_star.path = agent_a_star.find_path_to(nearest_task_astar, algorithm="A*")
                        agent_a_star.moving = True
                elif agent_a_star.moving:
                    agent_a_star.move()
                last_move_time = current_time

        # Update the display
        pygame.display.flip()
        clock.tick(20)

if __name__ == "__main__":
    main()