from Graph import Graph
from collections import deque
from Item import Item

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




if __name__ == '__main__':
    graph = initializeGraph()
    var = shortest_path(graph,"Zerind","Timisoara")
    var2= shortest_path(graph,"Zerind","Fagaras")
    top = []
    top.append(var)
    top.append(var2)
    print(top)
    print(min(top))
