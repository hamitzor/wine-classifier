from os import path


file_name = 'wine'

file = path.abspath('../data/'+file_name+'.csv')
preprocessed_file = path.abspath(
    '../data/'+file_name+'-preprocessed.csv')
train_file = path.abspath('../data/'+file_name+'-train.csv')
test_file = path.abspath('../data/'+file_name+'-test.csv')

# feature columns
feature_columns = ["Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids",
                   "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]
