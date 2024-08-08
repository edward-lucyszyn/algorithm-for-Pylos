## Algorithm for Pylos

### Game Overview

The Pyramid Game is a strategic two-player board game where the goal is to build a pyramid by stacking blocks on a grid. Each player controls a set of blocks, either black or white, and takes turns placing them on the board according to specific rules.

#### Game Rules

1. **Objective**: The primary objective is to build a pyramid with your blocks, stacking them layer by layer.
2. **Board Layout**: The board consists of multiple levels, with each level having a grid that reduces in size as you move up. The base level (0) has the largest grid, while the top level (3) has the smallest.
3. **Player Turns**: Players alternate turns, starting with the black blocks (-1), followed by the white blocks (+1).
4. **Block Placement**: Blocks can be placed on the board following specific rules:
   - A block can be placed on an empty spot on the current level.
   - To place a block on a higher level, there must be supporting blocks underneath on the lower level.
5. **Winning Condition**: The game ends when one player successfully places their block on the top level of the pyramid or when no more moves are possible.

### Project Description

This project focuses on implementing an Artificial Intelligence (AI) player for the Pyramid Game using a provided framework. The main task is to develop a heuristic function that will be used by the ALPHABETA algorithm to determine the best possible moves for the AI player.

#### Project Tasks and Constraints

1. **Heuristic Implementation**: 
   - Develop a heuristic function that evaluates the game board and returns a score.
   - The heuristic should quickly compute a value indicating how favorable the board state is for the AI player.
   - A positive score indicates a favorable state for the AI player (Max), while a negative score indicates an unfavorable state.

2. **Sorting Moves (Optional)**: 
   - Optionally implement a move-sorting function to help the ALPHABETA algorithm reach greater depths in its search.
   - The function should order possible moves to optimize the performance of the AI.

3. **Restrictions**:
   - Do not modify the class constructor (`__init__`) of the `AIPlayer`.
   - Do not add parameters to the existing functions provided in the framework.
   - Focus solely on enhancing the `AIPlayer` class without altering other parts of the code.

4. **File Submission**:
   - Rename the `aiplayer.py` file to `NOM_prenom.py` before submission.
   - Ensure that the variable `name` in the code is set to your full name.
   - Submit the program by the deadline: December 18.

### Getting Started

1. **Download and Setup**:
   - Download the provided Pyramid archive and extract it to your chosen directory.
   - The folder contains all necessary source files for the project.

2. **Testing**:
   - Test your AI by running `main.py` which pits your AI against itself.
   - Replace one AI instance with `HumanPlayer` to play against your AI manually.

### Class Information

- **Board Class**: Represents the game board with a property `board.cells`, which is a nested list representing the grid at different levels.
  - Example Access: `board.cells[level][line][col]`

- **AIPlayer Class**: The class where you will implement your heuristic and any additional methods needed for your AI to perform well in the game.

### Course Context

This project was completed as part of the "Computational Approach to Games" course during my first year at CentraleSupélec.

### Conclusion

I enjoyed this project as it allowed me to improve my understanding of the ALPHABETA algorithm. Additionally, I received one of the highest grades for the project, indicating that my AI was among the most effective. It was a pleasure to work on this project.