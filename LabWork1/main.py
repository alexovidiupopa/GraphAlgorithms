from DirectedGraph import DirectedGraph
from utils import printMenu
class Console():
    def __init__(self,fileName):
        self.__fileName = fileName 
        self.__commands = {"0":self.__loadFromFile,"1":self.__getNumberOfVertices,
                           "2":self.__printAllVertices,"3":self.__edgeFromXToY,
                           "4":self.__getDegrees,"5":self.__modifyCost}
    def __loadFromFile(self):
        try:
            with open(self.__fileName,"r") as file:
                firstLine = file.readline()
                firstLine = firstLine.strip().split()
                vertices,edges = int(firstLine[0]),int(firstLine[1])
                self.__graph = DirectedGraph(vertices)
                for i in range(edges): 
                    line = file.readline()
                    line = line.strip().split()
                    start,end,cost = int(line[0]),int(line[1]),int(line[2])
                    self.__graph.addEdge(start, end, cost)
        except IOError:
            raise Exception("File Reading Error")
        
    def __getNumberOfVertices(self):
        print(self.__graph.getNumberOfVertices())
    
    def __printAllVertices(self):
        print(self.__graph.parseKeys())
        
    def __edgeFromXToY(self):
        print("Give vertices x and y:")
        x = int(input())
        y = int(input())
        result = {True:"Yes",False:"No"}
        print(result[self.__graph.isEdge(x, y)])
        
    def __getDegrees(self):
        print("Give vertex:")
        x = int(input())
        print("Out degree: " + str(self.__graph.getOutDegree(x)))
        print("In degree: " + str(self.__graph.getInDegree(x)))
        
    def __modifyCost(self):
        print("Give edge start:")
        x = int(input())
        print("Give edge end:")
        y = int(input())
        print("Give new cost:")
        cost = int(input())
        self.__graph.modifyEdgeCost(x,y,cost)
        
    def run(self):
        while True: 
            print(">>")
            printMenu()
            cmd = input()
            if cmd == "9": 
                return
            elif cmd in self.__commands: 
                    self.__commands[cmd]()
                
            else: 
                print("Wrong cmd")
c = Console("graph.txt")
c.run()