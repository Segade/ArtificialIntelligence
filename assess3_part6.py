from sklearn import svm
from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split

 # I also tryed the support vector classifier 
# This algorithm should suit the project, but for some reason the output that always gets is all ones.
# perhaps, because 1 (Home) is the most common value and the models thinks that it will be correct more times if it provides only that result.
# A screenshot of the output is provided in the report document 
 
df = pd.read_csv("result.csv")
X = df.iloc[:, 10:310]
Y = df.iloc[:,6]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=  0.3)



#clf = svm.SVC(decision_function_shape='ovo')
clf = svm.SVC()
clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)
print(Y_pred)

#SVC(decision_function_shape='ovo')
#dec = clf.decision_function([[1]])
#dec.shape[1] # 4 classes: 4*3/2 = 6
 
#clf.decision_function_shape = "ovr"
#dec = clf.decision_function([[1]])
#dec.shape[1] # 4 classes
 