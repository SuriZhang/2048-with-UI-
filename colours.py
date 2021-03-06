
BLACK = (74, 76, 87)
RED = (231, 78, 51)
PINK = (240, 120, 140)
PURPLE = (151, 104, 209)
DEEP_PURPLE = (103, 58, 183)
BLUE = (100, 154, 255)
TEAL = (0, 150, 136)
L_GREEN = (139, 195, 74)
GREEN = (112, 42, 93)
ORANGE = (233, 130, 75)
DEEP_ORANGE = (223, 177, 21)
BROWN = (271, 172, 132)

colour_dict = { 0:BLACK, 2:RED, 4:PINK, 8:PURPLE, 16:DEEP_PURPLE, 32:BLUE, 64:TEAL, \
				128:L_GREEN, 256:GREEN, 512:ORANGE, 1024: DEEP_ORANGE, 2048:BROWN}

def getColour(i):
	return colour_dict[i]