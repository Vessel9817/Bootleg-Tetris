# Bootleg-Tetris

[![CI](https://github.com/Anonymous-Humanoid/Bootleg-Tetris/actions/workflows/ci.yml/badge.svg)](https://github.com/Anonymous-Humanoid/Bootleg-Tetris/actions/workflows/ci.yml)

A simple recreation of competitive two-player Tetris

## Installation

```shell
git clone https://github.com/Anonymous-Humanoid/Bootleg-Tetris
cd Bootleg-Tetris
py -3.13 -m venv './venv'
'./venv/Scripts/activate'
pip install .
py -m bootleg_tetris
```

## Controls

### Player 1

- `W`: Rotate clockwise
- `A`: Move left
- `S`: Move down (soft drop)
- `D`: Move right
- `T`: Rotate 180 degrees
- `F`: Rotate counterclockwise
- `G`: Move down to the bottom (hard drop)
- `H`: Hold block for later

### Player 2

- `NUM 8`: Rotate clockwise
- `NUM 4`: Move left
- `NUM 5`: Move down (soft drop)
- `NUM 6`: Move right
- `I`: Rotate 180 degrees
- `J`: Rotate counterclockwise
- `K`: Move down to the bottom (hard drop)
- `L`: Hold block for later

## Features

- SRS rotation
- Block holding
- Local 2 player
- Competitive play
- Sending garbage lines
- Point system
- Level system
