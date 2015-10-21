import sys
from random import sample
import lap
from lap_h2 import solve 

#problem 1
# let k be the task assigned to i
# let l be the task assigned to j

# def swap(i,j):
#     temp = people[i]
#     people[i] = people[j]
#     people[j] = temp
    
def change(i,j):
    pass
        
 
def main(): 
    # default values
    nreps = 100
    fname = 'r.csv'
    # argv[0] - file name
    # argv[1] - number of replications
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        if len(sys.argv) > 2:
            try:
                nreps = int(sys.argv[2])
            except:
                print 'Invalid parameters.  Syntax: lab_h2.py fname nreps'
                exit()
    # initialize
    costs, people, tasks = lap.initialize(fname, 1)
    # initial solution with the "natural" sequence
    cost = solve(costs, people, tasks, range(len(people)))     
    costs, people, tasks = lap.initialize(fname, 1) 
    i = 0
    j = 1
    k = people[i]
    l = people[j]
    costs[i][k]
    costs[j][l]
    change = -costs[i][k] - costs[j][l] + costs[i][l] + costs[j][k]
    print change
    print 'this worked'
#     if change < 0
#         swap(i,j)
#     for n in range(100000):
#         i,j = random.sample(2)
#         if change(i,j) < 0:
#             swap(i,j)
