from myException import myException
from random import choice
class UndirectedGraph:
    
    def __init__(self,vertices):
        self.__dictEdges = {}
        for i in range(0,vertices):
            self.__dictEdges[i]=[]
        self.__E=[]
  
    def addEdge(self,x,y):
        if x not in self.__dictEdges[y] and y not in self.__dictEdges[x]:
            self.__dictEdges[x].append(y)
            self.__dictEdges[y].append(x)
            self.__E.append((x,y))
            self.__E.append((y,x))
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
    
    def getDegree(self,vertex):
        try:
            a=len(self.__dictEdges[vertex])
            b=0
            for i in self.__dictEdges:
                if i!=vertex and vertex in self.__dictEdges[i]:
                    b+=1
            return a+b
        except KeyError:
            raise myException("vertex doesn't exist")
        
    def getMaxDegreeVertex(self):
        max = -1
        vertex=-1
        for i in self.parseKeys():
            if self.getDegree(i)>max:
                max=self.getDegree(i)
                vertex=i
        return vertex
    
    def approximateVertexCover(self):
        result=set()
        while self.__E!=[]:
            #choose random (u,v) edge
            (u,v) = choice(self.__E)
            
            #add u and v to the result set, if they aren't already in there
            if u not in result:
                result.add(u)
            if v not in result:
                result.add(v)
                
            #delete all the edges having as endpoints u or v
            
            ok=True
            while ok:
                ok=False
                for i in range(len(self.__E)):
                    if self.__E[i][0]==u or self.__E[i][1]==u or self.__E[i][0]==v or self.__E[i][1]==v:
                        del self.__E[i]
                        ok = True 
                        break
        
        return result
    
    
    def greedyVertexCover(self):
        solution = set()
        while self.__dictEdges!={}:
            v = self.getMaxDegreeVertex()
            if self.getDegree(v)==0:
                break
            solution.add(v)
            del self.__dictEdges[v]
            ok=True
            while ok:
                ok=False
                for x in self.__dictEdges:
                    if v in self.__dictEdges[x]:
                        self.__dictEdges[x].remove(v)
                        ok = True 
                        break
        return solution
    
    
    def printSubgraphs(self):
        for sg in self.__subgraphs:
            print(sg.parseKeys())
            