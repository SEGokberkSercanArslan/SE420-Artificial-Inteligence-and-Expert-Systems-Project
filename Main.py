from Graph import Graph
from collections import deque

def dijsktra(graph, initial):  # initial baslangic nodu
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

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

def shortest_path(graph, origin, destination):
    visited, paths = dijsktra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

def detectClosestCity(currentLocation,container):
    distanceArray = []
    for i in range(len(container)):
        try:
            x = container[i*2]
            distanceArray.append(shortest_path(graph=graph,origin=currentLocation,destination=x))
        except IndexError:
            pass
        except KeyError:
            pass
    print(min(distanceArray))

if __name__ == '__main__':
    graph = initializeGraph()
    startLocation = "Neamt"
    currentLocation = "Neamt"
    shopDict = {"A":10,"B":5}
    moveNext = False
    total = 0
    for key in shopDict.keys():
        total += shopDict[key]
    pathLog = [] # Shows full path


    # Note, After while loop draw a path current node -> start Node
    # Add path to pathLog

    while total is not 0:
        for element in shopDict.keys(): # element is A -> B -> C
            #Start location icin de buraya bir if case i ac
            while shopDict[element] is not 0:
                if currentLocation is startLocation and moveNext is False:
                    if element is "A" and currentLocation in graph.cityContainA:
                        moveNext = True
                        pass
                    elif element is "B" and currentLocation in graph.cityContainB:
                        moveNext = True
                        pass
                    elif element is "C" and currentLocation in graph.cityContainC:
                        moveNext = True
                        pass
                if "A" in element:
                    detected = detectClosestCity(currentLocation,graph.cityContainA) # (910, ['Neamt', 'Iasi', 'Vaslui', 'Urziceni', 'Bucharest', 'Pitesti', 'Craiova', 'Drobeta', 'Mehadia', 'Lugoj'])
                    if graph.inventoryA[detected[0][-1]] > shopDict["A"]:
                        pass
                    else:
                        pass

                if "B" in element:                                        # Test Output
                    detected = detectClosestCity(currentLocation,graph.cityContainB)
                    if graph.inventoryA[detected[0][-1]] > shopDict["A"]:
                        pass
                    else:
                        pass

                if "C" in element:
                    detected = detectClosestCity(currentLocation,graph.cityContainC)
                    if graph.inventoryA[detected[0][-1]] > shopDict["A"]:
                        pass
                    else:
                        pass
