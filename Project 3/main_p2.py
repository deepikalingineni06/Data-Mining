# -*- coding: utf-8 -*-
"""Main_A_p2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13YgWFUiI6jh-2Iqx73xvVyETvtQSDO5W

# Part 1 - Direct Classification

> Connecting Drive
"""

from google.colab import drive

drive.mount('/content/drive/')

"""> Import Libraries"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import StratifiedKFold

"""> Loading Dataset"""

main_nba_dataframe = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Datasets/P2/nba2021.csv')

"""> Splitting Dataset"""

nba_features = main_nba_dataframe.drop(['Player', 'Pos', 'Tm'], axis=1)
nba_labels = main_nba_dataframe['Pos']
nba_features_train, nba_features_test, nba_labels_train, nba_labels_test = train_test_split(nba_features, nba_labels, test_size=0.25)

"""> Decision Tree Fit and Predict"""

main_decision_tree_model = DecisionTreeClassifier()
main_decision_tree_model.fit(nba_features_train, nba_labels_train)
nba_labels_predicted = main_decision_tree_model.predict(nba_features_test)

"""> Accuracy"""

main_accuracy = accuracy_score(nba_labels_test, nba_labels_predicted)
print("Normal Accuracy -", main_accuracy)

"""# Part 2 - With Improvement

> Features and labels
"""

new_combined_features = pd.concat([nba_features_train, nba_features_test])
new_combined_features = new_combined_features.reset_index( drop = True)
new_combined_labels = pd.Series( list(nba_labels_train) + list(nba_labels_test) )

"""> Label Encoding"""

for Loop_Column_Name in new_combined_features.select_dtypes("object"):
    new_combined_features[Loop_Column_Name], Use_Less = new_combined_features[Loop_Column_Name].factorize()

"""> Looking for discreete columns"""

all_discrete_features = new_combined_features.dtypes == int

"""> Finding Mi Score"""

final_mi_scores = mutual_info_classif(new_combined_features, new_combined_labels, discrete_features=all_discrete_features)
final_mi_scores = pd.Series(final_mi_scores, name="MI Scores", index=new_combined_features.columns).sort_values(ascending=False)

"""> Picking only features having Mi Score > 0.05"""

final_features = new_combined_features.loc[:, final_mi_scores > 0.07]

"""> Normal Train Test Split"""

nba_features_train, nba_features_test, nba_labels_train, nba_labels_test = train_test_split(final_features, new_combined_labels, test_size=0.25)

"""> Decision Tree Fit and Predict"""

main_decision_tree_model = DecisionTreeClassifier()
main_decision_tree_model.fit(nba_features_train, nba_labels_train)
nba_labels_predicted = main_decision_tree_model.predict(nba_features_test)

"""> Printing Normal Accuracy"""

main_accuracy = accuracy_score(nba_labels_test, nba_labels_predicted)
print("Normal Accuracy -", main_accuracy)

"""> Confusion Matrix"""

print("Confusion matrix:")
print(pd.crosstab(nba_labels_test, nba_labels_predicted, rownames=['True'], colnames=['Predicted'], margins=True))

"""> 10-fold stratified cross-validation"""

stratified_indexes = StratifiedKFold(n_splits=10)
list_of_accuracies = []

for idx_training, idx_testing in stratified_indexes.split(nba_features, nba_labels):
    nba_features_train, nba_features_test = nba_features.iloc[idx_training], nba_features.iloc[idx_testing]
    nba_labels_train, nba_labels_test = nba_labels.iloc[idx_training], nba_labels.iloc[idx_testing]
    main_decision_tree_model.fit(nba_features_train, nba_labels_train)
    nba_labels_predicted = main_decision_tree_model.predict(nba_features_test)
    main_accuracy = accuracy_score(nba_labels_test, nba_labels_predicted)
    list_of_accuracies.append(main_accuracy)

"""> Accuracy of each Fold"""

print("10 fold Accuracy scores -", list_of_accuracies)

"""> Mean Accuracy"""

print("Mean accuracy:", sum(list_of_accuracies)/len(list_of_accuracies))

