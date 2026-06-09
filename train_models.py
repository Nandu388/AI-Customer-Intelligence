import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# LOAD DATA
data = pd.read_csv("data/customers.csv")

# ==========================
# KMEANS SEGMENTATION
# ==========================

X_cluster = data[['income', 'spending_score']]

kmeans = KMeans(
    n_clusters=5,
    random_state=42
)

kmeans.fit(X_cluster)

# SAVE MODEL
joblib.dump(
    kmeans,
    "models/kmeans_model.pkl"
)

print("KMeans model saved.")

# ==========================
# CHURN PREDICTION MODEL
# ==========================

X = data[
    [
        'income',
        'spending_score',
        'tenure'
    ]
]

y = data['churn']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("Model Accuracy:", accuracy)

# SAVE MODEL
joblib.dump(
    model,
    "models/churn_model.pkl"
)

print("Churn model saved.")