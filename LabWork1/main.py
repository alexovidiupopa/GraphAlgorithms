from DirectedGraph import DirectedGraph
from utils import printMenu
from ProgramException import myException
from RandomGraphGenerator import RandomGraphGenerator

class Console():
        
    def __init__(self,fileName):
        self.__fileName = fileName 
        self.__commands = {"0":self.__loadFromFile,"1":self.__getNumberOfVertices,
                           "2":self.__printAllVertices,"3":self.__edgeFromXToY,
                           "4":self.__getDegrees,"5":self.__modifyCost,
                           "6":self.__addVertex, "7":self.__addEdge,
                           "8":self.__removeVertex,"9":self.__removeEdge,
                           "10":self.__copyGraph,"11":self.__printGraph,"12":self.__printGraphCopy,"13":self.__parseOut,
                           "14":self.__isolatedVertices}
    def __loadFromFile(self):
        try:
            with open(self.__fileName,"r") as file:
                firstLine = file.readline()
                firstLine = firstLine.strip().split()
                vertices,edges = int(firstLine[0]),int(firstLine[1])
                self.__graph = DirectedGraph(vertices)
                for times in range(edges): 
                    line = file.readline()
                    line = line.strip().split()
                    start,end,cost = int(line[0]),int(line[1]),int(line[2])
                    self.__graph.addEdge(start, end, cost)
            print("Graph loaded.")
        except IOError:
            raise myException("File Reading Error")
        
    def __getNumberOfVertices(self):
        print(self.__graph.getNumberOfVertices())
    
    def __printAllVertices(self):
        print(self.__graph.parseKeys())
        
    def __edgeFromXToY(self):
        print("Give vertices x and y:")
        start = int(input())
        end = int(input())
        result = {True:"Yes",False:"No"}
        print(result[self.__graph.isEdge(start, end)])
        
    def __getDegrees(self):
        print("Give vertex:")
        vertex = int(input())
        print("Out degree: " + str(self.__graph.getOutDegree(vertex)))
        print("In degree: " + str(self.__graph.getInDegree(vertex)))
        
    def __modifyCost(self):
        print("Give edge start:")
        start = int(input())
        print("Give edge end:")
        end = int(input())
        print(self.__graph.retrieveCost(start, end))
        print("Give new cost:")
        cost = int(input())
        self.__graph.modifyEdgeCost(start,end,cost)
        
    def __addVertex(self):
        print("Give new vertex:")
        vertex = int(input())
        self.__graph.addVertex(vertex)
    
    def __isolatedVertices(self):
        print(self.__graph.allIsolatedVertices())
        
    def __parseOut(self):
        print("Get vertex:")
        x = int(input())
        out = self.__graph.parseIterableOut(x)
        print(out)
        inZ = self.__graph.parseIterableIn(x)
        print(inZ)
    def __addEdge(self):
        print("Give edge start: ")
        start = int(input())
        print("Give edge end: ")
        end = int(input())
        print("Give edge cost: ")
        cost = int(input())
        self.__graph.addEdge(start, end, cost)
    
    def __removeEdge(self):
        print("Give edge start:")
        start = int(input())
        print("Give edge end:")
        end = int(input())
        self.__graph.removeEdge(start, end)
    
    def __removeVertex(self):
        print("Give vertex you want to remove:")
        vertex = int(input())
        self.__graph.removeVertex(vertex)
        
    def __copyGraph(self):
        print("Copying the graph...")
        self.__graphCopy = self.__graph.copyGraph()
        print("The graph is now copied and stored in __graphCopy")
        
    def __printGraphCopy(self):
        print(self.__graphCopy.parseKeys())
        print(self.__graphCopy.edges())
        
    def __printGraph(self):
        print("The vertices of the graph are: ")
        print(self.__graph.parseKeys())
        print("The edges of the graph are: ")
        print(self.__graph.edges())
        
    def run(self):
        while True: 
            printMenu()
            print(">>")
            cmd = input()
            if cmd == "end": 
                return
            elif cmd in self.__commands: 
                try:    
                    self.__commands[cmd]()
                except myException as e: 
                    print(e)
            else: 
                print("Wrong cmd")

c = Console("graph10k.txt")
c.run()