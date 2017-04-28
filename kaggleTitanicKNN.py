# This is a script to attempt the Kaggle Titanic binary classification problem.
# The training data is stored in 'train.csv' and the test data is stored in
# 'test.csv'. Within these .csv files, are the following properties for each
# passenger:
#
#   1. Passenger ID (integer)
#   2. Survived (binary)
#   3. Social class (integer)
#   4. Name (string)
#   5. Gender (binary)
#   6. Age (integer)
#   7. Number of siblings (integer)
#   8. Number of parents (integer)
#   9. Ticket Number (string)
#   10. Fare (float)
#   11. Cabin number (string)
#   12. Port of embarkment (string)
#
# A k-Nearest Neighbour (KNN) algorithm is used in this script.

from titanicFunctions import *
from sklearn.neighbors import KNeighborsClassifier

##### Data Preparation #####

# extact data from .csv files
trainingData = extractTrainingData()
testData = extractTestData()

# Missing values from the 'age' and 'fare' categories are
# represented by NaNs in the training and test data. Replace
# these by the median value calculate from training data.
ageData = []
for age in trainingData[:,3] :
    if not np.isnan( age ) : ageData.append( age )

fareData = []
for fare in trainingData[:,-1] :
    if not np.isnan( fare ) : fareData.append( fare )

# calculate median age and fare
ageMedian = np.median( np.asarray( ageData ) )
fareMedian = np.median( np.asarray( fareData ) )

# replace age nans with median
for i, age in enumerate( trainingData[:,3] ) :
    if np.isnan( age ) : trainingData[i,3] = ageMedian

for i, age in enumerate( testData[:,2] ) :
    if np.isnan( age ) : testData[i,2] = ageMedian

for i, fare in enumerate( testData[:,-1]) :
    if np.isnan( fare ) : testData[i,-1] = fareMedian


##### Nearest Neighbour Algorithm #####

# form array of features and targets
x = trainingData[:,1:]    # feature values
y = trainingData[:,0]       # survival values

xTest = testData

# need to normalise data of each feature ( x - mean(x) )/std(x)
for n in range( x.shape[1] ) :

    trainMean = np.mean( x[:,n] )
    trainStd  = np.std( x[:,n] )

    testMean = np.mean( xTest[:,n] )
    testStd  = np.std( xTest[:,n] )

    x[:,n] = ( x[:,n] - trainMean )/trainStd
    xTest[:,n] = ( xTest[:,n] - testMean )/testStd


# construct classifier
knnClassifier = KNeighborsClassifier( n_neighbors=30 )

# learn the training data
knnClassifier.fit(x,y)

# make predictions
yPred = knnClassifier.predict( xTest )

##### Write predictions to new .csv file #####

newFile = open( 'predictions.csv', 'wb')
writerObj = csv.writer( newFile )

# write csv file line-by-line, and add passenger id
for id, value in enumerate( yPred ) :
    print value
    writerObj.writerow( [ str( 892 + id ), str( int( value ) ) ] )
