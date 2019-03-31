from DirectedGraph import DirectedGraph
from ProgramException import myException

class Console():
    
    def __init__(self,fileName):
        
        self.__fileName = fileName 
        self.__commands = {"1":self.__loadFromFile, "2":self.__floydWarshall,"3":self.__printLowestCostWalk}
        
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
       
    def __floydWarshall(self):
        self.__floydWarshallMatrix = self.__graph.floydWarshall()
        
    def __printLowestCostWalk(self):
        print("start vertex:")
        x = int(input())
        print("end vertex:")
        y = int(input())
        if x==y:
            print("Cost from a vertex to itself is always 0")
        elif self.__floydWarshallMatrix[x][y] == 99999: 
            print("No possible walk from x to y.")
        else: 
            print(self.__floydWarshallMatrix[x][y])
            
    def run(self):
        while True: 
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
        
        
c = Console("graph.txt")
c.run()