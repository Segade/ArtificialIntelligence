# https://data36.com/random-forest-in-python/#content

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("result.csv")
 
X = df.iloc[:, 10:310]
# Target values
y = df.iloc[:,6]

 # I split the data into train and test data
# 70% for training data and 30% for testing data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=44)
 
# I create the model with 100 trees that create the forest 
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# I train the model 
rf_model.fit(X_train, y_train)

# I test the model 
Y_pred = rf_model.predict(X_test)

# method that compares the two arrays and retruns the percentage of similarity
def similarity_percentage(array1, array2):
    # Check if arrays are of the same length
    if len(array1) != len(array2):
        raise ValueError("Arrays must be of the same length")

    # Count the number of matching elements
    num_matching = sum(1 for a, b in zip(array1, array2) if a == b)

    # Calculate similarity percentage
    similarity_percent = (num_matching / len(array1)) * 100
    return similarity_percent


#print('\npredict \n', predictions, '\n', y_test)

#print(Y_pred)

print(Y_pred)


print("similarity ", similarity_percentage(y_test,Y_pred))