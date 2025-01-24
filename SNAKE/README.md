# ia-snakes
Snakes clone for AI teaching

## How to install

Make sure you are running Python 3.11.

`$ pip install -r requirements.txt`

*Tip: you might want to create a virtualenv first*

## How to play

Open 3 terminals:

`$ python3 server.py`

`$ python3 viewer.py`

`$ python3 client.py`

To play using the sample client, make sure the client pygame hidden window has focus.

### Keys

- **Directions:** Arrows

## Debug Installation

Make sure pygame is properly installed:

`python -m pygame.examples.aliens`

## Project Structure

## How it works

1. **Agent Decision Logic**:
   - The agent analyzes the game state provided by the server.
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
   - The `student.py` script manages communication with the server.
   - The server provides the game state, and the agent responds with a movement command.

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
- Add support for multiplayer scenarios (handling other snakes).
- Optimize performance by reducing unnecessary recalculations in `wander`.
- Use machine learning techniques like reinforcement learning for adaptive behavior.

# Tested on:
- MacOS 15.0.1
