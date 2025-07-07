import pandas as pd
import os

# Load CSV
df = pd.read_csv('data/hospital_data.csv')

# Convert gender to numbers
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0, 'Other': 2})

# Convert Readmission to 1/0
df['Readmission'] = df['Readmission'].map({'Yes': 1, 'No': 0})

# Extract diagnosis group
df['Diagnosis_Group'] = df['Diagnosis_Code'].str[:3]

# Drop original diagnosis code
df.drop(columns=['Diagnosis_Code'], inplace=True)

# ✅ Reassign numeric conversions
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Length_of_Stay'] = pd.to_numeric(df['Length_of_Stay'], errors='coerce')
df['Number_of_Procedures'] = pd.to_numeric(df['Number_of_Procedures'], errors='coerce')

# Save cleaned data
os.makedirs('processed', exist_ok=True)
df.to_csv('processed/cleaned.csv', index=False)
print("✅ Preprocessing done.")
