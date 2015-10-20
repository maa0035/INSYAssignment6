# ------------------
# randomLAP - generates a random cost matrix for an LAP
#
#   2015-09-15 - jeff smith
#
# $Id: randomLAP.py 645 2015-09-24 14:35:19Z smitjef $
# ------------------
import sys
from random import random

# default parameter values in case they aren't specified
#   on the command line
fname = 'r.csv'
num = 25
min_val = 100
max_val = 500
# command line parameters
if len(sys.argv) > 1:
    # asking for help?
    if sys.argv[1] == '--help':
        print 'Syntax: randomLAP [fname] [num min_val max_val]'
        exit()
    fname = sys.argv[1]
    if len(sys.argv) == 5 :
        try:
            num = int(sys.argv[2])
            min_val = float(sys.argv[3])
            max_val = float(sys.argv[4])
        except:
            print 'Invalid parameters.  Syntax: randomLP.py fname num min_val max_val'
            exit()
val_range = max_val - min_val
matrix = []
# generate the random values - use U(min_val, max_val)
for k in range(num):
    matrix.append([])
    for j in range(num):
        matrix[k].append(min_val + (random() * val_range))
# write the file
with open(fname, 'w') as outfile:
    for k in range(num):
        row = ['{:.2f}'.format(x) for x in matrix[k]]
        outfile.write('{}\n'.format(', '.join(row)))
# print information
print '\nCreated a {}x{} cost matrix with values in the range {} - {}.  File: {}\n'.format(
    num, num, min_val, max_val, fname
    )