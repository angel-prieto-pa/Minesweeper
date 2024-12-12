# Minesweeper
This project is a Python recreation of the classic Minesweeper game, designed to explore Python programming concepts such as logic, user interface design, and game mechanics.

## Table of Contents
- [Features](#features)
- [Gameplay Overview](#gameplay-overview)
- [Setup](#setup)
- [Project Structure](#project-structure)
- [Acknowledgments](#acknowledgments)

## Features

- **Graphical User Interface (GUI):** A user-friendly GUI built with Tkinter for enhanced gameplay experience.

- **Interactive Gameplay:** Abiltiy to reveal cells, flag potential mines, mark unknown states, and uncover the board to win.

- **Automatic Cell Clearing:** Automatically clear adjacent safe cells when applicable.

- **Timer:** Tracks the time taken to complete the game.

- **Bomb Counter:** Displays the number of remaining bombs based on the flags placed by the user.


- **Win and Lose Conditions:** Clear the board without triggering any mines to win or hit a mine to lose.

## Gameplay Overview

### Game Instructions

Use the graphical interface to click on cells in order to reveal them or right-click to add a marker to the cell.
- If a cell has no marker, right-click the cell to flag it as a potential mine.
- If a cell is flagged, right-click the cell again to mark it as unknown.
- If a cell is marked as unknown, a subsequent right-click will return the cell to its initial state without markers.

*Note: Flagged cells cannot be revealed. Mark the cell as unknown or return it to its initial state to reveal it.*

### Game Objective

Avoid revealing cells with mines while clearing the rest of the board.

Win the game by uncovering all safe cells, or lose if you reveal a mine.

## Setup

### Prerequisites

To run this project, ensure you have the following installed:

- Python 3.0 or higher

### Installation
To clone the repository, use the following command:
```bash
 git clone https://github.com/angel-prieto-pa/Minesweeper.git
```

### Execution

To run the project, use the following command:
```bash
python minesweeper.py
```

## Project Structure

```bash
minesweeper/
|-- assets/             # Static assets used by the game.
|-- minesweeper.py      # Game script.
|-- README.md           # The project's documentation.
```

## Acknowledgments

Inspired by the original Minesweeper game.