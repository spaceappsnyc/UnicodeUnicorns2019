from pandas import read_csv
import numpy

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


# Read the bastard
dataset = read_csv('pima-indians-diabetes.data.csv', header=None)

#Count empties for each column
# print((dataset[[1,2,3,4,5]] ==0).sum())

#Mark zeros as NaN
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, numpy.NaN)

# Drop the missing
dataset.dropna(inplace=True)

# Count the NaNs by column
# print(dataset.isnull().sum())

# Print the top 20
# print(dataset.head(20))

#Rip the values
values = dataset.values

#Split to X and y,  input and outputs
X = values[:, 0:8]
y = values[:, 8]

#Make the model
model = LinearDiscriminantAnalysis()

#Do some magic
kfold = KFold(n_splits=3, random_state=7)

#Check the results
result = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')

#Print the results
print(result.mean())
