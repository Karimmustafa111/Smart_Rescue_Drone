# Smart Rescue Drone Simulator

## 📌 Project Description
This project is a 2D interactive simulator developed using Python and Pygame. The primary objective is to design and implement a "Smart Rescue Drone". The project features two distinct modes: a Manual Mode (Human Agent) to demonstrate the UI and game dynamics, and an Autonomous Mode (Utility-based Agent) that balances trade-offs between maximizing rescue operations speed and conserving battery power.

## 📁 Project Files
- `drone_sim.py`: Manual play mode (Human Agent) where the user controls the drone via keyboard.
- `drone_sim2.py`: Autonomous AI mode (Utility-Based Agent) using Manhattan Distance for path evaluation (Algorithm 3).

## ⚙️ Requirements
- Programming Language: Python 3
- GUI & Rendering: Pygame Library

## 🎮 How to Run & Play

**1. Manual Mode (`drone_sim.py`)**
- Press the `SPACE` bar to start/restart.
- **Movement:** Use Arrow Keys (Up, Down, Left, Right) to control the drone's actuators manually.

**2. AI Mode (`drone_sim2.py`)**
- Press the `SPACE` bar to start.
- Watch the Autonomous Agent calculate paths using **Manhattan Distance** and make utility-based decisions to extinguish fires and recharge automatically without human intervention.

## 🧠 Environment Characteristics (ODESA)
- **Fully Observable:** The agent (human or AI) has access to the complete state of the grid.
- **Stochastic:** Fires spawn with a degree of randomness.
- **Sequential:** Each movement decision consumes battery, affecting future capabilities.
- **Dynamic:** The environment changes while playing (fires continue to spawn).
- **Single Agent:** The drone operates alone.

## 🏆 Game Rules (Performance Measure)
To succeed, the agent must maximize fires extinguished and maintain optimal battery levels to avoid crashing.
1. Extinguish **20 fires** to win.
2. Every fire extinguished gives a bonus of **+3 seconds** to the timer.
3. Keep an eye on the battery; return to the green base to recharge to 100%.
