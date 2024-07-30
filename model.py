import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

def preprocess_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Encoding categorical variables
    label_encoders = {}
    for column in ['gender', 'smoking_history']:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
    
    # Separating features and target variable
    X = df.drop('diabetes', axis=1)
    y = df['diabetes']
    
    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y, label_encoders, scaler

def train_and_save_model(file_path):
    X, y, label_encoders, scaler = preprocess_data(file_path)
    
    # Splitting the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save the model and preprocessing objects
    joblib.dump(model, 'model.pkl')
    joblib.dump(label_encoders, 'label_encoders.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    
if __name__ == "__main__":
    train_and_save_model('diabetes_data.csv')
