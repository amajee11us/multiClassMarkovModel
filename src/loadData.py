import os, itertools
import pandas as pd
import numpy as np


if __name__ == '__main__':
    # Changing directories
    os.chdir(os.path.dirname(__file__))
    filename = '../examples/MLC/Sample_1_MLC_2022.data'

    #Printing file location
    print('\nName of the file ' + filename + '\n')

    #Opening file
    f = open(filename, 'r')

    #Four Line preamble


    #First line is the total number of variables
    numberOfVariables = f.readline()
    print("numberOfVariables: \n" + numberOfVariables)

    #Getting the second line into secLine asarray
    secLine = np.asarray(f.readline().split(), dtype=np.int32)
    #Getting the first number which is the number of evidence variables
    numOfEvidenceVariables = secLine[:1]
    #Getting the rest of the line which is the indexes of observed variables
    indexObservedVariables = secLine[1:]
    print("number of evidence variables:")
    print(numOfEvidenceVariables)
    print("indexes")
    print(indexObservedVariables)

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

    fileLocation = "C:/multiClassMarkovModel/examples/MLC/Sample_1_MLC_2022.data"
    dataPoints = []
    #df = pd.read_csv(fileLocation, skiprows=7, sep=" ", names=["observed variables", "query variables", "weights"])
    df = pd.read_csv(fileLocation, skiprows=7, sep=" ", header=None)
    print(df)
    #Getting data points
    #for i in range(int(numberOfDataPoints)):
        #line = np.asarray(f.readline().split(), dtype=float)
        #dataPoints.append((np.asarray(line, dtype=np.int32))
    # df['Observed'] = df[df.columns[1:]].apply(
    #     lambda x: ','.join(x.dropna().astype(str)),
    #     axis=1
    # )
    # print(df['Observed'])


    # 2nd file
    filename = '../examples/MLC/Sample_2_MLC_2022.data'
    print('\nName of the file ' + filename + '\n')
    f = open(filename, 'r')
    numberOfVariables = f.readline()
    print(numberOfVariables)


    #Getting the second line into secLine asarray
    secLine = np.asarray(f.readline().split(), dtype=np.int32)
    #Getting the first number which is the number of evidence variables
    numOfEvidenceVariables = secLine[:1]
    #Getting the rest of the line which is the indexes of observed variables
    indexObservedVariables = secLine[1:]
    print("number of evidence variables:")
    print(numOfEvidenceVariables)
    print("indexes")
    print(indexObservedVariables)

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

    fileLocation = "C:/multiClassMarkovModel/examples/MLC/Sample_2_MLC_2022.data"
    dataPoints = []
    #df = pd.read_csv(fileLocation, skiprows=7, sep=" ", names=["observed variables", "query variables", "weights"])
    df = pd.read_csv(fileLocation, skiprows=7, sep=" ", header=None)
    print(df)
    #Getting data points
    #for i in range(int(numberOfDataPoints)):
        #line = np.asarray(f.readline().split(), dtype=float)
        #dataPoints.append((np.asarray(line, dtype=np.int32))
    # df['Observed'] = df[df.columns[1:]].apply(
    #     lambda x: ','.join(x.dropna().astype(str)),
    #     axis=1
    # )
    # print(df['Observed'])



    # 3rd file
    filename = '../examples/MLC/Sample_3_MLC_2022.data'
    print('\nName of the file ' + filename + '\n')


    #Getting the second line into secLine asarray
    # int32 does not work here
    secLine = np.asarray(f.readline().split())
    #Getting the first number which is the number of evidence variables
    numOfEvidenceVariables = secLine[:1]
    #Getting the rest of the line which is the indexes of observed variables
    indexObservedVariables = secLine[1:]
    print("number of evidence variables:")
    print(numOfEvidenceVariables)
    print("indexes")
    print(indexObservedVariables)

    #Third Line
    #Getting the third line
    # int32 does not work here
    thirdLine = np.asarray(f.readline().split())
    #Getting the number of queries
    numOfQueryVariables = thirdLine[:1]
    #Getting the rest of line which is the indexes of queries
    indexQueryVariables = thirdLine[1:]

    #Fourth Line
    # Getting the fourth line
    # int32 does not work here
    fourthLine = np.asarray(f.readline().split())
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

    fileLocation = "C:/multiClassMarkovModel/examples/MLC/Sample_3_MLC_2022.data"
    dataPoints = []
    #df = pd.read_csv(fileLocation, skiprows=7, sep=" ", names=["observed variables", "query variables", "weights"])
    df = pd.read_csv(fileLocation, skiprows=7, sep=" ", header=None)
    print(df)
    #Getting data points
    #for i in range(int(numberOfDataPoints)):
        #line = np.asarray(f.readline().split(), dtype=float)
        #dataPoints.append((np.asarray(line, dtype=np.int32))
    # df['Observed'] = df[df.columns[1:]].apply(
    #     lambda x: ','.join(x.dropna().astype(str)),
    #     axis=1
    # )
    # print(df['Observed'])



    #4th file
    filename = '../examples/MLC/Sample_4_MLC_2022.data'
    print('\nName of the file ' + filename + '\n')


    #Getting the second line into secLine asarray
    # int32 does not work here
    secLine = np.asarray(f.readline().split())
    #Getting the first number which is the number of evidence variables
    numOfEvidenceVariables = secLine[:1]
    #Getting the rest of the line which is the indexes of observed variables
    indexObservedVariables = secLine[1:]
    print("number of evidence variables:")
    print(numOfEvidenceVariables)
    print("indexes")
    print(indexObservedVariables)

    #Third Line
    #Getting the third line
    # int32 does not work here
    thirdLine = np.asarray(f.readline().split())
    #Getting the number of queries
    numOfQueryVariables = thirdLine[:1]
    #Getting the rest of line which is the indexes of queries
    indexQueryVariables = thirdLine[1:]

    #Fourth Line
    # Getting the fourth line
    # int32 does not work here
    fourthLine = np.asarray(f.readline().split())
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

    fileLocation = "C:/multiClassMarkovModel/examples/MLC/Sample_4_MLC_2022.data"
    dataPoints = []
    #df = pd.read_csv(fileLocation, skiprows=7, sep=" ", names=["observed variables", "query variables", "weights"])
    df = pd.read_csv(fileLocation, skiprows=7, sep=" ", header=None)
    print(df)
    #Getting data points
    #for i in range(int(numberOfDataPoints)):
        #line = np.asarray(f.readline().split(), dtype=float)
        #dataPoints.append((np.asarray(line, dtype=np.int32))
    # df['Observed'] = df[df.columns[1:]].apply(
    #     lambda x: ','.join(x.dropna().astype(str)),
    #     axis=1
    # )
    # print(df['Observed'])