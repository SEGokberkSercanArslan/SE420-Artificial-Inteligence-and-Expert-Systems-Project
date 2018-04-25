from collections import defaultdict
from Item import Item

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}
    self.itemCounter = {}
    self.cityContainA = []
    self.cityContainB = []
    self.cityContainC = []

  def add_node(self,value,*sets):
    self.nodes.add(value)
    print(sets)
    #for i in sets:
    #  self.itemCounter[sets[i][0]] += sets.get(i,0) + sets[i][1]


  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
