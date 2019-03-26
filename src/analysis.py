from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np
import pandas as pd


def pca(values):
    return PCA(n_components=2).fit_transform(values)


def lda(values, targets):
    lda_result = LinearDiscriminantAnalysis(
        n_components=2).fit_transform(values, targets)

    # merge result with target values
    lda_with_classes = [
        np.append(lda_result[i], targets[i]) for i in range(len(lda_result))]

    # return result as DataFrame
    return pd.DataFrame(data=lda_with_classes,
                        columns=['PC1',
                                 'PC2',
                                 'Class'])
