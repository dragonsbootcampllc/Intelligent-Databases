import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('../../merged_data.csv')

# Remove any missing values
df.dropna(inplace=True)

# Select the relevant columns
X = df[['Store', 'Category', 'Weekly_Sales']]

# One-hot encode the Category column
X_encoded = pd.get_dummies(X, columns=['Category'])

# Scale the data using StandardScaler and fit_transform
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Use PCA to reduce the dimensionality of the data
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Use the elbow method to determine the optimal number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_pca)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Based on the elbow plot, we can see that the optimal number ofclusters is 3 or 4. For this example, we will choose
# 3 clusters.

# Fit the KMeans clustering model with 3 clusters
kmeans = KMeans(n_clusters=10, init='k-means++', max_iter=300, n_init=10)
y_kmeans = kmeans.fit_predict(X_scaled)
df['Cluster'] = y_kmeans
df.groupby('Cluster')['Weekly_Sales'].describe()
# Add the cluster labels to the X_encoded dataframe
X_encoded['Cluster'] = kmeans.labels_

# Print the results
print(X_encoded.groupby('Cluster').mean())