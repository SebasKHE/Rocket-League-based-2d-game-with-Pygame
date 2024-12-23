# Rocket-League-based-2d-game-with-Pygame

This project is a simple 2D game inspired by the mechanics of *Rocket League*, implemented using the **Pygame** library. The player controls a car to catch a falling ball and score points. It's an engaging project demonstrating how to work with Pygame for collision detection, object movement, and simple game logic.

---

### **Project Overview**
- **Game Objective**: 
  - The goal is to control a car and prevent the ball from touching the ground.
  - For every successful touch, the player scores a point.
  - If the ball hits the ground, the player loses a life.
  - The game ends when all lives are lost, and the highest score is recorded.

- **Key Features**:
  - Smooth object movement and gravity simulation for the ball.
  - Simple user interface for displaying score and lives.
  - Basic Pygame elements such as sprite groups, event handling, and drawing.

---

### **Project File Structure**
1. **`coche.py`**: 
   - Contains the `Car` class, which defines the player's car behavior, including movement and interactions with other objects (like the ball).

2. **`ejecutable.py`**:
   - The main file to run the game. It initializes Pygame, sets up the game loop, and handles overall game flow, including drawing and updates.

3. **`funciones.py`**:
   - Helper functions used across the game, such as collision detection, score updates, or resetting the ball's position.

4. **`settings5.py`**:
   - Configuration file for game settings such as screen dimensions, colors, car speed, ball speed, and initial lives.

5. **`stats.py`**:
   - Tracks the game's statistics, including the current score, high score, and remaining lives.

6. **`balon.png`**:
   - Sprite image for the ball.

7. **`rocket-league.png`**:
   - Sprite or background image for the car or other game assets.

---

### **Installation Guide**
Follow these steps to clone the repository and set up the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SebasKHE/Rocket-League-based-2d-game-with-Pygame.git
   cd Rocket-League-based-2d-game-with-Pygame
   ```

2. **Install Python**:
   Ensure you have Python 3.8 or later installed. You can download it from [python.org](https://www.python.org/).

3. **Set Up a Virtual Environment** (Optional but Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Linux/Mac
   venv\Scripts\activate         # On Windows
   ```

4. **Install Dependencies**:
   Install the required libraries specified in `requirements.txt` (if included) or manually install **Pygame**:
   ```bash
   pip install pygame
   ```

5. **Run the Game**:
   Execute the main script to start the game:
   ```bash
   python ejecutable.py
   ```

---

### **Future Enhancements**
Here are some ideas to expand the project:
- Add multiple difficulty levels with faster balls or limited time.
- Introduce power-ups or penalties.
- Include additional sounds and animations for a more immersive experience.
