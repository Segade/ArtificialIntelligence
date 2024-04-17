from sklearn.tree import DecisionTreeRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Finally, I tryed the decission tree regressor
# This algorithm splits the data in several nodes and tryes to fit the  input in the best leaf 
# This model works reasonable fine. At least, the predicted data has the three possibles values only.
# I use the function to assess the percentages and are usually around the 40% 
# A screenshot of the result is provided in the report document 
df = pd.read_csv("result.csv")

# Sample input data with multiple columns
X = df.iloc[:, 10:310]
# Target values
y = df.iloc[:,6]

X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=  0.3)


# Create a Decision Tree Regression model
model = DecisionTreeRegressor()

# Train the model
model.fit(X_train, Y_train)

# Once trained, you can use the model to make predictions
# For example, predict the target value for a new data point:
 
predicted_value = model.predict(X_test)
print("Predicted value:", predicted_value)

import numpy as np

def similarity_percentage(array1, array2):
    # Check if arrays are of the same length
    if len(array1) != len(array2):
        raise ValueError("Arrays must be of the same length")

    # Count the number of matching elements
    num_matching = sum(1 for a, b in zip(array1, array2) if a == b)

    # Calculate similarity percentage
    similarity_percent = (num_matching / len(array1)) * 100
    return similarity_percent


# Calculate similarity percentage
similarity_percent = similarity_percentage(Y_test, predicted_value )
print("Percentage of similarity:", similarity_percent)

mse = mean_squared_error(Y_test, predicted_value)
print("Mean Squared Error:", mse)
