import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt


columns = "age sex bmi map tc ldl hdl tch ltg  glu".split() #declare column names
diabetes = datasets.load_diabetes()  #call the dataset

df = pd.DataFrame(diabetes.data, columns=columns)

y = diabetes.target # define the target variable in case of linear regresion

#creating test and train data
x_train, x_test, y_train, y_test = train_test_split(df, y, test_size=0.2) #determine how to split the data

print (x_train.shape, y_train.shape)

#fit the model ion training data

lm = linear_model.LinearRegression()

model = lm.fit(x_train,y_train)
predictions = lm.predict(x_test)

#plot
plt.scatter (y_test, predictions)
plt.xlabel("True")
plt.xlabel("predictions")

print ("score:", model.score(x_test,y_test) )


