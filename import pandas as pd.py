import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Read the data from the Excel spreadsheet
file_path = r'C:\Users\hanna\OneDrive\College Files\Second Semester\ITSCM 180\baseball.xlsx'
data = pd.read_excel(file_path)

# Step 2: Extract the required columns for model building
columns = ['Runs Scored', 'Runs Allowed', 'Wins', 'OBP', 'SLG', 'Team Batting Average', 'Playoffs']
model_data = data[columns]

# Step 3: Split the data into training (1962-2011) and testing (2012) data
train_data = model_data[model_data.index < 2012]  # Training data from 1962 to 2011
test_data = model_data[model_data.index == 2012]  # Testing data for 2012

# Check if training data is not empty
if not train_data.empty:
    # Extract features (X) and target (y) variables for training and testing
    X_train = train_data.drop('Playoffs', axis=1)
    y_train = train_data['Playoffs']
    X_test = test_data.drop('Playoffs', axis=1)
    y_test = test_data['Playoffs']

    # Step 4: Build a logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Step 5: Evaluate the model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    # Step 6: Compare the predicted playoff status to the actual playoff status for the year 2012
    print("Prediction Model:")
    print("Logistic Regression Model Accuracy:", accuracy)
    print("Predicted Playoff Status for 2012:", predictions[0])
    print("Actual Playoff Status for 2012:", y_test.values[0])
else:
    print("Training data is empty. Please check your data filtering/slicing.")

print ('UWW')