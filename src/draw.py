import matplotlib.pyplot as plt


targets = [1, 2, 3]
colors = ['r', 'g', 'b']


def draw(data, title):
    fig = plt.figure(figsize=(8, 8))
    subplot = fig.add_subplot(1, 1, 1)
    subplot.set_xlabel('Principal Component 1', fontsize=15)
    subplot.set_ylabel('Principal Component 2', fontsize=15)
    subplot.set_title(title, fontsize=20)
    for target, color in zip(targets, colors):
        indicesToKeep = data['Class'] == target
        subplot.scatter(data.loc[indicesToKeep, 'PC1'],
                        data.loc[indicesToKeep, 'PC2'], c=color, s=15)
    subplot.legend(targets)
    subplot.grid()
    plt.show()
