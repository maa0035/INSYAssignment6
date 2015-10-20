# ------------------
# lap_2 - LAP heuristic 2 - assigns low-cost task to each person and
#   does a local search based on the assignment sequence
#
#   2015-09-15 - jeff smith
#
# $Id: lap_h2.py 653 2015-09-28 19:57:50Z smitjef $
# ------------------
import sys
from random import sample
import lap

#
# solve - solves the problem for a given assignment sequence
#
def solve(costs, people, tasks, seq):
    total_cost = 0
    for k in seq:
        # find the low cost task for this person
        task, min_cost = lap.low_cost_task(costs, k, tasks)
        # assign task to person and person to task
        people[k] = task
        tasks[task] = k
        total_cost += min_cost
    return total_cost

def calcSDPI():
    while True:
        minval = 0
        swapi = -1
        swapj = -1
        for i in range(n-1):
            for j in range(i+1,n):
                if change(i,j) < minval:
                    minval = chang(i,j)
                    swapi = i
                    swapj = j
    if minval<0:
        swap(swapi,swapj)
    else
        break

#
# main
#
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
    # store the solution -- need to use deepcopy so the best
    #   incumbent solution is not overwritten
    solution = lap.store_solution(people, tasks, cost, range(len(people)))
    print 'Iteration {:3d}  Cost: {:.2f}'.format(-1, solution['obj_val'])
    # iterate
    for k in range(nreps):
        # clear the current assignments
        lap.clear_solution(people, tasks)
        # sample a random sequence
        seq = sample(range(len(people)), len(people))
        # solve with the random sequence
        cost = solve(costs, people, tasks, seq)
        print 'Iteration {:3d}  Cost: {:.2f}'.format(k, cost)
        # if this solution is better than the best incumbent, 
        #   make it the best incumbent.
        if cost < solution['obj_val'] :
            solution = lap.store_solution(people, tasks, cost, seq)
    # show solution
    print '\nFinal solution:'
    print 'Sequence: {}'.format(solution['seq'])
    lap.show_solution(costs, solution['people'], solution['tasks'])

# if cmd line, execute main
if __name__ == '__main__' : main()

