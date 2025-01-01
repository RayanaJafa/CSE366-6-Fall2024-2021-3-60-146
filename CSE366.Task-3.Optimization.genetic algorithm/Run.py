import pygame
from Environment import Environment
from Agent import Student  # Ensure "agent" is correctly implemented and imported
import random

# Initialize Pygame
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Class Scheduling Visualization")
font = pygame.font.Font(None, 24)

# Environment setup
num_classes = 8
num_students = 5
num_time_slots = 8
environment = Environment(num_classes, num_students, num_time_slots)
population = environment.generate_initial_population()

# Initialize students
students = [Student(id=i, availability=environment.student_availability[i], preferences=environment.student_preferences[i])for i in range(num_students)
]

# Genetic Algorithm parameters
population_size = 50
mutation_rate = 0.1
n_generations = 100
generation_delay = 1000  # Delay in ms

# Updates list to display below the grid
updates = []
max_updates = 5
# Fitness function
def fitness(schedule):
    return environment.calculate_fitness(schedule)

# Selection, Crossover, and Mutation functions
def selection(population):
    return sorted(population, key=fitness)[:population_size // 2]

def crossover(parent1, parent2):
    """
    Perform single-point crossover for the schedules.
    """
    point = random.randint(1, len(parent1) - 1)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(schedule):
    """
    Perform random mutations in the schedule.
    """
    for class_info in schedule:
        if random.random() < mutation_rate:
            class_info["student"] = random.randint(0, num_students - 1)
            class_info["time_slot"] = random.randint(0, num_time_slots - 1)
    return schedule

# Run the Genetic Algorithm
best_schedule = None
best_fitness = float("inf")
generation_count = 0
max_fitness_achieved = float('inf')
while generation_count < n_generations:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Selection, crossover, and mutation
    selected = selection(population)
    next_generation = []
    while len(next_generation) < population_size:
        parent1, parent2 = random.sample(selected, 2)
        child = mutate(crossover(parent1, parent2))
        next_generation.append(child)

    # Evaluate the current generation
    population = next_generation
    current_best = min(population, key=fitness)
    current_fitness = fitness(current_best)

    if current_fitness < best_fitness:
        best_fitness = current_fitness
        best_schedule = current_best

    # Track max fitness achieved
    if current_fitness < max_fitness_achieved:
        max_fitness_achieved = current_fitness

    # Draw the best schedule
    environment.draw_schedule(screen, font, best_schedule)

    # Display generation and fitness info
    generation_text = font.render(f"Generation: {generation_count + 1}", True, (0, 0, 0))
    fitness_text = font.render(f"Best Fitness: {best_fitness:.2f}", True, (0, 0, 0))
    max_fitness_text = font.render(f"Max Fitness Achieved: {max_fitness_achieved:.2f}", True, (0, 0, 0))


    screen.blit(generation_text, (SCREEN_WIDTH - 250, 50))
    screen.blit(fitness_text, (SCREEN_WIDTH - 250, 80))
    screen.blit(max_fitness_text, (SCREEN_WIDTH - 250, 110))

# Add update for the current generation to the updates list
    update_text = f"Generation {generation_count + 1}: Best Fitness = {best_fitness:.2f}"
    updates.append(update_text)
    if len(updates) > max_updates:
        updates.pop(0)


    # Display the list of updates below the grid
    update_start_y = 650
    for i, update in enumerate(updates):
        update_surface = font.render(update, True, (0, 0, 0))
        screen.blit(update_surface, (50, update_start_y + i * 25))


    pygame.display.flip()
    pygame.time.delay(generation_delay)
    generation_count += 1
    if generation_count >= n_generations:
        break
# Keep the visualization window open after completion
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
