# Langton's Ant Simulation with Pheromone-Based Multi-Agent Behavior

A Python implementation of an enhanced **Langton's Ant** cellular automaton featuring **multiple interacting ants**, **pheromone-based memory**, and **probabilistic decision-making**. The project extends the classic two-dimensional Turing Machine model by introducing self-recognition, cross-ant interference, and pheromone decay, resulting in rich emergent behaviors.

---

## Overview

Langton's Ant is a well-known deterministic cellular automaton where an ant moves across an infinite grid by following simple local rules. Despite the simplicity of these rules, the ant exhibits surprisingly complex global behavior.

This project expands the original model by introducing **two autonomous ants** that communicate indirectly through **pheromone trails**. Each ant remembers its own path, may become confused by another ant's trail, and adapts its movement based on probabilistic rules whose influence gradually fades over time.

The result is a dynamic simulation demonstrating how **simple local interactions**, **memory**, and **stochastic behavior** can generate complex collective patterns.

---

## Features

- Two independent Langton's Ant agents
- Dynamic black and white cellular grid
- Standard Langton's Ant movement rules
- Individual pheromone trails for each ant
- Self-pheromone recognition (memory effect)
- Cross-pheromone interference between ants
- Linear pheromone decay over time
- Automatic pheromone replacement
- Probabilistic movement decisions
- Real-time graphical visualization using Pygame
- Object-Oriented implementation for modularity and extensibility

---

## Simulation Rules

### Standard Movement

**At a White Cell**
- Turn 90° clockwise
- Flip the cell to black
- Deposit pheromone
- Move forward one cell

**At a Black Cell**
- Turn 90° counter-clockwise
- Flip the cell to white
- Deposit pheromone
- Move forward one cell

### Pheromone Behavior

#### Self-Pheromone
When an ant encounters **its own pheromone**:
- 80% probability of moving straight ahead
- 20% probability of applying the standard turning rule

#### Cross-Pheromone
When an ant encounters **the other ant's pheromone**:
- 20% probability of moving straight
- 80% probability of following the standard turning rule

#### Pheromone Replacement
- Only one pheromone may exist on a cell.
- Depositing a new pheromone removes any existing pheromone on that cell.

#### Pheromone Decay
- Pheromone influence decreases linearly over time.
- After approximately five movement steps, the pheromone completely loses its influence.

---

## Project Structure

```text
Langtons-Ant/
│
├── main.py               # Simulation entry point
├── ant.py                # Ant movement logic
├── grid.py               # Grid representation
├── pheromone.py          # Pheromone management
├── constants.py          # Simulation parameters
├── utils.py              # Helper functions
├── requirements.txt
└── README.md
```

> **Note:** Folder names may vary depending on your implementation.

---

## Technologies Used

- Python 3
- Pygame
- Object-Oriented Programming (OOP)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/langtons-ant.git
cd langtons-ant
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Simulation

```bash
python main.py
```

A simulation window will open where both ants move simultaneously while leaving pheromone trails and modifying the environment.

---

## Algorithm

For every simulation step:

1. Read the current cell color.
2. Check for an existing pheromone.
3. Compute movement probability based on:
   - Self pheromone
   - Cross pheromone
   - Pheromone age
4. Decide whether to move straight or apply the standard turning rule.
5. Flip the cell color.
6. Deposit a new pheromone.
7. Replace any existing pheromone.
8. Update pheromone decay.
9. Move to the next cell.
10. Render the updated grid.

---

## Emergent Behavior

Although each ant follows only simple local rules, the interaction between:

- Deterministic movement
- Probabilistic decisions
- Pheromone memory
- Pheromone decay
- Indirect communication

produces complex emergent patterns including:

- Chaotic exploration
- Recurring loops
- Trail formation
- Interference regions
- Cooperative and competitive movement

This simulation demonstrates how sophisticated global behavior can emerge from simple decentralized rules.

---

## Applications

This project demonstrates concepts used in:

- Cellular Automata
- Artificial Life (ALife)
- Swarm Intelligence
- Multi-Agent Systems
- Agent-Based Modeling
- Complex Adaptive Systems
- Stigmergy

---

## Future Improvements

- Configurable number of ants
- Adjustable pheromone decay functions
- Variable movement probabilities
- Heatmap visualization of pheromone intensity
- Performance optimization for larger grids
- Save and replay simulation states
- Interactive simulation controls
- Statistical analysis of ant trajectories

---

## Sample Output

The simulation visualizes:

- Dynamically changing black and white cells
- Independent ant movement
- Pheromone interactions
- Emergent patterns over time

> Add screenshots or GIFs here.

---

## License

This project is released for educational and research purposes. Feel free to modify and extend the simulation.
