import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.impute import SimpleImputer
from joblib import dump

# Load the password dataset from the given file path
data_path = '/Users/fupengzhao/Desktop/CSE 8A/Project/data/data.csv'
password_data = pd.read_csv(data_path, on_bad_lines='skip')

# Get rid of any repeated data and shuffle everything to ensure randomness
password_data = password_data.drop_duplicates().sample(frac=1, random_state=42)

# Create a new table to keep track of different characteristics of passwords
features_data = pd.DataFrame()
features_data['length'] = password_data['password'].str.len()  # How long the password is
features_data['uppercase_letters'] = password_data['password'].str.count(r'[A-Z]')  # Count of uppercase letters
features_data['lowercase_letters'] = password_data['password'].str.count(r'[a-z]')  # Count of lowercase letters
features_data['digits'] = password_data['password'].str.count(r'[0-9]')  # Count of digits
features_data['special_characters'] = password_data['password'].str.count(r'\W')  # Count of special characters like @, #
features_data['numerical_characters'] = password_data['password'].str.contains(r'[0-9]').fillna(False).astype(int)  # Whether the password contains numbers
features_data['alphabetical_characters'] = password_data['password'].str.contains(r'[a-zA-Z]').fillna(False).astype(int)  # Whether the password contains letters

# Split the data into inputs (X) for the model and outputs (y) it should predict
X = features_data
y = password_data['strength']

# Set up a tool that replaces missing data with zeros
imputer = SimpleImputer(strategy='constant', fill_value=0)

# Use the tool to fix any missing values in our input data
X = imputer.fit_transform(X)

# Prepare a Random Forest Classifier model and evaluate how well it does using cross-validation
model = RandomForestClassifier(n_estimators=10, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=5)

# Divide the data into a part for training the model and another part for testing it
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Use the training data to teach the model
model.fit(X_train, y_train)

# Find out which characteristics of passwords the model thinks are most important
feature_importances = model.feature_importances_

# Check the model's predictions against the actual password strengths
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Save the trained model to a file so we can use it later without having to retrain it
dump(model, '/Users/fupengzhao/Desktop/CSE 8A/Project/trained model/model.joblib')
print('Model training complete.')