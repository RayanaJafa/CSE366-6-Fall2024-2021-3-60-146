# **Class Scheduling Visualization with Genetic Algorithm**
## **Objective**
### This project employs a Genetic Algorithm (GA) to optimize the scheduling of classes for multiple students, taking into account their availability and preferences. The goal is to:

- Minimize Scheduling Conflicts: Assign classes to students based on their availability.

- Maximize Preference Alignment: Ensure that class schedules align closely with student preferences.

- Visualize Assignments: Provide a clear and interactive visualization of the scheduling process using Pygame.
## **Features**

### **Dynamic Scheduling Environment**
- Class Details:

   - Randomly generated durations (1-2 hours) and priorities (scale of 1-5).

- Student Details:

  - Random availability for each time slot.

  - Random preference scores (scale of 1-5) for each time slot.
### **Genetic Algorithm Optimization**

 - **Population Initialization:**

   - Randomly assigns classes to students and time slots.

- **Fitness Calculation:**

   - Penalizes conflicts where classes are assigned to unavailable students.

   - Considers misalignment with student preferences.

- **Selection, Crossover, and Mutation:**

  - Implements mechanisms to evolve the population towards better schedules.
### **Visualization**

 - Grid Representation:

    - Rows represent students.

    - Columns represent time slots.

    - Cells display class priorities and highlight conflicts.

- Dynamic Updates:

   - Displays generation count, best fitness score, and recent updates during the GA execution.

## **Assignment Details**

### **Background**

- Classes: Each class has a fixed duration and priority level.

- Students: Each student has specific availability and preferences for time slots.

- Environment: Simulates a realistic scheduling scenario where constraints and priorities must be balanced.

### **Tasks**

#### Data Preparation

- Generate random data for classes and students.
### GA Implementation

#### Genetic Algorithm Parameters

- Population Size: 50 schedules per generation.

- Number of Generations: 100 iterations to evolve solutions.

- Mutation Rate: 10% chance of random mutation for each gene.

#### Core Functions

- Fitness Function:
Evaluates each schedule based on conflicts and preference misalignment.

- Selection: Retains the top half of the population based on fitness.
- Crossover: Combines parent schedules to create offspring.
- Mutation: Introduces random changes to maintain diversity.
### Visualization

#### Grid Design

- Cells:

  - Default color indicates empty slots.

  - Highlighted cells show assigned classes with priority information.

- Student Info:

  - Displays availability and assigned classes.

- Dynamic Updates:

   - Shows generation count, best fitness score, and recent updates below the grid.

#### Pygame Implementation

- Grid Drawing


- Real-Time Updates:

   - Generation progress and fitness scores are displayed on the screen.

### **Customization**

- Number of Classes: Modify num_classes in the script.

- Number of Students: Adjust num_students as needed.

- Genetic Algorithm Parameters:

  - population_size, mutation_rate, and n_generations can be tuned for optimization.

## Conclusion

This project demonstrates the application of a Genetic Algorithm to solve a complex scheduling problem, with real-time visualization providing insight into the optimization process. The framework can be extended for various scheduling scenarios, such as workforce planning or resource allocation.

