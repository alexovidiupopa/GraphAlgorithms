from DirectedGraph import DirectedGraph
from ProgramException import myException
import math
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
        self.__floydWarshallMatrix,self.__floydWarshallPaths = self.__graph.floydWarshall()
        for i in range(len(self.__graph.parseKeys())):
            print(self.__floydWarshallMatrix[i])
        for i in range(len(self.__graph.parseKeys())):
            print(self.__floydWarshallPaths[i])
        print("Floyd-Warshall matrix computed.")
        
    def __printLowestCostWalk(self):
        print("start vertex:")
        start = int(input())
        print("end vertex:")
        end = int(input())
        if start not in self.__graph.parseKeys() or end not in self.__graph.parseKeys():
            print("No such vertices")
            return
        if start==end:
            print("Cost from a vertex to itself is always 0")
        elif self.__floydWarshallMatrix[start][end] == math.inf: 
            print("No possible walk from start to end.")
        else: 
            """Print the cost"""
            print("Cost:",end='')
            print(self.__floydWarshallMatrix[start][end])
            
            print("Path:",end='')
            """Reconstruct the path"""
            
            path = [start]
            while start!=end:
                start = self.__floydWarshallPaths[start][end]
                path.append(start)
            print(path)
            
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