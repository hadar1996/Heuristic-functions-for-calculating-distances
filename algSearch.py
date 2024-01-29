from backStage import Node, PriorityQueue, debug

#this function opperate BFS in the matrix
def best_first_graph_search(problem, f):
    counterPop = 0
    node = Node(problem.s_start)
    frontier = PriorityQueue(f) #Priority Queue
    frontier.append(node)
    log = []
    closed_list = set()
    while frontier:
        node = frontier.pop()
        #print(node, ": ", frontier)
        if debug:
            log.append((problem.state_str(node.state), node.solution(), node.path_cost,f(node),str(frontier), problem.actions(node.state), problem.is_goal(node.state)))
        if problem.is_goal(node.state):
            return node.solution(), log, counterPop, node.path_cost
        counterPop += 1
        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier:
                frontier.append(child)
            elif child in frontier and f(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)
        #print(node, ": ", frontier)
    return None, log, counterPop, None

#f = g:
#this function return the cost of path
def uniform_cost_search(problem):
    def g(node):
        return node.path_cost
    return best_first_graph_search(problem, f=g)

#this function DFS who limited by depth
def depth_limited_search(problem, limit=5):
    counerPop = 0
    frontier = [(Node(problem.s_start))]  # Stack
    log = []
    while frontier:
        node = frontier.pop()
        #print(node, ": ", frontier)
        counerPop += 1
        if debug:
          log.append((problem.state_str(node.state),node.solution(),len(frontier),problem.actions(node.state),problem.is_goal(node.state)))
        if problem.is_goal(node.state):
          return node.solution(), log, counerPop, node.path_cost
        if node.depth<limit:
          frontier.extend(node.expand(problem, True))
        #print(node, ": ", frontier)
    return None, log, counerPop, None

#this function run the DFS by +1 depth each iterative
def iterative_deepening_search(problem):
    iterative_log = []
    sumCounter = 0
    for depth in range(1, 20):
        result, log, counter, cost = depth_limited_search(problem, depth)
        iterative_log.extend(log)
        sumCounter += counter
        if result:
            return result, iterative_log, sumCounter, cost
    return None, iterative_deepening_search, None, None

#this function run BFS by cost and hyuristic function
def astar_search(problem, h):
  def g(node):
    return node.path_cost
  return best_first_graph_search(problem, f=lambda n: g(n)+h(n))

#this function DFS who limited by f value
def depth_limited_search_by_value(problem, limit, f):
    frontier = [(Node(problem.s_start))]  # Stack
    log = []
    counter = 0
    while frontier:
        node = frontier.pop()
        counter += 1
        if debug:
          log.append((problem.state_str(node.state),node.solution(),len(frontier),problem.actions(node.state),problem.is_goal(node.state)))
        if problem.is_goal(node.state):
          return node.solution(), log, counter, node.path_cost
        if f(node)<limit and node.depth < 20:
          frontier.extend(node.expand(problem, True))
    return None, log, counter, None

#this function run the DFS by new minimal f limit each iterative
def idaStar(problem, h):
  def g(node):
    return node.path_cost
  sumCounter = 0
  iterative_log = []
  for depth in range(1, 20):
    #print(depth)
    result, log, counter, cost = depth_limited_search_by_value(problem, depth, f=lambda n: g(n)+h(n))
    sumCounter += counter
    iterative_log.extend(log)
    if result:
      return result, iterative_log, sumCounter, cost
  return None, iterative_deepening_search, None, None

