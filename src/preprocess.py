"""Script for preprocessing"""
if __name__ == "__main__":
    from modules import args, stdout, filesystem, parser
    from datetime import datetime
    from modules.database import database
    from os import path
    import numpy as np
    import pandas as pd
    from sklearn import preprocessing
    from sklearn.model_selection import train_test_split
    from sklearn.decomposition import PCA
    import matplotlib.pyplot as plt

    args_parser = args.parser

    args = args_parser.parse_args()

    stdout = stdout.Stdout(args.api or args.quiet)

    file_name = 'wine'

    file = path.abspath('../data/'+file_name+'.csv')
    preprocessed_file = path.abspath(
        '../data/'+file_name+'-preprocessed.csv')
    train_file = path.abspath('../data/'+file_name+'-train.csv')
    test_file = path.abspath('../data/'+file_name+'-test.csv')

    # Read original dataset for preprocessing
    df = pd.read_csv(file)

    # feature columns
    features = ["Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids",
                "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]

    # Normalize necessary columns
    df[features] = ((df[features]-df[features].min())/(
        df[features].max()-df[features].min()))

    train, test = train_test_split(df, test_size=0.2)
    df.to_csv(preprocessed_file, index=False)
    train.to_csv(train_file, index=False)
    test.to_csv(test_file, index=False)

    train_values = df.loc[:, features].values

    pca = PCA(n_components=2)

    principal_components = pca.fit_transform(train_values)

    principal_df = pd.DataFrame(data=principal_components, columns=[
        'Principal Component 1', 'Principal Component 2'])

    final_df = pd.concat([principal_df, train[['Class']]], axis=1)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('Principal Component 1', fontsize=15)
    ax.set_ylabel('Principal Component 2', fontsize=15)
    ax.set_title('Wine Classification - 2d PCA Plot', fontsize=20)
    targets = [1, 2, 3]
    colors = ['r', 'g', 'b']
    for target, color in zip(targets, colors):
        indicesToKeep = final_df['Class'] == target
        ax.scatter(final_df.loc[indicesToKeep, 'Principal Component 1'],
                   final_df.loc[indicesToKeep, 'Principal Component 2'], c=color, s=15)
    ax.legend(targets)
    ax.grid()
    plt.show()

    print pca.explained_variance_ratio_

    exit(0)
