# ------------------
# lap - LAP model general functions
#
#   2015-09-15 - jeff smith
#
# $Id: lap.py 654 2015-09-28 20:26:49Z smitjef $
# ------------------
import sys
import copy
# need to update this to point to the location of parseCSV.py
sys.path.append('/Users/mattaskounis/Desktop/lap')
from parseCSV import parseCSV

# 
# initialize the problem - fname is the csv file with the cost matrix
# 
def initialize(fname, show):
    # read the costs matrix from the csv file
    costs = parseCSV(fname)
    # people[i] is the index of the task assigned to person i 
    #   or -1 if the person does not have an assigned task
    people = []
    # tasks[j] is the index of the person assigned to task j
    #   or -1 if the task is unassigned
    tasks = []
    # create the people and tasks lists
    for k in range(len(costs)):
        people.append(-1)
        tasks.append(-1)
    if show:
        print '{} people, {} tasks, {}x{} costs, lb = {:.2f}'.format(
            len(people), 
            len(tasks), 
            len(costs), 
            len(costs),
            simple_lb(costs))
    return costs, people, tasks
    
#
# show_solution - displays the current solution
#
def show_solution(costs, people, tasks):
    for k in range(len(people)):
        if people[k] > -1:
            task = 'T{}'.format(people[k])
            cost = costs[k][people[k]]
        else:
            task = 'n/a'
            cost = 0.0
        print '\tP{}, {}, {:.2f} '.format(k, task, cost)
    print '\nTotal cost: {:.2f} (lower bound: {:.2f})'.format(
        calc_cost(costs, people)[0],
        simple_lb(costs)
        )

#
# calc_cost - calculates the current solution cost
#
def calc_cost(costs, people):
    total_cost = 0
    num_assigned = 0
    # for each person
    for k in range(len(people)):
        # make sure the person has an assigned task
        if people[k] != -1:
            total_cost += costs[k][people[k]]
            num_assigned += 1
    return total_cost, num_assigned

#
# low_cost_task - finds the lowest cost available task for the
#   specified person
#
def low_cost_task(costs, person, tasks):
    # initialize with the biggest possible number
    min_cost = 1e308 
    # index of the low-cost task
    min_idx = -1
    # loop through all tasks
    for k in range(len(tasks)):
        # if the task is currently unassigned
        if tasks[k] == -1:
            # is the task lower cost than the current minimum?
            if costs[person][k] < min_cost:
                min_cost = costs[person][k]
                min_idx = k
    return min_idx, min_cost

#
# simple_lb - calculates a simple lower bound based on low-cost assignment
#
def simple_lb(costs):
    # min cost task for each person
    total_cost1 = 0;
    for k in range(len(costs)) :
        total_cost1 += min(costs[k])
    # min cost person for each task
    total_cost2 = 0;
    for k in range(len(costs)):
        total_cost2 += min([c[k] for c in costs])
    # return the better of the two bounds
    return max(total_cost1, total_cost2)

#
# clear_solution - clears the incumbent solution
#
def clear_solution(people, tasks):
    for k in range(len(people)):
        people[k] = -1
    for k in range(len(tasks)):
        tasks[k] = -1

#
# store_solution
#
def store_solution(people, tasks, cost, seq):
    # create the dictonary
    solution = {}
    # need to use copy since the lists are mutable
    solution['people'] = copy.copy(people)
    solution['tasks'] = copy.copy(tasks)
    solution['obj_val'] = cost
    solution['seq'] = copy.copy(seq)
    return solution

#
# main
#
def main():
    # default values
    fname = 'r.csv'
    # argv[0] - file name
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    # initialize
    costs, people, tasks = initialize(fname, 1)
    # Simple assignment - person k gets task k for all k
    for k in range(len(people)):
        people[k] = k;
        tasks[k] = k;
    print '\nSolution:'
    show_solution(costs, people, tasks)

# if cmd line, execute main
if __name__ == '__main__' : main()
