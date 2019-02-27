
class DirectedGraph(object):
    
    
    def __init__(self,vertices):
        
        self.__dictIn = {}
        
        self.__dictOut = {}
        
        self.__dictCosts = {}

        for i in range(vertices):
            self.__dictOut[i]=[]
            self.__dictIn[i] = []
    
    def parseKeys(self):
        """return all the vertex keys"""
        return list(self.__dictOut.keys())
    
    def parseIterableOut(self,x):
        """return all out neighbours of x"""
        return list(self.__dictOut[x])
    
    def parseIterableIn(self,x):
        """return all in neighbours of x"""
        return list(self.__dictIn[x])
    
    def isEdge(self,start,end):
        """Returns True if there is an edge from x to y, False otherwise"""
        return end in self.__dictOut[start]

    def addEdge(self,start,end,cost):
        exception = ""
        if start not in self.parseKeys(): 
            exception += "The point " + str(start) + " doesn't exist;"
        if end not in self.parseKeys():
            exception += "The point " + str(end) + " doesn't exist;"
        if self.isEdge(start,end):
            exception += "Already an edge" 
        if len(exception):
            raise Exception(exception)
        
        self.__dictOut[start].append(end)
        self.__dictIn[end].append(start)
        self.__dictCosts[(start,end)] = cost

    def addVertex(self,x):
        if x in self.parseKeys():
            raise Exception("Already existing vertex")
        self.__dictOut.append(x)
        self.__dictOut[x] = []
        self.__dictIn.append(x)
        self.__dictIn[x] = []
        
    def getNumberOfVertices(self):
        """return an integer containing the number of vertices in the graph"""
        return len(self.parseKeys())

    
    def getOutDegree(self,x):
        """return an integer representing the out degree of the vertex x"""
        return len(self.__dictOut[x])
    
    def getInDegree(self,x):
        """return an integer representing the in degree of the vertex x"""
        return len(self.__dictIn[x])
    
    
    
    
    
    
