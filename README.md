# Diabetes Prediction Web Application

This is a web application built using Python Flask, HTML, and CSS to predict the likelihood of diabetes in individuals based on their health features. The application allows users to input various health-related features, processes this data using a trained machine learning model, and provides a prediction result.

## Features
**User Input Form:** Allows users to input features such as gender, age, hypertension, heart disease, smoking history, BMI, HbA1c level, and blood glucose level.

**Prediction:** Uses a machine learning model to predict whether the user has diabetes or not based on the provided features.

**Results Display:** Shows a summary of the input features and the prediction result on a separate results page.

## Project Structure
    diabetes_prediction/
    │
    ├── app.py # Main Flask application
    ├── model.py # Script to train and save the model
    ├── requirements.txt # Python dependencies  
    │
    ├── static/ # Static files (CSS, JavaScript)
    │ └── style.css # CSS file
    │
    ├── templates/ # HTML templates
    │ ├── index.html # Home page with the form
    │ └── result.html # Page to display the results
    │
    └── data/
    └── diabetes_data.csv # Dataset for training the model

## Installation

## 1. Clone the Repository
    git clone https://github.com/kishorekumar0814/diabetes-prediction.git
    cd diabetes-prediction

## 2. Create a Virtual Environment
    python -m venv venv

## 3. Activate the Virtual Environment
## - On Windows:
    venv\Scripts\activate
## - On macOS/Linux:
    source venv/bin/activate

## 4. Install Dependencies
    pip install -r requirements.txt

## Model Training
Before running the application, you need to train the model and save it.
## 1. Run the Model Training Script
    python model.py
This script will preprocess the data, train the model, and save it to files (model.pkl, label_encoders.pkl, scaler.pkl).

## Running the Application

## 1. Start the Flask Application
    python app.py

## 2. Open Your Browser
Navigate to http://127.0.0.1:5000/ to access the application.

## Usage
 - Enter the required information in the form fields on the home page.
 - Submit the form to get the prediction result.
 - View the results on the result page, which includes a summary of the features and the diabetes prediction.

## Contributing
Feel free to submit issues, suggest improvements, or contribute code via pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the **MIT License** - see the **LICENSE** file for details.

## Acknowledgements
- Scikit-learn for the machine learning model.
- Flask for the web framework.
- Pandas for data manipulation.

## Contact:
If you have any questions or suggestions, feel free to reach out:
- Email: [Email-Me](mailto:kishorekumar1409@example.com)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/kishorekumar1409/)

*Project Report*:[Project report.docx](https://github.com/user-attachments/files/16432283/Project.report.docx)
