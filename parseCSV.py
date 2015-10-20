# ------------------
# parseCSV - Parses a CSV File
#
#   2015-09-15 - jeff smith
#   Based on code originally developed by Jacob Conaway and David Jones 
# $Id: parseCSV.py 644 2015-09-23 17:57:05Z smitjef $
# ------------------

def parseCSV(filename, dataType='float', returnJagged=False, fillerValue=0, delimiter=',', commentChar='%'):
    # define the matrix
    matrix = []
    # open the file
    with open(filename, 'U') as csvfile :
        # read all the lines
        csvFile = csvfile.readlines()
        maxSize = 0
        # iterate through each line
        for line in csvFile :
            # check for comments, go to next line if this is a comment
            if(line.startswith(commentChar)):
                continue
            # make sure it's not a blank line
            if line.rstrip():
                # Check for the data type (float or int)
                if dataType == 'float':
                    row = map(float, filter(None, line.rstrip().split(delimiter)))
                elif dataType == 'int':
                    row = map(int, filter(None, line.rstrip().split(delimiter)))                
                matrix.append(row)
                if len(row) > maxSize :
                    maxSize = len(row)
        # unless returnJagged is true, fill the blank values
        if not returnJagged :
            for row in matrix :    
                row += [fillerValue] * (maxSize - len(row))
        if len(matrix) == 1 :
            # This is a vector, just return a 1-D vector
            matrix = matrix[0]
    return matrix

def printMatrix(matrix):
    for row in matrix:
        for cell in row:
            print cell,