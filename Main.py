from Graph import Graph
from collections import deque
import sys
import time

start = time.clock() # Start timer

def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    minNode = None
    for node in nodes:
      if node in visited:
        if minNode is None:
          minNode = node
        elif visited[node] < visited[minNode]:
          minNode = node

    if minNode is None:
      break

    nodes.remove(minNode)
    currentWeight = visited[minNode]

    for edge in graph.edges[minNode]:
      weight = currentWeight + graph.distances[(minNode, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = minNode

  return  visited,path #[0] visited [1] path

def initializeGraph():
    graph = Graph()
    graph.add_node("Arad")
    graph.add_edge("Arad","Sibiu",140)
    graph.add_edge("Arad","Timisoara",118)
    graph.add_edge("Arad","Zerind",75)

    graph.add_node("Bucharest")
    graph.add_edge("Bucharest","Fagaras",211)
    graph.add_edge("Bucharest","Giurgiu",90)
    graph.add_edge("Bucharest","Pitesti",101)
    graph.add_edge("Bucharest","Urziceni",85)

    graph.add_node("Craiova")
    graph.add_edge("Craiova","Drobeta",120)
    graph.add_edge("Craiova","Pitesti",138)
    graph.add_edge("Craiova","Rimnicu Vileea",146)

    graph.add_node("Drobeta")
    graph.add_edge("Drobeta","Craiova",120)
    graph.add_edge("Drobeta","Mehadia",75)

    graph.add_node("Eforie")
    graph.add_edge("Eforie","Hirsova",86)

    graph.add_node("Fagaras")
    graph.add_edge("Fagaras","Bucharest",211)
    graph.add_edge("Fagaras","Sibiu",99)

    graph.add_node("Giurgiu")
    graph.add_edge("Giurgiu","Bucharest",90)

    graph.add_node("Hirsova")
    graph.add_edge("Hirsova","Eforie",86)
    graph.add_edge("Hirsova","Urziceni",98)

    graph.add_node("Iasi")
    graph.add_edge("Iasi","Neamt",87)
    graph.add_edge("Iasi","Vaslui",92)

    graph.add_node("Lugoj")
    graph.add_edge("Lugoj","Mehadia",70)
    graph.add_edge("Lugoj","Timisoara",111)

    graph.add_node("Mehadia")
    graph.add_edge("Mehadia","Drobeta",75)
    graph.add_edge("Mehadia","Lugoj",70)

    graph.add_node("Neamt")
    graph.add_edge("Neamt","Iasi",87)

    graph.add_node("Oradea")
    graph.add_edge("Oradea","Sibiu",151)
    graph.add_edge("Oradea","Zerind",71)

    graph.add_node("Pitesti")
    graph.add_edge("Pitesti","Bucharest",101)
    graph.add_edge("Pitesti","Craiova",138)
    graph.add_edge("Pitesti","Rimnicu Vileea",97)

    graph.add_node("Rimnicu Vileea")
    graph.add_edge("Rimnicu Vileea","Craiova",146)
    graph.add_edge("Rimnicu Vileea","Pitesti",97)
    graph.add_edge("Rimnicu Vileea","Sibiu",80)

    graph.add_node("Sibiu")
    graph.add_edge("Sibiu","Arad",140)
    graph.add_edge("Sibiu","Fagaras",99)
    graph.add_edge("Sibiu","Oradea",151)
    graph.add_edge("Sibiu","Rimnicu Vileea",80)

    graph.add_node("Timisoara")
    graph.add_edge("Timisoara","Arad",118)
    graph.add_edge("Timisoara","Lugoj",111)

    graph.add_node("Urziceni")
    graph.add_edge("Urziceni","Bucharest",85)
    graph.add_edge("Urziceni","Hirsova",98)
    graph.add_edge("Urziceni","Vaslui",142)

    graph.add_node("Vaslui")
    graph.add_edge("Vaslui","Iasi",92)
    graph.add_edge("Vaslui","Urziceni",142)

    graph.add_node("Zerind")
    graph.add_edge("Zerind","Arad",75)
    graph.add_edge("Zerind","Oradea",71)

    return graph

def shortestPath(graph, origin, destination):
    visited, paths = dijsktra(graph, origin)
    fullPath = deque()
    _destination = paths[destination]

    while _destination != origin:
        fullPath.appendleft(_destination)
        _destination = paths[_destination]

    fullPath.appendleft(origin)
    fullPath.append(destination)

    return visited[destination], list(fullPath)

def detectClosestCity(currentLocation,container):
    distanceArray = []

    for i in range(len(container)):
        try:
            x = container[i]
            distanceArray.append(shortestPath(graph=graph,origin=currentLocation,destination=x))
        except KeyError:
            pass
    try:
        return min(distanceArray)
    except ValueError:
        print("Cities don't have enough items for collect.")
        sys.exit(1)

def totalDistance(pathlog):
    sum = 0
    for i in range(len(pathLog)):
        sum += pathLog[i][0]
    return sum

if __name__ == '__main__':
    graph = initializeGraph()
    startLocation = "Neamt"
    currentLocation = "Neamt"
    shopDict = {"A":10,"B":20,"C":10} # Note for Mr Kutluhan Erol : Please only modify here if you want to test other things
    pathLog = [] # Shows full path
    for element in shopDict.keys(): # element is A -> B -> C
        while shopDict[element] is not 0:
            if "A" in element:
                detected = detectClosestCity(currentLocation,graph.cityContainA) #Ex: (910, ['Neamt', 'Iasi', 'Vaslui', 'Urziceni', 'Bucharest', 'Pitesti', 'Craiova', 'Drobeta', 'Mehadia', 'Lugoj'])
                detectedCity = list(detected)[1][-1]
                if graph.inventoryA[detectedCity] >= shopDict["A"]:
                    graph.inventoryA[detectedCity] -= shopDict["A"]
                    shopDict["A"] = 0
                    currentLocation = detectedCity
                    graph.cityContainA.remove(currentLocation)
                    pathLog.append(detected)
                    print("Big A: "+str(currentLocation))
                    print(shopDict)
                else:
                    shopDict["A"] -= graph.inventoryA[detectedCity]
                    graph.inventoryA[detectedCity] = 0
                    currentLocation = detectedCity
                    graph.cityContainA.remove(currentLocation)
                    pathLog.append(detected)
                    print("Small A:"+str(currentLocation))
                    print(shopDict)
            if "B" in element:
                detected = detectClosestCity(currentLocation,graph.cityContainB)
                detectedCity = list(detected)[1][-1]
                if graph.inventoryB[detectedCity] >= shopDict["B"]:
                    graph.inventoryB[detectedCity] -= shopDict["B"]
                    shopDict["B"] = 0
                    currentLocation = detectedCity
                    graph.cityContainB.remove(currentLocation)
                    pathLog.append(detected)
                    print("Big B: "+str(currentLocation))
                    print(shopDict)
                else:
                    shopDict["B"] -= graph.inventoryB[detectedCity]
                    graph.inventoryB[detectedCity] = 0
                    currentLocation = detectedCity
                    graph.cityContainB.remove(currentLocation)
                    pathLog.append(detected)
                    print("Small B: "+str(currentLocation))
                    print(shopDict)

            if "C" in element:
                detected = detectClosestCity(currentLocation,graph.cityContainC)
                detectedCity = list(detected)[1][-1]
                if graph.inventoryC[detectedCity] >= shopDict["C"]:
                    graph.inventoryC[detectedCity] -= shopDict["C"]
                    shopDict["C"] = 0
                    currentLocation = detectedCity
                    graph.cityContainC.remove(currentLocation)
                    pathLog.append(detected)
                    print("Big C: "+str(currentLocation))
                    print(shopDict)
                else:
                    shopDict["C"] -= graph.inventoryC[detectedCity]
                    graph.inventoryC[detectedCity] = 0
                    currentLocation = detectedCity
                    graph.cityContainC.remove(currentLocation)
                    pathLog.append(detected)
                    print("Small C: "+str(currentLocation))
                    print(shopDict)
pathLog.append(shortestPath(graph,pathLog[-1][1][-1],"Neamt"))
print("-----------------------------FULL PATH-----------------------------")
print(pathLog)
print("Total distance: "+str(totalDistance(pathLog)))
#print(dijsktra(graph,"Neamt")[0])
end = time.clock() # finish timer
print("Complite Time: "+str(end-start))
#print(dijsktra(graph,"Hirsova")[0])
