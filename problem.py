import json

from backStage import load_routes

#this class responsible of the defind the problem
#and defind the rules to solve the problem
class Problem:
    G = {}
    s_start = ""
    goal = ""

    #this function defind the new and the end of the path
    def __init__(self, ArrayInput):
        #print(ArrayInput[1])
        self.s_start = "[" + ArrayInput[1].split(',')[0] + ", " + ArrayInput[1].split(',')[1] + "]"
        self.goal = "[" + ArrayInput[2].split(',')[0] + ", " + ArrayInput[2].split(',')[1] + "]"
        self.createG(ArrayInput)

    #this function create the loyal steps by the rules
    def createG(self,ArrayInput):
        Matrix=[]
        for i in range(4,int(ArrayInput[3])+4):
            Matrix.append(ArrayInput[i].split(','))
        #print(Matrix)
        stringG = ""
        i = 0
        while i < int(ArrayInput[3]):
            j = 0
            while j < int(ArrayInput[3]):
                #print(i," ",j)
                srcP = [i, j]
                if j+1 < int(ArrayInput[3]) and int(Matrix[i][j+1]) >= 0:
                    desP = [i, j + 1]
                    stringG = stringG + str(srcP) + "&" + str(desP) + "&" + Matrix[i][j+1] + "\n"
                if i+1 < int(ArrayInput[3]) and j+1 < int(ArrayInput[3]) and int(Matrix[i+1][j+1]) >= 0 and int(Matrix[i+1][j]) >= 0 and int(Matrix[i][j+1]) >= 0:
                    desP = [i + 1, j + 1]
                    stringG = stringG + str(srcP) + "&" + str(desP) + "&" + Matrix[i + 1][j + 1] + "\n"
                if i+1 < int(ArrayInput[3]) and int(Matrix[i+1][j]) >= 0:
                    desP = [i + 1, j]
                    stringG = stringG + str(srcP) + "&" + str(desP) + "&" + Matrix[i+1][j] + "\n"
                if i+1 < int(ArrayInput[3]) and j-1 >= 0 and int(Matrix[i+1][j-1]) >= 0 and int(Matrix[i+1][j]) >= 0 and int(Matrix[i][j-1]) >= 0:
                    desP = [i + 1, j - 1]
                    stringG = stringG + str(srcP) + "&" + str(desP) + "&" + Matrix[i + 1][j - 1] + "\n"
                if j-1 >= 0 and int(Matrix[i][j-1]) >= 0:
                    desP = [i, j - 1]
                    stringG = stringG + str(srcP) + "&" + str(desP) + "&" + Matrix[i][j-1] + "\n"
                if i-1 >= 0 and j-1 >= 0 and int(Matrix[i-1][j-1]) >= 0 and int(Matrix[i][j-1]) >= 0 and int(Matrix[i-1][j]) >= 0:
                    desP = [i - 1, j - 1]
                    stringG = stringG + str(srcP) + "&" + str(desP) + "&" + Matrix[i - 1][j - 1] + "\n"
                if i-1 >= 0 and int(Matrix[i-1][j]) >= 0:
                    desP = [i - 1, j]
                    stringG = stringG + str(srcP) + "&" + str(desP) + "&" + Matrix[i-1][j] + "\n"
                if i-1 >= 0 and j+1 < int(ArrayInput[3]) and int(Matrix[i-1][j+1]) >= 0 and int(Matrix[i-1][j]) >= 0 and int(Matrix[i][j+1]) >= 0:
                    desP = [i - 1, j + 1]
                    stringG = stringG + str(srcP) + "&" + str(desP) + "&" + Matrix[i - 1][j + 1] + "\n"
                j += 1
            i += 1
        self.G = load_routes(stringG, symmetric=False)
        #print(json.dumps(self.G, indent=4, sort_keys=True))

    # this function look for next step in dictionary
    def actions(self, s):
        return self.G[s].keys()

    # this function return the next step if he exist
    def succ(self, s, a):
        if a in self.G[s]:
            return a
        raise ValueError(f'No route from {s} to {a}')

    # this function check if he arrived to the goal
    def is_goal(self, s):
        return s == self.goal

    # this function return the cost of the current step
    def step_cost(self, s, a):
        return self.G[s][a]

    # this function strind of the state
    def state_str(self, s):
        return s
