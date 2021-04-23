class base:
    def __init__(self, graph, mat, start, end):
        self.graph = graph
        self.start = start
        self.mat = mat
        self.end = end

    ''' Adds pointer to the node, from whitch this node was expanded '''
    def addPrev(self, to, from_):
        print (from_)
        self.graph.array[to[0], to[1]]["prev"] = from_
        print (self.graph.array[to[0], to[1]]["prev"])

    def reconstPath(self, start):
        currentNode = start
        while currentNode != self.start:
            self.graph.array[currentNode[0], currentNode[1]]["val"] = "P"
            currentNode = self.graph.array[currentNode[0], currentNode[1]]["prev"]
