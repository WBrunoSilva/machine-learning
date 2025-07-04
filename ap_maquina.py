import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt , plotly.express as px
import pickle

from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split , cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score, accuracy_score

iris = load_iris()

def label(x):
  labels = iris.target_names
  return labels[x]

iris_df = pd.DataFrame(iris.data, columns= iris.feature_names)
iris_df['class_codes'] = iris.target
iris_df['class'] = iris_df['class_codes'].apply(lambda x: label(x))

iris_df

for c in iris_df.columns:
  boxfig = px.box(iris_df, x= c, color= 'class', title='Boxplot of' +c)
  boxfig.show()
  histfig = px.histogram(iris_df, x= c, color= 'class', title= 'Histograma of' +c)
  histfig.show()

num_columns = iris_df.select_dtypes(include= 'number')
to_standadize = num_columns.columns.tolist()
to_standadize.remove('class_codes')
scaler = MinMaxScaler((0,1))
iris_df[to_standadize] = scaler.fit_transform(iris_df[to_standadize])

fig = px.scatter_matrix(iris_df, color = 'class', width= 1100, height= 1100)
fig.show()

pca_comp = 2
pca = PCA(n_components=pca_comp)
feature_columns = [c for c in iris_df.columns if c not in ['class','calss_codes']]
pca_iris_df = iris_df[feature_columns]
pca_iris_df = pd.DataFrame(pca.fit_transform(pca_iris_df), columns=['pc_'+str(i) for i in range(0,pca_comp)])
pca_iris_df['class_codes'] = iris_df['class_codes']

pca_iris_df

freature_columns = [c for c in pca_iris_df.columns if c != 'class_codes']
x_train, x_test, y_train,y_test = train_test_split(
                                    pca_iris_df[freature_columns],
                                    pca_iris_df['class_codes'],
                                    test_size= 0.2,
                                    random_state= 42
)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))
clf.feature_importances_

cv_result = cross_val_score(clf, pca_iris_df[freature_columns], pca_iris_df['class_codes'], cv=5 ,scoring= 'f1_weighted')
print("CV Result:", cv_result.round(3))
print("CV Mean:", round(cv_result.mean(),3))
print("CV Std:", round(cv_result.std(),3))

y_true = y_test.values
y_pred = clf.predict(x_test)
cm = confusion_matrix(y_true, y_pred)

print(cm)

x_labels = ['Pred'+str(c) for c in pca_iris_df['class_codes'].unique()]
y_labels = ['True'+str(c) for c in pca_iris_df['class_codes'].unique()]
px.imshow(cm, x= x_labels, y= y_labels, title= 'Confusion Matrix')

f1 = f1_score(y_true, y_pred, average='weighted')
pr = precision_score(y_true, y_pred, average='weighted')
re = recall_score(y_true, y_pred, average='weighted')
acrr = accuracy_score(y_true, y_pred)
metrics = {
     "f_measure": round(f1,3),
     "precision": round(pr,3),
     "recall": round(re,3),
     "accuracy": round(acrr,3)
}

print(metrics)

with open('classifier.pkl','wb') as fid:
  pickle.dump(clf, fid)

with open('classifier.pkl', 'rb')as fid:
  clf_loaded = pickle.load(fid)

clf_loaded.predict(x_test[0:1])
