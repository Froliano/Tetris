NUMBER_BLOCK_LINE = 8
WINDOW_SIZE = (800, 720)
PLACE_SPACE_POS = (50, 10)
PLACE_SPACE_SIZE = (320, 640)

BLOCK_SIZE = int(PLACE_SPACE_SIZE[0] / NUMBER_BLOCK_LINE)
PLACE_SPACE_SIZE = (PLACE_SPACE_SIZE[0] - (PLACE_SPACE_SIZE[0] % NUMBER_BLOCK_LINE), PLACE_SPACE_SIZE[1] - PLACE_SPACE_SIZE[1] % BLOCK_SIZE)


rightLPos = {
        1 : [["X", "_", "_"],
             ["X", "X", "X"]],

        2 : [["X", "X", "_"],
             ["X", "_", "_"],
             ["X", "_", "_"]],

        3 : [["X", "X", "X"],
             ["_", "_", "X"]],

        4 : [["_", "X", "_"],
             ["_", "X", "_"],
             ["X", "X", ""]]
    }

leftLPos = {
        1 : [["_", "_", "X"],
             ["X", "X", "X"]],

        2 : [["X", "", "_"],
             ["X", "_", "_"],
             ["X", "X", "_"]],

        3 : [["X", "X", "X"],
             ["X", "_", ""]],

        4 : [["X", "X", "_"],
             ["_", "X", "_"],
             ["_", "X", "_"]]
    }

sBlockPos = {
        1 : [["_", "X", "X"],
             ["X", "X", "_"]],

        2 : [["X", "_", "_"],
             ["X", "X", "_"],
             ["_", "X", "_"]],

        3 : [["_", "X", "X"],
             ["X", "X", ""]],

        4 : [["X", "_", "_"],
             ["X", "X", "_"],
             ["_", "X", "_"]]
    }

zBlockPos = {
        1 : [["X", "X", "_"],
             ["_", "X", "X"]],

        2 : [["_", "X", "_"],
             ["X", "X", "_"],
             ["X", "_", "_"]],

        3 : [["X", "X", "_"],
             ["_", "X", "X"]],

        4 : [["_", "X", "_"],
             ["X", "X", "_"],
             ["X", "_", "_"]]
    }

tBlockPos = {
        1 : [["_", "X", "_"],
             ["X", "X", "X"]],

        2 : [["X", "_", "_"],
             ["X", "X", "_"],
             ["X", "_", "_"]],

        3 : [["X", "X", "X"],
             ["_", "X", "_"]],

        4 : [["_", "X", "_"],
             ["X", "X", "_"],
             ["_", "X", "_"]]
}

iBlockPos = {
        1 : [["X", "_", "_"],
             ["X", "_", "_"],
             ["X", "_", "_"],
             ["X", "_", "_"]],

        2 : [["X", "X", "X", "X"]],

        3 : [["X", "_", "_"],
             ["X", "_", "_"],
             ["X", "_", "_"],
             ["X", "_", "_"]],

        4 : [["X", "X", "X", "X"]]
}

oBlockPos = {
        1 : [["X", "X", "_"],
             ["X", "X", "_"]],

        2 : [["X", "X", "_"],
             ["X", "X", "_"]],

        3 : [["X", "X", "_"],
             ["X", "X", "_"]],

        4 : [["X", "X", "_"],
             ["X", "X", "_"]]
}

ALL_FIGURES = [rightLPos, leftLPos, sBlockPos, zBlockPos, tBlockPos, iBlockPos, oBlockPos]















