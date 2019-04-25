"""Script for naive bayes"""
if __name__ == "__main__":
    from sklearn.naive_bayes import GaussianNB
    import pandas as pd
    from config import *
    import numpy as np

    # Read train dataset
    train = pd.read_csv(train_file)

    # Extract features for pda and lda
    train_feature_values = train[feature_columns].values
    # Extract target values (Class values) for pda and lda
    target_values = train['Class'].values

    gnb = GaussianNB()
    y_pred = gnb.fit(train_feature_values, target_values).predict(
        train_feature_values)

    actual_1 = 0
    actual_2 = 0
    actual_3 = 0

    for example_index in range(len(target_values)):
        actual = target_values[example_index]
        predicted = y_pred[example_index]
        if int(actual) is 1:
            actual_1 = actual_1 + 1
            print actual, predicted

    for example_index in range(len(target_values)):
        actual = target_values[example_index]
        predicted = y_pred[example_index]
        if int(actual) is 2:
            actual_2 = actual_2 + 1
            print actual, predicted

    for example_index in range(len(target_values)):
        actual = target_values[example_index]
        predicted = y_pred[example_index]
        if int(actual) is 3:
            actual_3 = actual_3 + 1
            print actual, predicted

    print actual_1, actual_2, actual_3
    exit(0)
