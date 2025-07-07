import pandas as pd
import os

df = pd.read_csv('processed/cleaned.csv')

# Age Grouping
df['Age_Group'] = pd.cut(df['Age'], bins=[17, 30, 45, 60, 75, 90],
                         labels=['18-30', '31-45', '46-60', '61-75', '76-89'])

# One-hot encode
df = pd.get_dummies(df, columns=['Diagnosis_Group', 'Age_Group'])

# Save features
os.makedirs('features', exist_ok=True)
df.to_csv('features/final.csv', index=False)
print("✅ Feature engineering complete.")
