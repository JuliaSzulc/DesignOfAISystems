import pickle
import pandas as pd
import RandomForestClassifier
import SVM
import RuleBased
import seaborn as sns
import matplotlib.pyplot as plt

def plot_density(param):
    x_b = [data_df[param][i] for i in data_df.index if not data_df['malignant'][i]]
    x_m = [data_df[param][i] for i in data_df.index if data_df['malignant'][i]]

    sns.kdeplot(x_b, color='b', bw=0.01).set_title(param)
    sns.kdeplot(x_m, color='r', bw=0.01)
    plt.show()

with open("data/wdbc.pkl", 'rb') as f:
    data = pickle.load(f)
data_df = pd.DataFrame(data)

# for key in data_df.keys():
#     plot_density(key)

print('Random forest')
RandomForestClassifier.classify(data_df)
print('SVC')
SVM.classify(data_df)
print('Rule based')
RuleBased.classify(data_df)
