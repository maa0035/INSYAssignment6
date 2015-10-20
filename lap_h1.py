# ------------------
# lap_h1 - LAP heuristic 1 - assign low-cost task to each person
#
#   2015-09-15 - jeff smith
#
# $Id: lap_h1.py 654 2015-09-28 20:26:49Z smitjef $
# ------------------
import sys
import lap

# initialize parameters then check for command line changes
show_intermediate = 1
fname = 'r.csv'
if len(sys.argv) > 1:
    fname = sys.argv[1]
    if len(sys.argv) > 2:
        show_intermediate = int(sys.argv[2])
# initialize the data structures using the cost matrix file
costs, people, tasks = lap.initialize(fname, 1)
# for each person, assign their low-cost task
for k in range(len(people)):
    # find the low cost task for this person
    task, min_cost = lap.low_cost_task(costs, k, tasks)
    # assign task to person and person to task
    people[k] = task
    tasks[task] = k
    # show current assignment
    if show_intermediate:
        if people[k] != -1:
            print 'Assigned P{} task T{} at cost {:.2f}'.format(
                k,
                people[k], 
                min_cost
                )
# show solution
print '\nFinal solution:'
lap.show_solution(costs, people, tasks)

