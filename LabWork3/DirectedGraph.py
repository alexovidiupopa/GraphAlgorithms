from ProgramException import myException
import math
class DirectedGraph(object):
    
    def __init__(self,vertices):
        
        self.__dictIn = {}
        
        self.__dictOut = {}
        
        self.__dictCosts = {}

        for i in range(vertices):
            self.__dictOut[i]=[]
            self.__dictIn[i] = []
    
    def parseKeys(self):
        """returns a copy of all the vertex keys"""
        return list(self.__dictOut.keys())
        
    def parseIterableOut(self,x):
        """returns a copy of all out neighbours of x"""
        try:
            return list(self.__dictOut[x])
        except KeyError:
            raise myException("No such vertex")
        
    def parseIterableIn(self,x):
        """return a copy of all in neighbours of x"""
        try:
            return list(self.__dictIn[x])
        except KeyError:
            raise myException("No such vertex")
        
    def isEdge(self,start,end):
        """Returns True if there is an edge from x to y, False otherwise"""
        try:
            return end in self.__dictOut[start]
        except KeyError: 
            raise myException("No such pair of vertices in the graph.")
        
    def addEdge(self,start,end,cost):
        """adds an edge (start,end) that has that cost to the graph
           precondition: the edge mustn't already exist and the vertices need to be valid"""
        exception = ""
        if self.isEdge(start,end):
            exception += "Already an edge;" 
        if len(exception):
            raise myException(exception)
        self.__dictOut[start].append(end)
        self.__dictIn[end].append(start)
        self.__dictCosts[(start,end)] = cost

    def addVertex(self,x):
        """adds the vertex x to the graph, as an isolated vertex
            precondition: x mustn't already be a vertex in the graph"""
        if x in self.parseKeys():
            raise myException("Already existing vertex")
        self.__dictOut[x] = []
        self.__dictIn[x] = []
        
    def retrieveCost(self,start,end):
        if self.isEdge(start,end):
            return self.__dictCosts[(start,end)]
        
    def removeVertex(self,x):
        """removes the vertex x from the graph
           precondition: x needs to exist in the graph as a vertex"""
        if x not in self.parseKeys():
            raise myException("Vertex doesn't exist")
        for y in self.__dictOut[x]: 
                self.__dictIn[y].remove(x)
                del self.__dictCosts[(x,y)]
        del self.__dictOut[x]
        for y in self.__dictIn[x]: 
                self.__dictOut[y].remove(x)
                del self.__dictCosts[(y,x)]
        del self.__dictIn[x]
            
    def removeEdge(self,x,y):
        """removes the edge (x,y) from the graph
            precondition: (x,y) needs to be a valid edge in the graph """
        if not self.isEdge(x,y):
            raise myException("This edge doesn't exist")
        del self.__dictCosts[(x,y)]
        self.__dictOut[x].remove(y)
        self.__dictIn[y].remove(x)
        
    def getNumberOfVertices(self):
        """return an integer containing the number of vertices in the graph"""
        return len(self.parseKeys())
    
    def getOutDegree(self,x):
        """return an integer representing the out degree of the vertex x
           precondition: x needs to be a valid vertex in the graph 
                         in case it isn't, the error is handled and the user is informed"""
        try:
            return len(self.__dictOut[x])
        except KeyError:
            raise myException("No such vertex")
        
    def getInDegree(self,x):
        """return an integer representing the in degree of the vertex x
           precondition: x needs to be a valid vertex in the graph """
        try:
            return len(self.__dictIn[x])
            
        except KeyError:
            raise myException("No such vertex")

    def modifyEdgeCost(self,start,end,c):
        """modifies the cost of an edge
        precondition: (x,y) needs to be a valid edge in the graph"""
        if (start,end) in self.__dictCosts: 
            self.__dictCosts[(start,end)] = c 
        else: 
            raise myException("No such edge")
        
    def floydWarshall(self):
        INFINITY = math.inf
        vertices = self.getNumberOfVertices()
        
        """initialize the distances matrix with infinity on every position
           and the path matrix with -1 on every position"""
        distances = [[INFINITY] * vertices for i in range(vertices)]
        paths = [[-1]*vertices for i in range(vertices)]
        
        """initialize the (i,i) distances with 0
           and the intersection (i,i) with i"""
        for i in range(vertices):
            distances[i][i]=0
            paths[i][i] = i
            
        """add the corresponding costs to the matrix"""
        for (x,y) in self.__dictCosts:
            distances[x][y] = self.retrieveCost(x, y)
            paths[x][y] = y
        
        """construct the floyd-warshall distances matrix and also the path matrix"""
        for k in range(vertices): 
            for i in range(vertices):
                for j in range(vertices):
                    if distances[i][k] + distances[k][j] < distances[i][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
                        paths[i][j] = paths[i][k]
                        
        """return the two matrices"""
        
        return distances[:],paths[:]
    
    
    