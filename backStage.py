import heapq

# this function convert all path that available for string to dictionary
def load_routes(routes, symmetric=True):
  def insert(frm,to,cost):
    if frm in G:
      G[frm][to]=cost
    else:
      G[frm] = {to:cost}
  G = {}
  routes = routes.splitlines()
  for route in routes:
    r = route.split('&')
    insert(r[0],r[1],int(r[2]))
    if symmetric:
      insert(r[1],r[0],int(r[2]))
  return G


debug = True

#this function defind type of dictionary
def ordered_set(coll):
  return dict.fromkeys(coll).keys()

#this class responsible of data in usc
#we use it to endle the data and sort it by the cost value
class PriorityQueue:
    # constructor
    def __init__(self, f=lambda x: x):
      self.heap = []
      self.f = f

    # push new node to heap
    def append(self, item):
      heapq.heappush(self.heap, (self.f(item), item))

    # add all the sons
    def extend(self, items):
      for item in items:
        self.append(item)

    # this function pop new node and sort the heap by cost but keep the inset order
    def pop(self):
      if self.heap:
        heao_list = []
        cost = 0
        while len(heao_list) < len(self.heap):
          for n in self.heap:
            if n[0] == cost:
              heao_list.append(n)
          cost += 1
        self.heap = heao_list[1:]
        return heao_list[0][1]
      else:
        raise Exception('Trying to pop from empty PriorityQueue.')

    # return the length of heap
    def __len__(self):
      return len(self.heap)

    # return if the key exist
    def __contains__(self, key):
      return any([item == key for _, item in self.heap])

    # return value of key
    def __getitem__(self, key):
      for value, item in self.heap:
        if item == key:
          return value
      raise KeyError(str(key) + " is not in the priority queue")

    # delete value of key
    def __delitem__(self, key):
      try:
        del self.heap[[item == key for _, item in self.heap].index(True)]
      except ValueError:
        raise KeyError(str(key) + " is not in the priority queue")
      heapq.heapify(self.heap)

    # return string of heap
    def __repr__(self):
      return str(self.heap)

# this class responsible of nodes and the behavior of them
# its consist all the relevant function of node in the problem
class Node:
  # constructor
  def __init__(self, state, parent=None, action=None, path_cost=0):
    self.state = state
    self.parent = parent
    self.action = action
    self.path_cost = path_cost
    self.depth = 0
    if parent:
      self.depth = parent.depth + 1

  # do list with all nodes sucssesor
  def expand(self, problem, reverse=False):
    if not reverse:
      return ordered_set([self.child_node(problem, action)
                        for action in problem.actions(self.state)])
    else:
      return ordered_set([self.child_node(problem, action)
                          for action in reversed(list(problem.actions(self.state)))])

  # defind sons of node
  def child_node(self, problem, action):
    next_state = problem.succ(self.state, action)
    next_node = Node(next_state, self, action,
                     self.path_cost + problem.step_cost(self.state, action))
    return next_node

  # opperate action for node
  def solution(self):
    return [node.action for node in self.path()[1:]]

  # return the path of nodes in list
  def path(self):
    node, path_back = self, []
    while node:
      path_back.append(node)
      node = node.parent
    return list(reversed(path_back))

  # print as string
  def __repr__(self):
    return f"<{self.state}>"

  # compare between two nodes
  def __lt__(self, node):
    return self.state < node.state

  # compare between two states
  def __eq__(self, other):
    return isinstance(other, Node) and self.state == other.state

  # check equal between two nodes
  def __ne__(self, other):
    return not (self == other)

  # give the hash of nodes
  def __hash__(self):
    return hash(self.state)
