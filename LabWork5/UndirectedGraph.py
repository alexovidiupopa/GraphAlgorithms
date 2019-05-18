from myException import myException

class UndirectedGraph:
    
    def __init__(self,vertices):
        self.__dictEdges = {}
        for i in range(0,vertices):
            self.__dictEdges[i]=[]
  
    def addEdge(self,x,y):
        if x not in self.__dictEdges[y] and y not in self.__dictEdges[x]:
            self.__dictEdges[x].append(y)
            self.__dictEdges[y].append(x)
        else: 
            raise myException("edge already exists")
    
    def addVertex(self,x):
        if x in self.__dictEdges:
            raise myException("vertex already exists")
        self.__dictEdges[x] = []
        
    def parseNeighbours(self,x):
        return self.__dictEdges[x]
    
    def parseKeys(self):
        return list(self.__dictEdges.keys())
    
    def vertexCover(self):
        pass
    
    def printSubgraphs(self):
        for sg in self.__subgraphs:
            print(sg.parseKeys())
            