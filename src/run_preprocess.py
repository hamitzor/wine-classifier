"""Script for preprocessing and analysis"""
if __name__ == "__main__":
    import pandas as pd
    import analysis
    from config import *
    from draw import *
    from sklearn.model_selection import train_test_split

    # Read train dataset
    train = pd.read_csv(train_file)

    # Extract features for pda and lda
    train_feature_values = train[feature_columns].values
    # Extract target values (Class values) for pda and lda
    target_values = train['Class'].values

    # lda without pca
    lda1, lda_without_pca_df = analysis.lda(
        train_feature_values, target_values)

    print lda1.score(train_feature_values, target_values)

    # draw result
    draw(lda_without_pca_df, 'Wine Classification - LDA without PCA')

    # apply pca
    principal_components = analysis.pca(train_feature_values)

    # after pca apply lda
    lda2, lda_df = analysis.lda(principal_components, target_values)

    print lda2.score(principal_components, target_values)

    # draw result
    draw(lda_df, 'Wine Classification - LDA with PCA')

    exit(0)
