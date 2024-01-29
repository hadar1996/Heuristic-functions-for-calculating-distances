from algSearch import uniform_cost_search, iterative_deepening_search, astar_search, idaStar
from problem import Problem

file = open("input.txt", "r")
counter = 0
for i in file:
    counter += 1
file.close()
file = open("input.txt", "r")
Arr = []
for i in range(counter):
    Arr.append(file.readline().rstrip())
file.close()
pro = Problem(Arr)

#Calculate max distance between x-distance and y-distance
def h(node):
    xnode = node.state.split(',')[0][1]
    #print(xnode)
    ynode = node.state.split(',')[1][1]
    #print(ynode)
    xgoal = Arr[2].split(',')[0]
    #print(xgoal)
    ygoal = Arr[2].split(',')[1]
    #print(ygoal)
    diffx = abs(int(xnode) - int(xgoal))
    diffy = abs(int(ynode) - int(ygoal))
    h = max(diffx, diffy)
    return h

# choose algorithm by input
if Arr[0] == str("UCS"):
    result, log, counter, cost = uniform_cost_search(pro)
elif Arr[0] == str("IDS"):
    result, log, counter, cost = iterative_deepening_search(pro)
elif Arr[0] == str("IDASTAR"):
    result, log, counter, cost = idaStar(pro, h)
elif Arr[0] == str("ASTAR"):
    result, log, counter, cost = astar_search(pro, h)
#print(result, counter, cost)

#path of output
path = ""
if result == None:
    path = "no path"
else:
    for i in range(len(result)):
        if i == 0:
          Xold = int(Arr[1][0])
          Yold = int(Arr[1][2])
        else:
          Xold = int(result[i-1][1])
          Yold = int(result[i-1][4])
        Xnew = int(result[i][1])
        Ynew = int(result[i][4])

        Xval = Xnew - Xold
        Yval = Ynew - Yold

        if Xval == 1 and Yval == 0:
            path = path + "-D"
        if Xval == 0 and Yval == 1:
            path = path + "-R"
        if Xval == 1 and Yval == 1:
            path = path + "-RD"
        if Xval == -1 and Yval == -1:
            path = path + "-LU"
        if Xval == -1 and Yval == 0:
            path = path + "-U"
        if Xval == -1 and Yval == 1:
            path = path + "-RU"
        if Xval == 0 and Yval == -1:
            path = path + "-L"
        if Xval == 1 and Yval == -1:
            path = path + "-LD"


    path = path[1:] + " " + str(cost) + " " + str(counter)
print(path)
#create new file
f = open("output.txt", "w")
f.write(path)
f.close()

