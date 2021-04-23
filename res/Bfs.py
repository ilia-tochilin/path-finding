from queue import Queue
from res.Base import base

class bfs(base):
    def __init__(self, graph, mat, start, end):
        base.__init__(self, graph, mat, start, end)
        self.queue = Queue()
        self.queue.put(start)
    
    def makeStep(self):
        node = self.queue.get()
        self.graph.array[node[0], node[1]]["val"] = 'E'

        if node == self.end:
            self.reconstPath(node)
            return True
        
        neig = self.mat [node[0] * self.graph.array.shape[1] + node[1]]
        for i in neig:
            if self.graph.array[i[0], i[1]]["expanded"] == False:
                self.addPrev(i, node)
                self.queue.put(i)

        self.graph.array[node[0], node[1]]["expanded"] = True
        return False
