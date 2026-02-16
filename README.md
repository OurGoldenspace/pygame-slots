# Pygame Slots
#### Pygame-based slot machine with easily changeable symbols, sound effects, and music.

## Demos
#### Graphics/music included in this Github repo:

https://user-images.githubusercontent.com/98667270/189539691-6cc22c1d-d719-4339-9889-77163738a07d.mp4

#### Licensed symbols via Adobe Stock and additional sound effects via Google search:

https://user-images.githubusercontent.com/98667270/189508033-ac361229-e493-44d3-a441-e075d22c3ddb.mp4

## Features

- Five reels, each with three symbols in play at any given time
- 300x300 png image symbols that are easy to change via Python dictionary
- Easy-to-import audio (commented out by default)
- Basic win animation
- Basic UI

## Tech

Basically just Pygame:

- [Pygame] - Python game library
- Images/Music/Sound effects

## Installation

Pygame and Python3 are required, as well as the [kidspace.ttf] font in graphics/font/

```sh
pip install -r requirements.txt
```

From cmd/PowerShell:

```sh
python main.py
```

## Media

I have provided some basic symbols that don't look great but they work well enough.  You can simply add a new directory and create a new symbol dictionary in settings.py to replace them.  Same with audio files!  See comments throughout for more info.

## Win Data
win_data is formatted as such:  
`{1: ['symbol_1', [1, 2, 3]], 3: ['symbol_2', [0, 1, 2]]}` 





