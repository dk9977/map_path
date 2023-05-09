'''
File: lab1.py
Author: Derrick Kempster
Purpose: Program for Lab 1
'''


import math
from PIL import Image
import sys


# SEASONS
SUMMER = 'summer'
FALL = 'fall'
WINTER = 'winter'
SPRING = 'spring'

SEASONS = [SUMMER, FALL, WINTER, SPRING]


# TERRAINS
OPEN_LAND = (248, 148, 18, 255)
ROUGH_MEADOW = (255, 192, 0, 255)
EASY_MOV_FOREST = (255, 255, 255, 255)
SLOW_RUN_FOREST = (2, 208, 60, 255)
WALK_FOREST = (2, 136, 40, 255)
IMPASS_VEG = (5, 73, 24, 255)
WATER = (0, 0, 255, 255)
PAVED_ROAD = (71, 51, 3, 255)
FOOTPATH = (0, 0, 0, 255)
OUT_OF_BOUNDS = (205, 0, 101, 255)
ICE = (0, 187, 255, 255)

LEAFY_OPEN_LAND = (248, 148, 18, 254)
LEAFY_ROUGH_MEADOW = (255, 192, 0, 254)
LEAFY_EASY_MOV_FOREST = (255, 255, 255, 254)
LEAFY_SLOW_RUN_FOREST = (2, 208, 60, 254)
LEAFY_WALK_FOREST = (2, 136, 40, 254)
LEAFY_IMPASS_VEG = (5, 73, 24, 254)
LEAFY_WATER = (0, 0, 255, 254)
LEAFY_PAVED_ROAD = (71, 51, 3, 254)
LEAFY_FOOTPATH = (0, 0, 0, 254)

MUDDY_OPEN_LAND = (248, 128, 0, 255)
MUDDY_ROUGH_MEADOW = (255, 172, 0, 255)
MUDDY_EASY_MOV_FOREST = (255, 235, 235, 255)
MUDDY_SLOW_RUN_FOREST = (2, 188, 40, 255)
MUDDY_WALK_FOREST = (2, 116, 20, 255)
MUDDY_IMPASS_VEG = (5, 53, 4, 255)
MUDDY_PAVED_ROAD = (71, 31, 0, 255)
MUDDY_FOOTPATH = (40, 0, 0, 255)

SPEED = {
    OPEN_LAND:              0.950,
    ROUGH_MEADOW:           0.500,
    EASY_MOV_FOREST:        0.800,
    SLOW_RUN_FOREST:        0.700,
    WALK_FOREST:            0.600,
    IMPASS_VEG:             0.100,
    WATER:                  0.050,
    PAVED_ROAD:             1.000,
    FOOTPATH:               0.900,
    OUT_OF_BOUNDS:          0.001,
    ICE:                    0.400,
    LEAFY_OPEN_LAND:        0.855,
    LEAFY_ROUGH_MEADOW:     0.450,
    LEAFY_EASY_MOV_FOREST:  0.720,
    LEAFY_SLOW_RUN_FOREST:  0.630,
    LEAFY_WALK_FOREST:      0.540,
    LEAFY_IMPASS_VEG:       0.090,
    LEAFY_WATER:            0.045,
    LEAFY_PAVED_ROAD:       0.900,
    LEAFY_FOOTPATH:         0.810,
    MUDDY_OPEN_LAND:        0.475,
    MUDDY_ROUGH_MEADOW:     0.250,
    MUDDY_EASY_MOV_FOREST:  0.400,
    MUDDY_SLOW_RUN_FOREST:  0.350,
    MUDDY_WALK_FOREST:      0.300,
    MUDDY_IMPASS_VEG:       0.050,
    MUDDY_PAVED_ROAD:       0.500,
    MUDDY_FOOTPATH:         0.450
}

FORESTS = [EASY_MOV_FOREST, SLOW_RUN_FOREST, WALK_FOREST]
FREEZABLE = [WATER, ICE]
NOT_SHORE = [WATER, OUT_OF_BOUNDS, ICE]
UNSOAKABLE = [WATER, OUT_OF_BOUNDS]

LEAFEN = {
    OPEN_LAND:              LEAFY_OPEN_LAND,
    ROUGH_MEADOW:           LEAFY_ROUGH_MEADOW,
    EASY_MOV_FOREST:        LEAFY_EASY_MOV_FOREST,
    SLOW_RUN_FOREST:        LEAFY_SLOW_RUN_FOREST,
    WALK_FOREST:            LEAFY_WALK_FOREST,
    IMPASS_VEG:             LEAFY_IMPASS_VEG,
    WATER:                  LEAFY_WATER,
    PAVED_ROAD:             LEAFY_PAVED_ROAD,
    FOOTPATH:               LEAFY_FOOTPATH,
    OUT_OF_BOUNDS:          OUT_OF_BOUNDS,
    LEAFY_OPEN_LAND:        LEAFY_OPEN_LAND,
    LEAFY_ROUGH_MEADOW:     LEAFY_ROUGH_MEADOW,
    LEAFY_EASY_MOV_FOREST:  LEAFY_EASY_MOV_FOREST,
    LEAFY_SLOW_RUN_FOREST:  LEAFY_SLOW_RUN_FOREST,
    LEAFY_WALK_FOREST:      LEAFY_WALK_FOREST,
    LEAFY_IMPASS_VEG:       LEAFY_IMPASS_VEG,
    LEAFY_WATER:            LEAFY_WATER,
    LEAFY_PAVED_ROAD:       LEAFY_PAVED_ROAD,
    LEAFY_FOOTPATH:         LEAFY_FOOTPATH
}
SOAK = {
    OPEN_LAND:              MUDDY_OPEN_LAND,
    ROUGH_MEADOW:           MUDDY_ROUGH_MEADOW,
    EASY_MOV_FOREST:        MUDDY_EASY_MOV_FOREST,
    SLOW_RUN_FOREST:        MUDDY_SLOW_RUN_FOREST,
    WALK_FOREST:            MUDDY_WALK_FOREST,
    IMPASS_VEG:             MUDDY_IMPASS_VEG,
    PAVED_ROAD:             MUDDY_PAVED_ROAD,
    FOOTPATH:               MUDDY_FOOTPATH,
    MUDDY_OPEN_LAND:        MUDDY_OPEN_LAND,
    MUDDY_ROUGH_MEADOW:     MUDDY_ROUGH_MEADOW,
    MUDDY_EASY_MOV_FOREST:  MUDDY_EASY_MOV_FOREST,
    MUDDY_SLOW_RUN_FOREST:  MUDDY_SLOW_RUN_FOREST,
    MUDDY_WALK_FOREST:      MUDDY_WALK_FOREST,
    MUDDY_IMPASS_VEG:       MUDDY_IMPASS_VEG,
    MUDDY_PAVED_ROAD:       MUDDY_PAVED_ROAD,
    MUDDY_FOOTPATH:         MUDDY_FOOTPATH
}

ICE_SHORE = 7
MUD_SHORE = 15


# PATHING
PATH = (255, 0, 0, 255)
PIN = (150, 0, 0, 255)

ADJACENT = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
SQUARE_ADJACENT = [(-1, 0), (0, -1), (0, 1), (1, 0)]

X_MUL = 10.29
Y_MUL = 7.55

ELEV = []


# USER INPUTS
terrain_filename = ''
elevation_filename = ''
path_filename = ''
season = ''
output_filename = ''


'''
Loads all elevations into memory.
@param size     tuple of map width and height
'''
def loadElev(size):
    global ELEV
    ELEV = [[0.0] * (size[0] + 5) for i in range(size[1])]
    with open(elevation_filename) as f:
        row = 0
        for line in f:
            nums = line.split()
            col = 0
            for num in nums:
                ELEV[row][col] = float(num)
                col += 1
            row += 1


'''
Finds the elevation of the specified pixel.
@param row      row of the map
@param col      column of the map
@return         elevation
'''
def elevation(row, col):
    return ELEV[col][row]


'''
Modifies the map to reflect the fall conditions.
@param image    the map to modify
@return         the fall map
'''
def fall(image):
    print('Reformatting for fall...')
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            terrain = image.getpixel((x,y))
            if terrain in FORESTS:
                image.putpixel((x, y), LEAFEN[terrain])
                for (i, j) in ADJACENT:
                    xi, yj = x + i, y + j
                    if xi >= 0 and xi < image.size[0] and \
                            yj >= 0 and yj < image.size[1]:
                                adjterrain = LEAFEN[image.getpixel((xi, yj))]
                                image.putpixel((xi, yj), adjterrain)
    return image


'''
Freezes the water surrounding shores.
@param image    the map to modify
@param coord    the coordinate to start freezing at
'''
def freeze(image, coord):
    start_node = [coord, 0]
    disc = [coord]
    front = [start_node]
    while len(front) > 0:
        cur = front[0]
        for (i, j) in SQUARE_ADJACENT:
            x, y = i + cur[0][0], j + cur[0][1]
            adjc = (x, y)
            if cur[1] < ICE_SHORE and adjc not in disc and x >= 0 and \
                    y >= 0 and x < image.size[0] and y < image.size[1] and \
                    image.getpixel(adjc) in FREEZABLE:
                        image.putpixel(adjc, ICE)
                        disc.append(adjc)
                        front.append([adjc, cur[1] + 1])
        front.remove(cur)


'''
Modifies the map to reflect the winter conditions.
@param image    the map to modify
@return         the winter map
'''
def winter(image):
    print('Reformatting for winter...')
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if image.getpixel((x, y)) not in NOT_SHORE:
                freeze(image, (x, y))
    return image


'''
Muddies the land on shores.
@param image    the map to modify
@param coord    the coordinate to start muddying at
'''
def soak(image, coord):
    start_node = [coord, elevation(coord[0], coord[1]), 0]
    disc = [coord]
    front = [start_node]
    while len(front) > 0:
        cur = front[0]
        for (i, j) in SQUARE_ADJACENT:
            x, y = i + cur[0][0], j + cur[0][1]
            adjc = (x, y)
            if cur[2] < MUD_SHORE and adjc not in disc and x >= 0 and \
                    y >= 0 and x < image.size[0] and y < image.size[1]:
                        terrain = image.getpixel(adjc)
                        if terrain not in UNSOAKABLE:
                            elev = elevation(x, y)
                            if elev < start_node[1] + 1:
                                image.putpixel(adjc, SOAK[terrain])
                                disc.append(adjc)
                                front.append([adjc, elev, cur[2] + 1])
        front.remove(cur)


'''
Modifies the map to reflect the spring conditions.
@param image    the map to modify
@return         the spring map
'''
def spring(image):
    print('Reformatting map for spring...')
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if image.getpixel((x, y)) == WATER:
                soak(image, (x, y))
    return image


'''
Modifies the map to reflect the seasonal conditions.
@param image    the map to modify
@return         the seasonal map
'''
def seasonModify(image):
    if season == FALL:
        return fall(image)
    if season == WINTER:
        return winter(image)
    if season == SPRING:
        return spring(image)
    return image


'''
Finds the coordinates to reach in when exploring.
@return         the specified coordinates
'''
def getCoords():
    coords = []
    with open(path_filename) as f:
        for line in f:
            strcoord = line.split()
            coord = (int(strcoord[0]), int(strcoord[1]))
            coords.append(coord)
    return coords


'''
Determines the heuristic based on distance to goal, terrain, and elevation.
@param image    the map with the coordinates
@param coord    the coordinate to score
@param end      the ending coordinate
@return         the score of the coordinate
'''
def score(image, coord, end):
    xd = X_MUL * (coord[0] - end[0])
    yd = Y_MUL * (coord[1] - end[1])
    zd = elevation(coord[0], coord[1]) - elevation(end[0], end[1])
    dist = math.sqrt(xd * xd + yd * yd + zd * zd)
    speed = SPEED[image.getpixel(coord)]
    return dist / speed


'''
Finds a path from the start to end with an A* search.
@param image    the map to search through
@param start    the starting coordinate
@param end      the ending coordinate
@return         the path from start to finish
'''
def search(image, start, end):
    start_node = [start, score(image, start, end), [start]]
    disc = [start]
    front = [start_node]
    cur = start_node
    while cur[0] != end:
        for (i, j) in ADJACENT:
            coord = (cur[0][0] + i, cur[0][1] + j)
            if coord not in disc:
                disc.append(coord)
                newscore = cur[1] + score(image, coord, end)
                front.append([coord, newscore, cur[2] + [coord]])
        front.remove(cur)
        champ = front[0]
        for node in front:
            if node[1] < champ[1]:
                champ = node
        cur = champ
    return cur[2]


'''
Finds the full path along all coordinates in order.
@param image    the map with the coordinates
@param coords   the coordinates the path will follow
@return         the fastest path that hits all coordinates
'''
def path(image, coords):
    fullpath = []
    for i in range(len(coords) - 1):
        subpath = search(image, coords[i], coords[i + 1])
        for j in range(len(subpath) - 1):
            fullpath.append(subpath[j])
    fullpath.append(coords[-1])
    return fullpath


'''
Finds the distance traveled along the path.
@param coords   the coordinates of the path points
@return         the distance along the path
'''
def pathDist(coords):
    dist = 0
    for i in range(len(coords) - 1):
        xd = coords[i + 1][0] - coords[i][0]
        yd = coords[i + 1][1] - coords[i][1]
        if xd == 0:
            dist += Y_MUL
        elif yd == 0:
            dist += X_MUL
        else:
            dist += X_MUL * Y_MUL
    return dist


'''
Marks all specified coordinates as a path.
@param image    the map to modify
@param coords   the list of coordinates
'''
def sketch(image, coords):
    for coord in coords:
        image.putpixel(coord, PATH)


'''
Marks a 3x3 pixel square on all specified coordinates.
@param image    the map to modify
@param coords   the list of coordinates
'''
def pin(image, coords):
    for (x, y) in coords:
        for (i, j) in ADJACENT:
            image.putpixel((x + i, y + j), PIN)


'''
The main portion of the path generation algorithm.
'''
def main():
    terrain = Image.open(terrain_filename)
    loadElev(terrain.size)
    outmap = seasonModify(terrain.copy())
    coords = getCoords()
    print('Finding path...')
    fullpath = path(outmap, coords)
    print('Path distance: ' + str(pathDist(fullpath)) + ' meters')
    sketch(outmap, fullpath)
    pin(outmap, coords)
    outmap.save(output_filename)
    outmap.show()


if __name__ == '__main__':
    terrain_filename += sys.argv[1]
    elevation_filename += sys.argv[2]
    path_filename += sys.argv[3]
    season += sys.argv[4]
    output_filename += sys.argv[5]

    if season not in SEASONS:
        raise Exception

    main()

