# ------------------
# lap_optimal - LAP optimal - Gurobi
#
#   2015-09-15 - jeff smith
#
# $Id: lap_optimal.py 652 2015-09-28 18:56:36Z smitjef $
# ------------------
import sys
import lap
from gurobipy import *

#
# main
#
def main():
    show_intermediate = 0
    fname = 'r.csv'
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help':
            print 'Syntax: lap_optimal [fname] [0/1 - show gurobi details]'
            exit()
        fname = sys.argv[1]
        if len(sys.argv) > 2:
            show_intermediate = int(sys.argv[2])
    # initialize
    costs, people, tasks = lap.initialize(fname,1)

    # Define the model
    m = Model('LAP')
    # turn off intermediate output
    if show_intermediate == 0:
        m.setParam('OutputFlag',False)
    # Limit to 5 minutes
    m.setParam('TimeLimit', 360)
    
    num_people = len(people)
    num_tasks = len(tasks)
    # decvarx - x[i][j] = 1 if person i is assigned task j
    decvarx = []
    for i in range(num_people):
        decvarx.append([])
        for j in range(num_tasks):
            # Assign decvarx[i][j] to a Gruobi Variable Object
            decvarx[i].append(m.addVar(obj=costs[i][j],vtype=GRB.BINARY))

    # The objective is to minimize the total cost.
    m.modelSense = GRB.MINIMIZE
    # Update model to integrate new variables
    m.update()
    # Each person is assigned exactly 1 task
    for i in range(num_people):
        # quicksum is a Gurobi method (faster than sum for these models)
        m.addConstr(quicksum(decvarx[i][j] for j in range(num_tasks)) == 1)
    # Each task is assigned to exactly 1 person
    for j in range(num_tasks):
        m.addConstr(quicksum(decvarx[i][j] for i in range(num_people)) == 1)
    m.optimize()
    if m.Status == GRB.OPTIMAL:
        print '\nGurobi reports the solution is optimal'
    else:
        print '\nSolution might not be optimal (Gurobi optimal flag not set)'
    print '\nSolution:'
    for i in range(num_people):
        for j in range(num_tasks):
            if decvarx[i][j].x == 1:
                print '\tP{}, T{}, {}'.format(i, j, costs[i][j])
    print '\nTotal Cost: {:.2f}'.format(m.objVal)                

# if cmd line, execute main
if __name__ == '__main__' : main()
