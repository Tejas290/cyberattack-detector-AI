import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neural_network import MLPClassifier
import joblib

# Load dataset
df = pd.read_csv("labeled_dataset.csv")

# Drop irrelevant columns
drop_cols = ['Flow ID', 'Src IP', 'Dst IP', 'Timestamp', 'Label']  # 'Label' will be handled later
features = df.drop(columns=drop_cols).columns.tolist()

X = df[features]
y = df['Label']

# Encode labels
le = LabelEncoder()
y = le.fit_transform(y)

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/Test split
X_train, _, y_train, _ = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu', solver='adam', max_iter=200, random_state=42)
mlp.fit(X_train, y_train)

# Save model, scaler, and feature names
joblib.dump(mlp, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(features, "features.pkl")  # used later to generate dynamic form