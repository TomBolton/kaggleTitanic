### Tom Bolton
### 28/04/2017
### thomasmichaelbolton@gmail.com

This repository contains python scripts to tackle the Kaggle Titanic classification challenge. Three
different methods are implemented using the Scikit Learn package: multi-layer perceptron (MLP), 
K-nearest neighbours (KNN), and support vector machines (SVM). SVM performed best, followed by MLP and
finally KNN.

Missing values in the age and fares features are replaced by the median. Features such as ticket 
number and port of embarkment are assumed to be unimportant in survival prediction.
