from UndirectedGraph import UndirectedGraph
from myException import myException

class Console:
    
    def __init__(self):
        self.__fileName = "graph.txt"
        self.__options={"1":self.__loadGraph, "2":self.__connectedComponentsWithDFS
            }
    
    def __printMenu(self):    
        print("Options: ")
        print("1-load graph")
        print("2-print the connected components with dfs")
        print("exit")
    
    def __loadGraph(self):
        try:
            with open(self.__fileName,"r") as file:
                firstLine = file.readline()
                firstLine = firstLine.strip().split()
                vertices,edges = int(firstLine[0]),int(firstLine[1])
                self.__graph = UndirectedGraph(vertices)
                for times in range(edges): 
                    line = file.readline()
                    line = line.strip().split()
                    start,end,cost = int(line[0]),int(line[1]),int(line[2])
                    self.__graph.addEdge(start, end)
            print("Graph loaded.")
        except IOError:
            raise myException("File Reading Error")
            
    def __connectedComponentsWithDFS(self):
        pass    
    
    def main(self):
        print(">>")
        while True:
            cmd = input()
            
            if cmd == exit:
                return 
            elif cmd in self.__options:
                self.__options[cmd]()
        pass