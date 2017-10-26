import pandas as pd

data = pd.read_csv("https://s3.amazonaws.com/demo-datasets/wine.csv")
data.columns
numeric_data = data.drop('color',1)
numeric_data = (numeric_data - numeric_data.mean()) / numeric_data.std(ddof=0)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit(numeric_data).transform(numeric_data)

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]
y = principal_components[:,1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1"); plt.ylabel("Principal Component 2")
plt.show()

def accuracy(predictions, outcomes):
    size = len(predictions)
    hit = 0
    for x in range(size):
        if predictions[x] == outcomes[x]:
            hit = hit + 1
    return (hit/size)

x = np.array([1,2,3])
y = np.array([1,2,4])
print( accuracy(x,y) )

y = data["high_quality"]
x = np.zeros(len(x))
print(accuracy(x,y))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, data['high_quality'])
library_predictions = knn.predict(numeric_data)
print ( accuracy(library_predictions, data['high_quality']) )

n_rows = data.shape[0]
random.seed(123)
selection = random.sample( range(n_rows), 10 )

predictors = np.array(numeric_data)
outcomes = np.array(data["high_quality"])
my_predictions = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors[selection]])
percentage = accuracy(my_predictions, data.high_quality[selection])
print(percentage)





