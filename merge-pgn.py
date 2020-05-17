# Author: Aven Bross
#
# Description: A simple tool to merge several pgn games into a single game with
# variations.

import chess.pgn
import sys


def main():
    try:
        args = sys.argv[1:]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <string_to_reverse>")

    games = []
    for name in args:
        pgn = open(name, encoding="utf-8-sig")
        game = chess.pgn.read_game(pgn)
        while game is not None:
            games.append(game)
            game = chess.pgn.read_game(pgn)

    master_node = chess.pgn.Game()

    mlist = []
    for game in games:
        mlist.extend(game.variations)

    variations = [(master_node, mlist)]
    done = False

    while not done:
        newvars = []
        done = True
        for vnode, nodes in variations:
            newmoves = {}
            for node in nodes:
                if node.move is None:
                    continue
                elif node.move not in list(newmoves):
                    nvnode = vnode.add_variation(node.move)
                    if len(node.variations) > 0:
                        done = False
                    newvars.append((nvnode, node.variations))
                    newmoves[node.move] = len(newvars) - 1
                else:
                    nvnode, nlist = newvars[newmoves[node.move]]
                    if len(node.variations) > 0:
                        done = False
                    nlist.extend(node.variations)
                    newvars[newmoves[node.move]] = (nvnode, nlist)
        variations = newvars

    print(master_node)


main()
