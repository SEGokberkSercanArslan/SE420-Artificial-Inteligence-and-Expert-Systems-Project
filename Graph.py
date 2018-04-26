from collections import defaultdict
from Item import Item

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}
    self.cityContainA = ["Lugoj",10]
    self.cityContainB = ["Arad",1, "Bucharest", 1, "Craiova", 1, "Drobeta", 1, "Eforie", 1, "Fagaras", 1,
                         "Giurgiu", 1, "Hirsova", 1, "Iasi", 1, "Lugoj", 1, "Mehadia", 1, "Neamt", 1,
                         "Oradea", 1, "Pitesti", 1, "Rimnicu Vileea", 1, "Sibiu", 1, "Timisoara", 1,
                         "Urziceni", 1, "Vaslui", 1, "Zerind", 1]
    self.cityContainC = ["Lugoj", 5, "Arad", 5, "Oradea", 5]

    self.inventoryA = {"Lugoj":10}
    self.inventoryB = {"Arad":1, "Bucharest":1, "Craiova":1, "Drobeta":1, "Eforie":1, "Fagaras":1,
                         "Giurgiu":1, "Hirsova":1, "Iasi":1, "Lugoj":1, "Mehadia":1, "Neamt":1,
                         "Oradea":1, "Pitesti":1, "Rimnicu Vileea":1, "Sibiu":1, "Timisoara":1,
                         "Urziceni":1, "Vaslui":1, "Zerind":1}
    self.inventoryC = {"Lugoj": 5, "Arad": 5, "Oradea":5}


  def add_node(self,value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
