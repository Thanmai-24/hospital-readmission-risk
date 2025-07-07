import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

df = pd.read_csv('features/final.csv')

X = df.drop(columns=['Readmission'])
y = df['Readmission']

model = RandomForestClassifier(class_weight='balanced', random_state=42)
model.fit(X, y)

print("✅ Model trained.")

os.makedirs('models', exist_ok=True)
pickle.dump(model, open('models/model.pkl', 'wb'))
print("✅ Model saved.")
