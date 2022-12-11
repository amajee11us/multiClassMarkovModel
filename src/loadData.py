import os, itertools
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

class LoadData:
    def __init__(self, filename):

        #Printing file location
        print('\nName of the file ' + filename + '\n')

        #Opening file
        f = open(filename, 'r')

        #Four Line preamble
        #First line is the total number of variables
        numberOfVariables = f.readline()

        #Getting the second line into secLine asarray
        secLine = np.asarray(f.readline().split(), dtype=np.int32)
        #Getting the first number which is the number of evidence variables
        numOfEvidenceVariables = secLine[:1]
        #Getting the rest of the line which is the indexes of observed variables
        self.indexObservedVariables = secLine[1:]

        #Third Line
        #Getting the third line
        thirdLine = np.asarray(f.readline().split(), dtype=np.int32)
        #Getting the number of queries
        numOfQueryVariables = thirdLine[:1]
        #Getting the rest of line which is the indexes of queries
        self.indexQueryVariables = thirdLine[1:]

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
                entry_in_row = y #(x,y)
                if ( count < numOfEvidenceVariables):
                    evidence_row.append(entry_in_row)
                else:
                    query_row.append(entry_in_row)
                count += 1
            evidence_rows.append(evidence_row)
            query_rows.append(query_row)

        #print(df)
        self.evidence_df = pd.DataFrame(data=evidence_rows, columns=self.indexObservedVariables)
        self.query_df = pd.DataFrame(data=query_rows, columns=self.indexQueryVariables)
        self.weights_df = pd.DataFrame(data=weight_rows, columns=['weights'])

    def __get_preamble(self):
        pass

    def __get_functionVars(self):
        pass
    
    def get_data_splits(self):
        self.evidence_assignments = self.evidence_df.to_numpy()
        self.query_assignments = self.query_df.to_numpy()

        return train_test_split(self.evidence_assignments, self.query_assignments, test_size=0.33)

    def get_dataframes(self):
        return self.evidence_df, self.query_df, self.weights_df

if __name__ == '__main__':
    print("[Test] Loading some test data ...")
    filename = "/home/shared/anay/multiClassMarkovModel/data/1.data"


    dataloader = LoadData(filename=filename)

    e, q, wt = dataloader.get_dataframes()
    print(e)
    print("---------------------")
    print(q)
    print("---------------------")
    print(wt)
    print("---------------------")

    print(dataloader.get_data_splits())