from ProgramException import myException
import copy

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
        return copy.deepcopy(self.__dictOut.keys())
    
    def parseIterableOut(self,x):
        """returns a copy of all out neighbours of x"""
        return copy.deepcopy(self.__dictOut[x])
    
    def parseIterableIn(self,x):
        """return a copy of all in neighbours of x"""
        return copy.deepcopy(self.__dictIn[x])
    
    def isEdge(self,start,end):
        """Returns True if there is an edge from x to y, False otherwise"""
        try:
            return end in self.__dictOut[start]
        except KeyError: 
            raise myException("No such pair of vertices in the graph.")
        
    def addEdge(self,start,end,cost):
        """adds an edge (start,end) that has that cost to the graph
           precondition: the edge mustn't already exist and the vertices need to be valid
                         in case it doesn't exist or the vertices aren't valid the error is handled and the user is informed"""
        exception = ""
        if start not in self.parseKeys(): 
            exception += "The vertex " + str(start) + " doesn't exist;"
        if end not in self.parseKeys():
            exception += "The vertex " + str(end) + " doesn't exist;"
        if self.isEdge(start,end):
            exception += "Already an edge;" 
        if len(exception):
            raise myException(exception)
        
        self.__dictOut[start].append(end)
        self.__dictIn[end].append(start)
        self.__dictCosts[(start,end)] = cost

    def addVertex(self,x):
        """adds the vertex x to the graph, as an isolated vertex
            precondition: x mustn't already be a vertex in the graph
                         if it is, the errors is handled and the user is informed"""
        if x in self.parseKeys():
            raise myException("Already existing vertex")
        self.__dictOut[x] = []
        self.__dictIn[x] = []
    
    def __removeEdgesContainingX(self,x):
        """just a helper function"""
        while True: 
            ok = False
            for edges in self.__dictCosts:
                if edges[0] == x or edges[1] == x:
                    del self.__dictCosts[edges]
                    ok = True
                    break 
            if not ok: 
                return
            
    def removeVertex(self,x):
        """removes the vertex x from the graph
           precondition: x needs to exist in the graph as a vertex
                         if it doesn't, the error is handled and the user is informed """
        if x not in self.parseKeys():
            raise myException("Vertex doesn't exist")
        del self.__dictOut[x]
        del self.__dictIn[x]
        self.__removeEdgesContainingX(x)
            
    def removeEdge(self,x,y):
        """removes the edge (x,y) from the graph
            precondition: (x,y) needs to be a valid edge in the graph
                           if it isn't, the error is handled and the user is informed """
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
           precondition: x needs to be a valid vertex in the graph 
                         in case it isn't, the error is handled and the user is informed"""
        try:
            return len(self.__dictIn[x])
        except KeyError:
            raise myException("No such vertex")

    def modifyEdgeCost(self,x,y,c):
        """modifies the cost of an edge
        precondition: (x,y) needs to be a valid edge in the graph
                      if it isn't, the error is handled and the user is informed"""
        if (x,y) in self.__dictCosts: 
            self.__dictCosts[(x,y)] = c 
        else: 
            raise myException("No such edge")
        
    def copyGraph(self):
        """returns a copy of the graph"""
        newGraph = DirectedGraph(10)
        newGraph.__dictIn = copy.deepcopy(self.__dictIn)
        newGraph.__dictOut = copy.deepcopy(self.__dictOut)
        newGraph.__dictCosts = copy.deepcopy(self.__dictCosts)
        return newGraph
    
    def edges(self):
        """return an iterable containing all the edges"""
        edgesList = []
        for edges in self.__dictCosts: 
            edgesList.append(edges)
        return edgesList[:]
        
