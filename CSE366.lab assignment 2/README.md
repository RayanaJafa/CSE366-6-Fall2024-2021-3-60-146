# Pathfinding Simulation with UCS and A* Algorithms

## Overview

This project is a grid-based simulation that demonstrates Uniform Cost Search (UCS) and A Search* algorithms. The simulation involves two agents navigating a grid to complete tasks while avoiding barriers. The user can observe and compare the behavior of both algorithms in real-time.

## Features
### Environment:

- A grid where agents move and interact with tasks and barriers.
- Random placement of tasks and barriers at the start of the simulation.
- Tasks are displayed with unique numbers on the grid.

### Agents:

- Two agents using UCS and A* Search respectively.
- Agents calculate and follow paths to the nearest task.
- Tracks completed tasks, positions, and total path costs.

### Graphical Interface:

- Displays the grid, barriers, tasks, and agent positions.
- Buttons to start the UCS and A* simulations.
- Live statistics for each agent, including tasks completed and path cost.

### Pathfinding Algorithms:

- UCS: Explores nodes uniformly based on path cost.
- A*: Uses a heuristic (Manhattan distance) for informed search.

## How to Run
### 1. Install Python and Pygame:

- Ensure Python 3.x is installed.
- Install Pygame using the command:

    pip install pygame

### 2. Run the Script:

- Save the code to a file named, for example,     
   pathfinding_simulation.py.
- Execute the script:

   python pathfinding_simulation.py
### 3. Interact with the Simulation:

- Press the UC Search or A Search* buttons to start the corresponding algorithm.
- Observe the agents navigate the grid to complete tasks.
## Controls and Interface
### Grid:

- Green cells with numbers: Task locations.
- Black cells: Barriers.
- White cells: Completed task locations.
### Agents:

- Blue squares represent agents.
- UCS and A* agents start from the top-left corner.
### Buttons:

- UC Search: Starts the UCS algorithm.
- A Search:* Starts the A* algorithm.
### Task Information:

- Displays live statistics:
  - Algorithm type.
  - Number of tasks completed.
  - Current position of the agent.
  - Completed tasks.
  - Total path cost.
## Code Structure
- Agent Class:

  - Handles movement, pathfinding, and task completion for agents.
  - Implements both UCS and A* Search.
- Environment Class:

  - Generates the grid with tasks and barriers.
  - Manages navigation logic and step costs.
- draw_* Functions:

  - Render the grid, tasks, agents, and interface components.
- Main Loop:

  - Processes user input, updates agent paths, and renders the simulation.
## Customization
- Modify Grid Size:

  - Adjust GRID_SIZE in the constants section.
- Change Task/Barrier Count:

  - Modify NUM_TASKS and NUM_BARRIERS.
- Alter Movement Delay:

  - Change MOVEMENT_DELAY for faster or slower agent updates.
## Dependencies
- Python 3.x
- Pygame library
## Notes
- Tasks and barriers are randomly generated at each run.
- Both algorithms operate independently and can be compared side-by-side.
- UCS prioritizes cost while A* combines cost and heuristic for efficiency