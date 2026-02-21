import os
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "disease_dataset.csv")
data = pd.read_csv(csv_path)

X_text = data["text"]
y = data["disease"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_text)

model = RandomForestClassifier()
model.fit(X, y)

model_path = os.path.join(BASE_DIR, "disease_model.pkl")
joblib.dump((model, vectorizer), model_path)

print("Model trained successfully!")