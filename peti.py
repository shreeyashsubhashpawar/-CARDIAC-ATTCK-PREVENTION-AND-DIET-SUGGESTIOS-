# Import necessary libraries
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load Heart Attack Dataset
heart_data = pd.read_csv('C:/Users/LENOVO/Downloads/peti/Cardiovascular_Disease_Dataset_main.csv')

# Features and Target
heart_features = ['age', 'gender', 'chestpain', 'restingBP', 'serumcholestrol', 'fastingbloodsugar', 'restingrelectro', 'maxheartrate', 'exerciseangia', 'oldpeak', 'slope', 'noofmajorvessels']
heart_target = 'target'

# Split the data
X_heart = heart_data[heart_features]
y_heart = heart_data[heart_target]
X_train_heart, X_test_heart, y_train_heart, y_test_heart = train_test_split(X_heart, y_heart, test_size=0.2, random_state=42)

# Preprocessing pipeline
preprocessor_heart = ColumnTransformer([
    ('scaler', StandardScaler(), heart_features)
])

# Model pipeline
heart_model = Pipeline([
    ('preprocessor', preprocessor_heart),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train the model
heart_model.fit(X_train_heart, y_train_heart)

# Save the model
joblib.dump(heart_model, 'C:/Users/LENOVO/Downloads/peti/model/heart_attack_model.pkl')
print('Heart Attack Model trained and saved successfully!')

# Load Diet Dataset
diet_data = pd.read_csv('C:/Users/LENOVO/Downloads/peti/expanded_diet_recommendation_dataset.csv')

# Label Encoding
label_encoders = {}
categorical_columns = ['Diet Plan', 'Foods to Include', 'Foods to Avoid']
for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    diet_data[column] = label_encoders[column].fit_transform(diet_data[column])

# Save Label Encoders
joblib.dump(label_encoders, 'C:/Users/LENOVO/Downloads/peti/model/label_encoders.pkl')

# Diet features and target
features_diet = ['age', 'serumcholestrol', 'restingBP', 'slope', 'oldpeak', 'chestpain']
target_diet = ['Diet Plan', 'Foods to Include', 'Foods to Avoid']

X_diet = diet_data[features_diet]
y_diet = diet_data[target_diet]

# Split the data
X_train_diet, X_test_diet, y_train_diet, y_test_diet = train_test_split(X_diet, y_diet, test_size=0.2, random_state=42)

# Train Diet Model
diet_model = RandomForestClassifier(n_estimators=100, random_state=42)
diet_model.fit(X_train_diet, y_train_diet)

# Save the model
joblib.dump(diet_model, 'C:/Users/LENOVO/Downloads/peti/model/diet_model.pkl')
print('Diet Model trained and saved successfully!')
