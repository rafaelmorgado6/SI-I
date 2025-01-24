# ia-snakes
Snakes clone for AI teaching

## How to install

Make sure you are running Python 3.11.

`$ pip install -r requirements.txt`

*Tip: you might want to create a virtualenv first*

## How to play

Open 3 terminals:

### **Single Player**
Run the server in single-player mode:
`$ python3 server.py`

Run the viewer:
`$ python3 viewer.py`

Run the client (user plays manually) or the AI agent (AI plays for the user):
- **To play manually**: `$ python3 client.py`  
  - Use the **arrow keys** to control the snake.
- **To use the AI agent**: `$ python3 student.py`  
  - The AI will control the snake automatically.

### **Multiplayer**
Run the server in multiplayer mode with 2 players:
`$ python3 server.py --players 2`

Run the viewer:
`$ python3 viewer.py`

Run two instances of the client (or a combination of client and AI agent):
- Example:
  - Terminal 1: `$ python3 client.py` (manual control).
  - Terminal 2: `$ python3 student.py` (AI plays for the second player).

*Note*: In multiplayer mode, you must run one instance of the game for each snake.

### Keys

- **Directions (manual play):** Arrow keys

## Debug Installation

Make sure pygame is properly installed:

`python -m pygame.examples.aliens`

## Project Structure
snake-ai
├── agent.py # Contains the intelligent agent logic
├── student.py # Client script for AI-controlled snake
├── client.py # Client script for manual control
├── server.py # Game server (single-player or multiplayer)
├── viewer.py # Visual interface for observing the game
├── game/ # Game logic and mechanics
├── README.md # Project documentation
└── requirements.txt # Python dependencies


## How it works

1. **Agent Decision Logic**:
   - The agent (`student.py`) analyzes the game state provided by the server.
   - Uses `tree_search` to explore possible moves and selects the best one based on a heuristic:
     - Proximity to food.
     - Safety (avoiding collisions and venoms).
   - If no food is visible, the agent calls `wander` to explore safely.

2. **Key Functions**:
   - `solve(state)`: Main function that processes the game state and determines the next move.
   - `tree_search(depth, head, body, food, bad_food_list)`: Depth-limited search to find the optimal move.
   - `wander(...)`: Generates exploratory movements when no food is visible.
   - `is_safe_move(...)`: Ensures that moves avoid collisions and hazards.

3. **Client-Server Interaction**:
   - The `student.py` or `client.py` script connects to the server.
   - The server provides the game state, and the script sends back a movement command (from the user or the AI).

## Algorithms

### Search Algorithm:
- **Depth-Limited Search**:
  - Explores possible states up to a fixed depth.
  - Uses a heuristic to prioritize states closer to the goal (food).

### Heuristic:
- Distance to the nearest food:
  \[
  h(n) = -\text{distancia\_Manhattan}
  \]
- Encourages movements that minimize the distance to the closest food.

## Future Improvements

- Implement **A*** for more efficient pathfinding.
- Optimize performance by reducing unnecessary recalculations in `wander`.
- Use machine learning techniques like reinforcement learning for adaptive behavior.


