from sklearn import tree  # uses decision tree classifier
from sklearn.ensemble import RandomForestClassifier  # uses random forest classifier
from sklearn.linear_model import (
    LogisticRegression,
)  # uses logistic regression classifier
from sklearn.naive_bayes import GaussianNB  # uses naive bayes classifier
from sklearn.neighbors import KNeighborsClassifier  # uses k-nearest neighbor classifier

#  [height, weight, shoe size]
x = [
    [181, 80, 44],
    [177, 70, 43],
    [160, 60, 38],
    [154, 54, 37],
    [166, 65, 40],
    [190, 90, 47],
    [175, 64, 39],
    [177, 70, 40],
    [159, 55, 37],
    [171, 75, 42],
    [181, 85, 43],
]

# gender list corresponding to the above body-measurements
y = [
    "male",
    "female",
    "female",
    "female",
    "male",
    "male",
    "male",
    "female",
    "male",
    "female",
    "male",
]

# variable to store the decision tree classification
clf = tree.DecisionTreeClassifier()

# fitting the data using decision tree
clf = clf.fit(x, y)

# variable to store the k-nearest neighbor classification
neigh = KNeighborsClassifier(n_neighbors=3)

# fitting the data using k-nearest neighbor
neigh.fit(x, y)

# variable to store the logistic regression classification
log_reg = LogisticRegression()

# fitting the data using logistic regression
log_reg.fit(x, y)

# variable to store the decision tree classification
gnb = GaussianNB()

# fitting the data using logistic regression
gnb = gnb.fit(x, y)

# variable to store the random forest classification
rfc = RandomForestClassifier(n_estimators=2)

# fitting the data using random forest
rfc = rfc.fit(x, y)


# create a dict

predictions = {}

# test data from the given dataset
t = [[177, 70, 43]]

# a new variable to predict the gender based on body measurement
prediction_dt = clf.predict(t)
prediction_kn = neigh.predict(t)
prediction_log = log_reg.predict(t)
prediction_gnb = gnb.predict(t)
prediction_rfc = rfc.predict(t)

# add results to dict
predictions["Decision Tree Classifier"] = prediction_dt
predictions["K-Nearest Neighbor"] = prediction_kn
predictions["Logistic Regression"] = prediction_log
predictions["Gaussian NB Classifier"] = prediction_gnb
predictions["Random Forest Classifier"] = prediction_rfc

print("These results are predicted using a predefined test-data.\n")

for keys in predictions.keys():
    print(f"{keys} predicted {predictions.get(keys)}.")

print("\n")

# create a list for more accurate methods

methods = []

for keys in predictions.keys():
    if predictions.get(keys) == "female":
        methods.append(keys)
        print(f"{keys} is more accurate")

print("\n")

print(f"The {methods} will be used for classifications.")

print("\n")

var1 = float(input("Enter Height: "))
var2 = float(input("Enter Weight: "))
var3 = float(input("Enter Shoe-Size: "))
190

data = [[var1, var2, var3]]

for i in range(len(methods)):
    if methods[i] == "Decision Tree Classifier":
        prediction_dt1 = clf.predict(data)
        print(f"{methods[i]} predicted {prediction_dt1}.")
    elif methods[i] == "K-Nearest Neighbor":
        prediction_kn1 = neigh.predict(data)
        print(f"{methods[i]} predicted {prediction_kn1}.")
    elif methods[i] == "Logistic Regression":
        prediction_log1 = log_reg.predict(data)
        print(f"{methods[i]} predicted {prediction_log1}.")
    elif methods[i] == "Gaussian NB Classifier":
        prediction_gnb1 = gnb.predict(data)
        print(f"{methods[i]} predicted {prediction_gnb1}.")
    elif methods[i] == "Random Forest Classifier":
        prediction_rfc1 = rfc.predict(data)
        print(f"{methods[i]} predicted {prediction_rfc1}.")
