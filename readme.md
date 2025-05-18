# A* Pathfinding Visualizer

🎯 A visual demonstration of the A* pathfinding algorithm built using Python and Pygame.

## 🚀 Features
- 🖱 Click to set:
  - Start node (green)
  - End node (red)
  - Walls (black)
- 🔁 Press:
  - `Enter` to visualize A* search
  - `Space` to reset the board
  - `M` to auto-generate a random maze
- 🎨 Realtime visual updates:
  - Open set (blue)
  - Closed set (orange)
  - Final path (purple)

## 📦 Requirements

Install using pip:

```bash
pip install -r requirements.txt 
```

## 🧠 How It Works

This tool uses the A* algorithm, which combines actual distance (`g`) and heuristic estimate (`h`) to determine the shortest path between two points on a grid.

Visualization colors:

| Color | Meaning              |
|-------|----------------------|
| 🟩    | Start node           |
| 🟥    | End node             |
| ⬛    | Wall (not walkable)  |
| 🔵    | In open set          |
| 🟠    | In closed set        |
| 🟣    | Final path (shortest path) |

## 🧩 Future Improvements

Here are some possible enhancements you can add to this project:

- 🔀 **Algorithm Toggle**:  
  Add support for switching between:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Dijkstra’s Algorithm
  - (Let user press a key or select via button)

- 🖱 **Clickable UI Buttons**:  
  Replace keyboard controls with on-screen buttons for:
  - Start Search
  - Reset Board
  - Generate Maze
  - Choose Algorithm

- 🧱 **Advanced Maze Generation**:
  - Implement *Recursive Division* or *Randomized DFS* maze generation
  - Guarantee solvable mazes
  - Let user choose maze density

- ⏱ **Pathfinding Statistics**:
  - Display path length, search time, open/closed node counts

- 📱 **Mobile-Friendly Pygame Port** (for fun):  
  Touch support + mobile resolution layout

## 🙌 Acknowledgments

This project was inspired by [Tech With Tim](https://www.youtube.com/watch?v=JtiK0DOeI4A)'s tutorial on visualizing the A* pathfinding algorithm using Python and Pygame.