"""Script for preprocessing"""
if __name__ == "__main__":
    import pandas as pd
    import analysis
    from config import *
    from draw import *
    from analysis import *
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

    # Extract features for pda and lda
    train_feature_values = train[feature_columns].values
    # Extract target values (Class values) for pda and lda
    target_values = train['Class'].values

    # lda without pca
    lda_without_pca_df = analysis.lda(train_feature_values, target_values)

    # draw result
    draw(lda_without_pca_df, 'Wine Classification - LDA without PCA')

    # apply pca
    principal_components = analysis.pca(train_feature_values)

    # after pca apply lda
    lda_df = analysis.lda(principal_components, target_values)

    # draw result
    draw(lda_df, 'Wine Classification - LDA with PCA')

    exit(0)
