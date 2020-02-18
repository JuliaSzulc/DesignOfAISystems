from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest

def classify(df):
    classifier = LinearSVC()
    Y = df['malignant']
    X = df.drop('malignant',1)

    #Scale data
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    #Only select 5 best features
    select = SelectKBest(k=5)
    X = select.fit_transform(X,Y)

    #Train/Test
    X_train, X_test, Y_train,Y_test = train_test_split(X,Y, test_size=0.2)
    classifier.fit(X_train, Y_train)
    Y_pred = classifier.predict(X_test)
    print(accuracy_score(Y_test, Y_pred))