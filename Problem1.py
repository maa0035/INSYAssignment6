import sys
import random
import lap
#from lap_h2 import solve 

#problem 1
# let k be the task assigned to i
# let l be the task assigned to j

def swap(i,j, people):
    temp = people[i]
    people[i] = people[j]
    people[j] = temp
    
# def change(i,j):
#     pass
        
 
def main(): 
# initialize parameters then check for command line changes
    show_intermediate = 1
    fname = 'r.csv'
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        if len(sys.argv) > 2:
            show_intermediate = int(sys.argv[2])
    # initialize the data structures using the cost matrix file
    costs, people, tasks = lap.initialize(fname, 1)
    # initial solution with the "natural" sequence
    #cost = solve(costs, people, tasks, range(len(people)))     
    #costs, people, tasks = lap.initialize(fname, 1) 
    i = 10
    j = 12
    k = people[i]
    l = people[j]
    costs[i][k]
    costs[j][l]
    swap(i,j,people)
    change = -costs[i][k] - costs[j][l] + costs[i][l] + costs[j][k]
    if change < 0:
        swap(i,j, people)
    for n in range(100):
        j = random.random()
        i = random.random()
        k = people[i]
        l = people[j]
        change = -costs[i][k] - costs[j][l] + costs[i][l] + costs[j][k]
        if change < 0:
            swap(i,j)
    print 'this worked'
#     if change < 0
#         swap(i,j)
#     for n in range(100000):
#         i,j = random.sample(2)
#         if change(i,j) < 0:
#             swap(i,j)
# if cmd line, execute main
if __name__ == '__main__' : main()

