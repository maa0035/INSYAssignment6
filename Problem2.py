import sys
import lap
import Problem1
from Problem1 import swap

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
    for k in range(len(people)):
        # find the low cost task for this person
        task, min_cost = lap.low_cost_task(costs, k, tasks)
        # assign task to person and person to task
        people[k] = task
        tasks[task] = k
    while True:
        minval = 0
        swapi = -1
        swapj = -1
        for i in range(len(people)-1):
            for j in range(i+1,len(people)):
                k = people[i]
                l = people[j]
                change = -costs[i][k] - costs[j][l] + costs[i][l] + costs[j][k]
                if change < minval:
                    minval = change
                    swapi = i
                    swapj = j
                if minval<0:
                    swap(i,j, people)
    print '\nFinal solution:'
    lap.show_solution(costs, people, tasks)

if __name__ == '__main__' : main()
