# Langton's Ant Simulation with Pheromone-Based Multi-Agent Behavior

An interactive Python simulation of an enhanced **Langton's Ant** cellular automaton featuring **two autonomous ants**, **pheromone-based memory**, and **probabilistic movement**. Built using **Pygame** and **NumPy**, this project demonstrates how simple local rules can produce complex emergent behavior.

---

## Overview

Langton's Ant is a two-dimensional Turing machine that moves on a grid by following simple deterministic rules. Despite these simple rules, the ant eventually exhibits highly complex and unpredictable behavior.

This project extends the classical Langton's Ant by introducing:

- Two independent ants
- Individual pheromone trails
- Self-pheromone recognition
- Cross-pheromone interference
- Pheromone decay over time
- Probabilistic movement decisions

The simulation provides an interesting demonstration of **cellular automata**, **agent-based modeling**, and **emergent systems**.

---

## Features

- Two independently moving Langton's Ants
- Real-time simulation using **Pygame**
- Randomized initial positions and directions
- Standard Langton's Ant movement rules
- Individual pheromone trails for each ant
- Self-pheromone recognition with probabilistic movement
- Cross-pheromone confusion between ants
- Automatic pheromone replacement
- Linear pheromone decay
- Grid visualization with color updates
- Object-Oriented implementation

---

## Simulation Rules

### Standard Movement

When an ant lands on a **white cell**:

- Turn left (counter-clockwise)
- Flip the cell to black
- Deposit its pheromone
- Move forward one step

When an ant lands on a **black cell**:

- Turn right (clockwise)
- Flip the cell to white
- Deposit its pheromone
- Move forward one step

---

### Pheromone Behavior

#### Self-Pheromone

If an ant encounters its own pheromone:

- Moves straight with high probability
- Otherwise follows the standard Langton's Ant rule

#### Cross-Pheromone

If an ant encounters the other ant's pheromone:

- Has a higher probability of following the standard turning rule
- Lower probability of moving straight

#### Pheromone Replacement

Whenever an ant deposits a pheromone on a cell, any existing pheromone at that location is replaced.

#### Pheromone Decay

Each pheromone has a limited lifetime.

Its influence decreases over time and is automatically removed after approximately five movement steps.

---

## Technologies Used

- Python 3
- NumPy
- Pygame

---

## Project Structure

```
.
├── langtons_ant.py
├── requirements.txt
└── README.md
```

*(Rename `langtons_ant.py` to match your actual filename.)*

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/langtons-ant.git
cd langtons-ant
```

Install the required libraries

```bash
pip install pygame numpy
```

or

```bash
pip install -r requirements.txt
```

---

## Running the Simulation

Run the Python file:

```bash
python langtons_ant.py
```

A Pygame window will open displaying the simulation.

---

## Implementation Details

The project is implemented using two primary classes:

### Ground

Responsible for:

- Maintaining the grid state
- Tracking pheromone locations
- Managing pheromone decay
- Removing expired pheromones

### Ant

Responsible for:

- Position and direction
- Standard Langton movement
- Turning logic
- Pheromone interactions
- Probabilistic movement
- Boundary checking

---

## Algorithm

For every simulation step:

1. Read the current grid cell.
2. Check for an existing pheromone.
3. If no pheromone exists:
   - Apply the standard Langton rule.
4. If the ant detects its own pheromone:
   - Move straight with high probability.
   - Otherwise apply the standard rule.
5. If the ant detects another ant's pheromone:
   - Follow modified probabilities.
6. Flip the current cell color.
7. Deposit a new pheromone.
8. Update pheromone timers.
9. Remove expired pheromones.
10. Render the updated grid.

---

## Concepts Demonstrated

- Cellular Automata
- Langton's Ant
- Emergent Behavior
- Multi-Agent Systems
- Swarm Intelligence
- Stochastic Decision Making
- Object-Oriented Programming
- Pygame Visualization

---

## Future Improvements

- Support for multiple ants
- Adjustable simulation speed
- Infinite scrolling grid
- Customizable pheromone decay functions
- Heatmap visualization of pheromone intensity
- Pause and resume controls
- Save and load simulation states
- Performance optimization for larger grids

---

## Sample Output

The simulation displays:

- A dynamically changing black-and-white grid
- Two ants represented by different colors
- Real-time movement across the grid
- Emergent patterns created through pheromone interactions
- Live movement counter

> Add screenshots or GIFs of the simulation here.

---

## License

This project was developed for educational purposes and to explore emergent behavior in cellular automata. Feel free to modify and extend the simulation.
