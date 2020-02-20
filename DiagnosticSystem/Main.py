import pickle
import pandas as pd
import RandomForestClassifier
import SVM
import RuleBased

with open("data/wdbc.pkl", 'rb') as f:
    data = pickle.load(f)
data_df = pd.DataFrame(data)

print('Random forest')
#RandomForestClassifier.classify(data_df)
print('SVC')
#SVM.classify(data_df)
print('Rule based')
RuleBased.classify(data_df)