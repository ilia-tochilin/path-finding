from queue import Queue, LifoQueue, PriorityQueue
import numpy as np
import typing
import pygame
from res.node import Node
from res.Arr import myArr
from res.Bfs import bfs
from res.Dfs import dfs
from res.Dijk import dijk
from res.A import a
from res.Astar import astar
from consts import *


def go_fast (graph, wholeGraph):
    for line in graph:
        for char in line:
            if char == 'X':
                wholeGraph.push (char, True, 2)
                continue
            wholeGraph.push (char)
    return wholeGraph

def makeGraph(graph):

    graph = graph.split ('\n')
    rowsNumber = len (graph)
    rowLen  = len (graph[0])


    dt = np.dtype ([("val", np.str, 1), ("expanded", np.bool), ("dist", np.int16), ("prev", typing.List)])
    wholeGraph = myArr (np.zeros ((rowsNumber * rowLen), dtype=dt), rowLen)

    wholeGraph = go_fast (graph, wholeGraph)
    
    return wholeGraph

def addNeigh (neigh, to, who):
    neigh.append([to, who])

def createGraph (graph):
    neigh = []

    for i in range(graph.array.shape[0]):
        for j in range(graph.array.shape[1]):
            
            tmp = []

            if graph.array[i, j]["expanded"] == True:
                neigh.append([])
                continue

            if i == 0 and j == 0:
                if graph.array[i + 1, j]["expanded"] != True:
                    tmp.append([i + 1, j])
                if graph.array[i, j + 1]["expanded"] != True:
                    tmp.append([i, j + 1])
            elif i == 0 and j == graph.array.shape[1] - 1:
                if graph.array[i + 1, j]["expanded"] != True:
                    tmp.append([i + 1, j])
                if graph.array[i, j - 1]["expanded"] != True:
                    tmp.append([i, j - 1])
            elif i == graph.array.shape[0] - 1 and j == 0:
                if graph.array[i - 1, j]["expanded"] != True:
                    tmp.append([i - 1, j])
                if graph.array[i, j + 1]["expanded"] != True:
                    tmp.append([i, j + 1])
            elif i == graph.array.shape[0] - 1 and j == graph.array.shape[1] - 1:
                if graph.array[i - 1, j]["expanded"] != True:
                    tmp.append([i - 1, j])
                if graph.array[i, j - 1]["expanded"] != True:
                    tmp.append([i, j - 1])

            elif i == 0 or i == graph.array.shape[0] - 1 or j == 0 or j == graph.array.shape[1] - 1:
                # first row
                if i == 0:
                    if graph.array[i, j - 1]["expanded"] != True:
                        tmp.append([i, j - 1])
                    if graph.array[i, j + 1]["expanded"] != True:
                        tmp.append([i, j + 1])
                    if graph.array[i + 1, j]["expanded"] != True:
                        tmp.append([i + 1, j])
                # last row
                elif i == graph.array.shape[0] - 1:
                    if graph.array[i, j - 1]["expanded"] != True:
                        tmp.append([i, j - 1])
                    if graph.array[i, j + 1]["expanded"] != True:
                        tmp.append([i, j + 1])
                    if graph.array[i - 1, j]["expanded"] != True:
                        tmp.append([i - 1, j])
                # first col
                elif j == 0:
                    if graph.array[i, j + 1]["expanded"] != True:
                        tmp.append([i, j + 1])
                    if graph.array[i + 1, j]["expanded"] != True:
                        tmp.append([i + 1, j])
                    if graph.array[i - 1, j]["expanded"] != True:
                        tmp.append([i - 1, j])
                # last col
                elif j == graph.array.shape[1] - 1:
                    if graph.array[i, j - 1]["expanded"] != True:
                        tmp.append([i, j - 1])
                    if graph.array[i + 1, j]["expanded"] != True:
                        tmp.append([i + 1, j])
                    if graph.array[i - 1, j]["expanded"] != True:
                        tmp.append([i - 1, j])
            else:
                if graph.array[i, j + 1]["expanded"] != True:
                    tmp.append([i, j + 1])
                if graph.array[i, j - 1]["expanded"] != True:
                    tmp.append([i, j - 1])
                if graph.array[i + 1, j]["expanded"] != True:
                    tmp.append([i + 1, j])
                if graph.array[i - 1, j]["expanded"] != True:
                    tmp.append([i - 1, j])

            if not tmp:
                neigh.append([])
            neigh.append(tmp)
    return neigh

def drawGraph(graph, gui):
    WHITE = gui[0]
    BLACK = gui[1]
    GREEN = gui[2]
    BLOCK_SIZE = gui[3]
    MARGIN = gui[4]
    SIZE = gui[5]
    screen = gui[6]

    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    # Draw Graph #u8
    for i in range(SIZE[1] // (BLOCK_SIZE + MARGIN)):
        for j in range(SIZE[0] // (BLOCK_SIZE + MARGIN)):

            rect = pygame.Rect(j * (BLOCK_SIZE + MARGIN), i * (BLOCK_SIZE + MARGIN), BLOCK_SIZE, BLOCK_SIZE)
            tmp = graph.array[i, j]["val"]
            if tmp == 'X':
                color = BLACK
            elif tmp == 'E':
                color = GREEN
            elif tmp == 'S' or tmp == 'F':
                color = BLUE
            elif tmp == 'P':
                color = YELLOW
            else:
                color = WHITE

            pygame.draw.rect(screen, color, rect, 0)
    # End #

def chooseAlg (alg, graph, mat, start, end):
    if alg == "bfs":
        return bfs(graph, mat, start, end)
    if alg == "dfs":
        return dfs(graph, mat, start, end)
    if alg == "dijk":
        return dijk(graph, mat, start, end)
    if alg == "a":
        return a(graph, mat, start, end)
    if alg == "astar":
        return astar(graph, mat, start, end)

    return "fuck you with your algorithms"



def start():

    with open("dataset/{}".format(TEST_FILE), "r") as f:
        graph = f.read()

    graph = makeGraph(graph)
    graph.array = np.reshape(graph.array, (graph.array.shape[0] // graph.rowLen, -1))
    graph.out ()

    mat = createGraph (graph)

    start = START
    end = END

    graph.array[start[0], start[1]]['val'] = 'S'
    graph.array[end[0], end[1]]['val'] = 'F'

    # GUI init #
    nrows = graph.array.shape[0] # 7
    ncols = graph.array.shape[1] # 55
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    BLOCK_SIZE = 24
    MARGIN = 1
    SIZE = ((BLOCK_SIZE + MARGIN) * ncols, (BLOCK_SIZE + MARGIN) * nrows)
    
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    # End #

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit (1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                run = False
        
        screen.fill(WHITE)
        rect = pygame.Rect(0, 0, SIZE[0], SIZE[0])
        pygame.draw.rect(screen, (0, 255, 0), rect, 0)
        
        pygame.display.update()
        clock.tick(60)

    alg = chooseAlg(ALG, graph, mat, start, end)

    run = True
    while run:
        pygame.event.get()

        screen.fill(WHITE)

        drawGraph(graph, [WHITE, BLACK, GREEN, BLOCK_SIZE, MARGIN, SIZE, screen, clock])

        if alg.makeStep():
            drawGraph(graph, [WHITE, BLACK, GREEN, BLOCK_SIZE, MARGIN, SIZE, screen, clock])
            pygame.display.update()
            print("DONE")
            pygame.time.delay(10 * 1000)
            continue


        pygame.display.update()
        clock.tick(60)



if __name__=="__main__":
    start()