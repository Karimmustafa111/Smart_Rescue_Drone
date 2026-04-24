# Smart_Rescue_Drone

# Smart Rescue Drone Simulator

## 📌 Project Description
[cite_start]This project is a 2D interactive simulator developed using Python and Pygame[cite: 2]. [cite_start]The primary objective is to design and implement a "Smart Rescue Drone"[cite: 3]. [cite_start]The system is designed to demonstrate the concepts of a Utility-based Agent [cite: 6][cite_start], balancing trade-offs between maximizing rescue operations speed and conserving battery power[cite: 9].

## ⚙️ Requirements
- [cite_start]Programming Language: Python 3[cite: 21].
- [cite_start]GUI & Rendering: Pygame Library[cite: 21].

## 🎮 How to Play
[cite_start]The drone navigates within a discrete grid environment to detect and extinguish fires and return to a central charging base before its battery depletes[cite: 4].
- [cite_start]**Movement:** Use Arrow Keys (Up, Down, Left, Right) to control the drone's actuators[cite: 12].
- **Start/Restart:** Press the `SPACE` bar.

## 🧠 Environment Characteristics (ODESA)
- [cite_start]**Fully Observable:** The player has access to the complete state of the grid[cite: 14].
- [cite_start]**Stochastic:** Fires may spawn with a degree of randomness[cite: 16].
- [cite_start]**Sequential:** Each movement decision consumes battery, affecting future capabilities[cite: 18].
- [cite_start]**Dynamic:** The environment changes while playing (fires continue to spawn)[cite: 19].
- [cite_start]**Single Agent:** The drone operates alone[cite: 20].

## 🏆 Game Rules (Performance Measure)
[cite_start]To succeed, you must maximize fires extinguished and maintain optimal battery levels to avoid crashing[cite: 10].
1. Extinguish **20 fires** to win.
2. Every fire extinguished gives a bonus of **+3 seconds** to the timer.
3. Keep an eye on the battery; return to the green base to recharge to 100%.
