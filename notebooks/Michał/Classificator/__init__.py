from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from DataPreparation import *

# Load the data from a CSV file into a DataFrame
df = loadFromCSV('data.csv')

# Convert 'cmplnt_fr_dt' to datetime, handling errors by setting invalid parsing to NaT (Not a Time)
df['cmplnt_fr_dt'] = pd.to_datetime(df['cmplnt_fr_dt'], errors='coerce')

# Drop rows where 'cmplnt_fr_dt' is NaT (invalid datetime)
df = df.dropna(subset=['cmplnt_fr_dt'])

# Convert 'cmplnt_fr_tm' to datetime using the specified format and extract the time part
df['cmplnt_fr_tm'] = pd.to_datetime(df['cmplnt_fr_tm'], format='%H:%M:%S').dt.time

# Extract the hour from 'cmplnt_fr_tm' and create a new column 'hour'
df['hour'] = df['cmplnt_fr_tm'].apply(lambda x: x.hour)

# Extract additional time-based features from 'cmplnt_fr_dt'
df['day'] = df['cmplnt_fr_dt'].dt.day
df['month'] = df['cmplnt_fr_dt'].dt.month
df['year'] = df['cmplnt_fr_dt'].dt.year

# Filter out rows where the year is less than 2000
df = df[df['year'] >= 2000]

# Extract the day of the week from 'cmplnt_fr_dt' (0 = Monday, 6 = Sunday)
df['day_of_week'] = df['cmplnt_fr_dt'].dt.dayofweek

# Drop rows with any remaining null values
df = df.dropna()

# Encode the 'ofns_desc' column into numerical labels
offense_encoder = LabelEncoder()
df['offense_encoded'] = offense_encoder.fit_transform(df['ofns_desc'])

# Define the feature matrix (X) and the target vector (y)
X = df[['hour', 'day', 'month', 'year', 'day_of_week', 'latitude', 'longitude']]
y = df['offense_encoded']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the RandomForestClassifier with a fixed random state for reproducibility
model = RandomForestClassifier(random_state=42)

# Train the model using the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's performance using various metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

# Print the evaluation metrics
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')
