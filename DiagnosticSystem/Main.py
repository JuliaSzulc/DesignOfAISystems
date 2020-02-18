import pickle
import pandas as pd
import RandomForestClassifier

with open("data/wdbc.pkl", 'rb') as f:
    data = pickle.load(f)
data_df = pd.DataFrame(data)

RandomForestClassifier.classify(data_df)