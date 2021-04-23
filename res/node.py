class Node:
    def __init__(self, row, col, val):
        self.expanded = False
        self.neighbours = []
        self.row = 0
        self.col = 0
        self.body = val
        
    def setBody(self, char):
        self.body = str(char)