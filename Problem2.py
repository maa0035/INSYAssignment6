import sys
import lap
from Problem1 import swap
import lap_h2

def main():
    # initialize parameters then check for command line changes
    fname = 'r.csv'
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        if len(sys.argv) > 2:
            show_intermediate = int(sys.argv[2])
    # initialize the data structures using the cost matrix file
    costs, people, tasks = lap.initialize(fname, 1)
    # initial solution with the "natural" sequence
    cost = lap_h2.solve(costs, people, tasks, range(len(people)))
    solution = lap.store_solution(people, tasks, cost, range(len(people)))
    people = solution['people']
    for i in range(len(people)-1):
        minval = 0
        for j in range(i+1,len(people)):
            k = people[i]
            l = people[j]
            change = -costs[i][k] - costs[j][l] + costs[i][l] + costs[j][k]
            if change < minval:
                minval = change
                swap(i,j, people)
    print '\nFinal solution:'
    lap.show_solution(costs, people, tasks)

if __name__ == '__main__' : main()
