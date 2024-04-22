import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
# I also try the linear regression model, but this model doesn't fit the project.
# the linear regression tryes to calculate a value close to the correct value.
# The problem is, although the target values are numbers, they are eventually a category, so the output cannot be an approximate value, it has to be 0, 1 or 2 exactly.
# I try to use a function to  to determine the similarity between the predicted value and the testing value, but as the predicted value is not an exact number, the function says always 0%
# I also tryed the mean squared error, but I don't know how to interpretate it 
df = pd.read_csv("result.csv")

x = df.iloc[:, 10:310]
y = df.iloc[:,6]
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=  0.3)


X, Y = np.array(X_train), np.array(Y_train)

 

# to create the regression model as an instance of LinearRegression and fit it with .fit():
model = LinearRegression().fit(X_train, Y_train)

# the properties of the model 
r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"coefficients: {model.coef_}")


# Predictions also work the same way as in the case of simple linear regression:
y_pred = model.predict(X_test)
print(f"predicted response:\n{y_pred}")
 
# The predicted response is obtained with .predict(), which is equivalent to the following:
y_pred = model.intercept_ + np.sum(model.coef_ * X_test, axis=1)
print(f"predicted response:\n{y_pred}")

 
mse = mean_squared_error(Y_test, y_pred)
print("Mean Squared Error:", mse)



