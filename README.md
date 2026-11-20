# Nouka Runner

Name: Brishty Pain
Student ID:11230321211

## About the Game

Nouka Runner is a 2D river game made with Python and pygame. You steer a country boat (nouka) down a river, dodge water hyacinth and floating logs, and collect hilsa fish to score as many points as possible before you run out of lives.

## How to Play

| Key | Action |
|---|---|
| Left Arrow / A | Move boat to the left lane |
| Right Arrow / D | Move boat to the right lane |
| P | Pause / resume |
| Enter / Space | Start the game (from the menu) |
| R | Restart (on the game over screen) |
| Esc | Back to menu (while playing) / quit (on menu or game over screen) |

**Rules**
- Hilsa fish: +10 points
- Surviving: +1 point every half second
- Hitting water hyacinth or a log: lose 1 life (you start with 3)
- The game ends when all lives are gone

## Features

- Graphical window drawn with pygame (no image files needed)
- Boat controlled with the keyboard, moving smoothly between 3 lanes
- Moving objects: water hyacinth, logs and hilsa fish
- Collision detection between the boat and every object
- Score shown on screen during play
- Game over screen showing the final score
- Restart with R or quit with Esc
- Levels: a new level every 100 points, and the river gets faster
- Stage colours change with each level (Morning, Day, Sunset)
- 3 lives, shown as red circles, with a blinking boat after a hit
- High score saved to a file (`highscore.json`)
- Pause option (P key)
- Start menu
- Scrolling river ripples and trees on the banks
