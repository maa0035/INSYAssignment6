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
    for k in range(len(people)):
        # find the low cost task for this person
        task, min_cost = lap.low_cost_task(costs, k, tasks)
        # assign task to person and person to task
        people[k] = task
        tasks[task] = k
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

