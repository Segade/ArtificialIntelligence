import pandas as pd 

from sklearn.datasets import load_iris

 
iris_data = pd.read_csv("result.csv")

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
# I add layers and I reduce the density gradually until reach 3, the number of possible options:
# draw = 0, Home team = 1, Away team = 2

model.add(Dense(220,activation='relu',input_shape = (None,300)))
model.add(Dense(100, activation='relu'))
model.add(Dense(3, activation='softmax'))
# setting up the model parameters 
model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

from tensorflow.keras.utils import to_categorical
import numpy as np
 
 # I fetch the input and output data 
X = iris_data.iloc[:, 10:310]
# I reshape the input data in the way that the algorithms can work with it
X = np.reshape(X, (380, 1,300))
 
print("x shape", X.shape)
Y = iris_data.iloc[:,6]
# I convert the output in categorical 
Y_c = to_categorical(Y)
# I reshape the output data in the way that the algorithms can work with it
Y_c = np.reshape(Y_c,(380,1,3))
 
#history = model.fit(X,Y_c,epochs=500)

from matplotlib import pyplot as py

#py.plot(history.history['loss'])
#py.plot(history.history['accuracy'])

from sklearn.model_selection import train_test_split

 
# I divide the input and output data by 70% and leave the other 30% for testing purposes 
X_train,X_test,Y_train,Y_test = train_test_split(X,Y_c,test_size=  0.3)

# I reshape the new variables with the corresponding values 
X_train = np.reshape(X_train, (266,1,300))
X_test = np.reshape(X_test,(114,1,300))
Y_train =  np.reshape(Y_train,( 266,1,3))
Y_test = np.reshape(Y_test, (114,1,3))
 

model2 = Sequential()
# I add layers and I reduce the density gradually until reach 3, the number of possible options
model2.add(Dense(200,activation='relu',input_shape = (None,300)))
model2.add(Dense(130, activation='relu'))
model2.add(Dense(120, activation='relu'))
model2.add(Dense(3, activation='softmax'))

model2.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# I train the model and I set the number of EPOCs in 200
# The reason is that 200 has the best balance between the lost function and the confusion matrix.
# Actually, with 200 the lost value got under 6, one of the lowest value I got 
# Also, the confusion matrix has values in the three rows most of the times. the other times always 2 rows
# With lower numbers such as 100 or bigger such as 300 or 400, the lost function doesn't improve, I even got over 10 with the two ranges 
# also with lower or bigger, the confusion matrix rarely has values in the three rows. Only with 300 I got three, but rarely as well.
# with  lowwer values, most of the time I got one row or two, never three 
# with under 100, I even got the three rows without any value at all
# In the report document there are two screenshots with 40 and 200 EPOCs

hist2 = model2.fit(X_train,Y_train, validation_data=(X_test,Y_test) , epochs=200)

py.plot(hist2.history['loss'])
py.plot(hist2.history['val_loss'])

 
# I test the model by passing the test data 
Y_pred = model.predict(X_test)
 

from sklearn.metrics import confusion_matrix

import numpy as np

# I test the model with the train data 
Y_train_Pred = model.predict(X_train)

print("jjj", Y_train_Pred.shape)
# I print out the confusion matrix for checking the performance 
# The matrix is a 3X3 matrix for the 3 possible results 
# The first row belongs to the first possible value "Draw". It say the number of times the model determined the result is a draw, Home or Away.
# The first value in the row is the correct number of times. The other values the mode failded 
# In the second row, the middle value is for Home (the correct one for this). Likewise above, the other values means the number of times the model determined Draw or Away and it is wrong 
# the third row is for Away. it is the same logic. The third value is the number of times the model determined Away and it is correct
# the first and second values are for Draw and Home and they are the number of thimes the model is wrong.
print("confusion " , confusion_matrix( np.argmax(Y_pred, axis = 2), np.argmax(Y_test, axis = 2)))

 