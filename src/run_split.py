"""Script for splitting dataset into test and train"""
if __name__ == "__main__":
    import pandas as pd
    from config import *
    from sklearn.model_selection import train_test_split

    # Read original dataset for preprocessing
    df = pd.read_csv(file)

    # Normalize necessary columns
    df[feature_columns] = ((df[feature_columns]-df[feature_columns].min())/(
        df[feature_columns].max()-df[feature_columns].min()))

    # Seperate set into test and train sets
    train, test = train_test_split(df, test_size=0.2)

    # Save files
    df.to_csv(preprocessed_file, index=False)
    train.to_csv(train_file, index=False)
    test.to_csv(test_file, index=False)

    exit(0)
