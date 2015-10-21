#problem 1
# let k be the task assigned to i
# let l be the task assigned to j
k = people[i]
l = people[j]
costs[i][k]
costs[j][l]
def swap(i,j):
        tmp = people[i]
        people[i] = people[j]
        people[j] = temp
change = -costs[i][k] - costs[j][l] + costs[i][l] + costs[j][k]
if change < 0
        swap(i,j)
for n in range(100000):
        i,j = random.sample(2)
    if change(i,j) < 0:
        swap(i,j)
