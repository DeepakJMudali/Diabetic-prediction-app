# Diabetes Prediction Web Application

A Flask-based web application that predicts diabetes using logistic regression. This application takes user input for various health metrics and uses a trained machine learning model to predict whether a person is diabetic or not.

## Project Structure

```
.
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── Dataset/                        # Training and test datasets
├── Model/                          # Pre-trained models and scalers
│   ├── modelForPrediction.pkl     # Trained logistic regression model
│   └── StandardScaler.pkl          # Fitted StandardScaler for feature scaling
├── Notebook/                       # Jupyter notebooks for model development
└── templates/                      # HTML templates for the web interface
    └── index.html                  # Homepage and prediction form
```

## Features

- **User-friendly Web Interface**: Simple HTML form to input health metrics
- **Real-time Predictions**: Get instant diabetes predictions based on input data
- **Feature Engineering**: Applies log transformation to specific features (Glucose, BloodPressure, SkinThickness, Insulin, BMI)
- **Data Normalization**: Uses StandardScaler for feature normalization

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. Clone the repository (if applicable) or navigate to the project directory:
   ```bash
   cd projects
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

- **Flask**: Web framework for building the application
- **scikit-learn**: Machine learning library (LogisticRegression, StandardScaler)
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **seaborn**: Data visualization (used in model development)

## Usage

### Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000/
   ```

3. Fill in the health metrics:
   - **Pregnancies**: Number of pregnancies
   - **Glucose**: Plasma glucose concentration
   - **Blood Pressure**: Diastolic blood pressure (mm Hg)
   - **Skin Thickness**: Triceps skin fold thickness (mm)
   - **Insulin**: 2-Hour serum insulin (mu U/ml)
   - **BMI**: Body Mass Index
   - **Diabetes Pedigree Function**: A function that scores diabetes likelihood based on family history
   - **Age**: Age in years

4. Click the prediction button to get results

### Expected Output

- **Diabetic**: If the model predicts the person is diabetic
- **Non-Diabetic**: If the model predicts the person is not diabetic

## Model Details

### Input Features (8 parameters)
1. Pregnancies
2. Glucose
3. BloodPressure
4. SkinThickness
5. Insulin
6. BMI
7. DiabetesPedigreeFunction
8. Age

### Feature Preprocessing
- **Log Transformation**: Applied to Glucose, BloodPressure, SkinThickness, Insulin, and BMI (using `np.log1p()`)
- **Standardization**: All features are scaled using StandardScaler before prediction

### Model Type
- **Algorithm**: Logistic Regression
- **Status**: Pre-trained and ready for inference

## Files

- **app.py**: Main application file containing Flask routes and prediction logic
- **StandardScaler.pkl**: Pre-fitted scaler for normalizing input features
- **modelForPrediction.pkl**: Trained logistic regression model
- **requirements.txt**: List of Python dependencies

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Displays the homepage with prediction form |
| `/predictdata` | POST | Processes form data and returns prediction result |

## Notes

- The model expects input values in specific ranges. Ensure the input values are realistic health metrics.
- Log transformation is applied to numerical features to handle skewed distributions.
- Feature scaling is crucial for logistic regression performance.

## Development

### Model Training (See Notebook folder)
If you want to retrain the model:
1. Navigate to the `Notebook/` folder
2. Review the model development notebooks
3. Regenerate the pickle files (`modelForPrediction.pkl` and `StandardScaler.pkl`)

## Troubleshooting

- **Port already in use**: Change the Flask port in `app.py` or kill the process using port 5000
- **Missing pickle files**: Ensure both `StandardScaler.pkl` and `modelForPrediction.pkl` exist in the `Model/` folder
- **Import errors**: Reinstall dependencies: `pip install -r requirements.txt`

## Future Improvements

- Add data validation and error handling for invalid inputs
- Implement confidence scores for predictions
- Add more detailed health analysis and recommendations
- Create an API endpoint for programmatic access
- Implement model versioning and deployment strategies



## Author

Created as a machine learning project for educational purposes.
