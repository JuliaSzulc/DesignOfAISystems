from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def classify(df):
    classifier = RandomForestClassifier()
    Y = df['malignant']
    X = df.drop('malignant',1)

    X_train, X_test, Y_train,Y_test = train_test_split(X,Y, test_size=0.2, random_state=24)
    classifier.fit(X_train, Y_train)
    Y_pred = classifier.predict(X_test)
    print(accuracy_score(Y_test, Y_pred))

