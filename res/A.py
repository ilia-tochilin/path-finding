from queue import PriorityQueue
import math
from res.Base import base

class a(base):
    def __init__(self, graph, mat, start, end):
        base.__init__(self, graph, mat, start, end)
        self.queue = PriorityQueue()
        self.queue.put((0, start))

        ''' Beginning distance equal to 0 '''
        self.graph.array[start[0], start[1]]["dist"] = 0

    def makeStep(self):
        node = self.queue.get()[1]
        self.graph.array[node[0], node[1]]["val"] = 'E'

        if node == self.end:
            self.reconstPath(node)
            return True
        
        # get neighbours
        neig = self.mat [node[0] * self.graph.array.shape[1] + node[1]]

        for i in neig:
            if self.graph.array[i[0], i[1]]["expanded"] == False:
                self.addPrev(i, node)
                dist = math.sqrt(math.pow(self.end[0] - node[0], 2) + math.pow(self.end[1] - node[1], 2))

                self.queue.put((dist, i))

        self.graph.array[node[0], node[1]]["expanded"] = True
        return False