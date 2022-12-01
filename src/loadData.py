import os, itertools
import pandas as pd
import numpy as np

class LoadTestFormat:
    def __init__(self, filename):

        #Printing file location
        print('\nName of the file ' + filename + '\n')

        #Opening file
        f = open(filename, 'r')

        #Four Line preamble


        #First line is the total number of variables
        numberOfVariables = f.readline()
        #print("numberOfVariables: \n" + numberOfVariables)

        #Getting the second line into secLine asarray
        secLine = np.asarray(f.readline().split(), dtype=np.int32)
        #Getting the first number which is the number of evidence variables
        numOfEvidenceVariables = secLine[:1]
        #Getting the rest of the line which is the indexes of observed variables
        indexObservedVariables = secLine[1:]
        #print("number of evidence variables:")
        #print(numOfEvidenceVariables)
        #print("indexes")
        #print(indexObservedVariables)

        #Third Line
        #Getting the third line
        thirdLine = np.asarray(f.readline().split(), dtype=np.int32)
        #Getting the number of queries
        numOfQueryVariables = thirdLine[:1]
        #Getting the rest of line which is the indexes of queries
        indexQueryVariables = thirdLine[1:]

        #Fourth Line
        # Getting the fourth line
        fourthLine = np.asarray(f.readline().split(), dtype=np.int32)
        # Getting the number of hidden variables
        numOfHiddenVariables = thirdLine[:1]
        # Getting the rest of line which is the indexes of queries
        indexHiddenVariables = thirdLine[1:]

        #Blank line inbetween preamble and data section
        f.readline()

        #Data Section
        #Getting first line
        #Getting T, number of data points
        numberOfDataPoints = f.readline()

        fileLocation = filename
        dataPoints = []
        #df = pd.read_csv(fileLocation, skiprows=7, sep=" ", names=["observed variables", "query variables", "weights"])
        df = pd.read_csv(filename, skiprows=6, sep=" ", header=None)
        evidence_rows = []
        query_rows = []
        weight_rows = []
        for row in df.itertuples(index=False):
            evidence_row = []
            query_row = []
            weight_rows.append(row[-1])
            count = 0
            for x,y in zip(*[iter(row)]*2):
                entry_in_row = (x,y)
                if ( count < numOfEvidenceVariables):
                    evidence_row.append(entry_in_row)
                else:
                    query_row.append(entry_in_row)
                count += 1
            evidence_rows.append(evidence_row)
            query_rows.append(query_row)

            #print(evidence_rows)
            #print(query_rows)

        #print(df)
