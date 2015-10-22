import sys
import random
import lap
import lap_h2

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
#-----------USE H1
    # initialize the data structures using the cost matrix file
#     for k in range(len(people)):
#         # find the low cost task for this person
#         task, min_cost = lap.low_cost_task(costs, k, tasks)
#         # assign task to person and person to task
#         people[k] = task
#         tasks[task] = k
#-----------USE H2
    costs, people, tasks = lap.initialize(fname, 1)
    # initial solution with the "natural" sequence
    cost = lap_h2.solve(costs, people, tasks, range(len(people)))
    # store the solution -- need to use deepcopy so the best
    #   incumbent solution is not overwritten
    solution = lap.store_solution(people, tasks, cost, range(len(people)))
##------------------------
    print 'Iteration {:3d}  Cost: {:.2f}'.format(-1, solution['obj_val'])
    # iterate
    for k in range(100):
        # clear the current assignments
        lap.clear_solution(people, tasks)
        # sample a random sequence
        seq = lap_h2.sample(range(len(people)), len(people))
        # solve with the random sequence
        cost = lap_h2.solve(costs, people, tasks, seq)
        print 'Iteration {:3d}  Cost: {:.2f}'.format(k, cost)
        # if this solution is better than the best incumbent, 
        #   make it the best incumbent.
        if cost < solution['obj_val'] :
            solution = lap.store_solution(people, tasks, cost, seq)
    # show solution
    print '\nFinal solution:'
    print 'Sequence: {}'.format(solution['seq'])
    lap.show_solution(costs, solution['people'], solution['tasks'])
#------------------------
    #Calculate Problem 1 Algorithm
#     totalcost = 0
    for n in range(100000):
        i, j = random.sample(range(len(people)), 2)
        k = people[i]
        l = people[j]
        change = -costs[i][k] - costs[j][l] + costs[i][l] + costs[j][k]
        if change < 0:
            swap(i,j, people)
#     for index in range(25):
#         totalcost += costs[index][people[index]]
#         print people[index]
#     print totalcost
    print '\nFinal solution:'
    lap.show_solution(costs, people, tasks)

if __name__ == '__main__' : main()

