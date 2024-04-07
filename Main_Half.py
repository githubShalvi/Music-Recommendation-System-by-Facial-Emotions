	
# ========= IMPORT PACKAGES =========

import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
# ========= READ INPUT =========


df= pd.read_excel("Dataset.xlsx")

print("---------------------------")
print("DATA SELECTION")
print("---------------------------")
print()

print(df.head(10))

# ========= PREPROCESSING =========

print("---------------------------")
print("CHECKING MISSING VALUES")
print("---------------------------")
print()

print(df.isnull().sum())
print()

# ========= DATA SPLITTING =========


X = df['mood']
y = df['Label']


print("---------------------------")
print("DATA SPLITTING")
print("---------------------------")
print()

cv = CountVectorizer()
X = cv.fit_transform(X) # Fit the Data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


print()
print("Total No of input data    :",df.shape[0])
print()
print("Total No of training data :",X_train.shape[0])
print()
print("Total No of testing data  :",X_test.shape[0])
print()

# ========= CLASSIFICATION =========

clf = MultinomialNB()
clf.fit(X_train,y_train)
pred=clf.predict(X_test)
acc_nb=clf.score(X_test,y_test)

print("-----------------------------------------------------------")
print(" 1.LOGISTIC REGRESSION")
print("-----------------------------------------------------------")
print()
print("1.Accuracy: ",acc_nb ,'%')
print()
print(metrics.classification_report(y_test, pred))
print()
