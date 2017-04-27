# Functions to be used in the Kaggle Titanic Challenge

import csv
import numpy as np

def extractTrainingData() :

    # read in training data from train.csv
    file = open('train.csv', 'rb')
    readObj = csv.reader(file)

    # initialise training data
    trainingData = []

    # loop through each passenger and put data into a list, excluding
    # their name, ticket number, cabin number and port
    for n, row in enumerate(readObj):

        if n == 0: continue  # ignore header

        # change 'male' to 0, and 'female' to 1
        row[4] = 0 if row[4] == 'male' else 1

        row.pop(3)  # exclude name
        row.pop(7)  # exclude ticket number
        row.pop(8)  # exclude cabin
        row.pop(8)  # exclude port of embarkment

        # change data from strings to int and float
        for i, item in enumerate(row):

            if i == 7:
                row[i] = float(row[i])  # convert fare to float
            elif i == 4:
                row[4] = float(row[4]) if row[4] != '' else float('nan')  # some ages are missing
            else:
                row[i] = float(row[i])

        # remove passenger ID
        row.pop(0)

        # add this passengers data to list
        trainingData.append(row)

    # trainingData is currently stored as a list; convert
    # into a numpy array for use later on
    trainingData = np.asarray(trainingData)

    return trainingData


def extractTestData() :
    # read in test data from train.csv
    file = open('test.csv', 'rb')
    readObj = csv.reader(file)

    # initialise test data
    testData = []

    # loop through each passenger and put data into a list, excluding
    # their name, ticket number, cabin number and port
    for n, row in enumerate(readObj):

        if n == 0: continue  # ignore header

        # change 'male' to 0, and 'female' to 1
        row[3] = 0 if row[3] == 'male' else 1

        row.pop(2)  # exclude name
        row.pop(6)  # exclude ticket number
        row.pop(7)  # exclude cabin
        row.pop(7)  # exclude port of embarkment

        # change data from strings to int and float
        for i, item in enumerate(row):

            if i == 6:
                row[i] = float(row[i]) if row[i] != '' else float('nan') # convert fare to float
            elif i == 3:
                row[3] = float(row[3]) if row[3] != '' else float('nan')  # some ages are missing
            else:
                row[i] = float(row[i])

        # remove passenger ID
        row.pop(0)

        # add this passengers data to list
        testData.append(row)

    # trainingData is currently stored as a list; convert
    # into a numpy array for use later on
    testData = np.asarray(testData)

    return testData