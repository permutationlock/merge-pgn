## Merge-PGN

A simple tool for merging several pgn games into a single pgn with one
game including all moves as variations. All headers and comments are ignored as
this is designed only to manipulate the move lines.

Requires you to have [python-chess](https://python-chess.readthedocs.io)
installed.

```
pip install python-chess
```

I needed this tool to construct pgn files to upload to ChessTempo's opening
trainer.

Example:
```
python merge-pgn.py "game1.pgn" "game2.pgn" "games3-7.pgn" > "all_games.pgn"
```
