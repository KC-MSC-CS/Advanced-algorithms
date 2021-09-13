import sys #Library for maxsize integer.


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    #function to print constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    #finding vertex with min distance value. from vertices not yet
    #included in shortest path tree
    def minKey(self, key, mstSet):

        #initializing min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index
    #primting MST graph represented using adjacency matrix
    def primMST(self):

        #key values to pick min weight edge
        key = [sys.maxsize] * self.V
        parent = [None] * self.V #array to store MST
        #making key 0 so this vertex is picked as first vertex.
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1 #first node always root of
        for cout in range(self.V):

            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                #Update key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)
        
g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]
#function call
g.primMST()