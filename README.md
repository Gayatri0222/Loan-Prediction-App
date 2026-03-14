
# Loan Prediction App

## Overview
The Loan Prediction App is a machine learning web application that predicts whether a loan application will be approved or rejected based on applicant information. The system analyzes multiple factors such as income, credit history, and employment status to generate predictions.

This project demonstrates how machine learning models can support financial decision making by automating loan eligibility analysis. The application provides a simple and interactive user interface where users can input applicant details and instantly receive prediction results.

The web application is developed using Python and deployed using Streamlit to provide a user friendly interface.

Live Demo [https://loan-prediction-app-f8wmgeucluvwjkgbhdf4qd.streamlit.app/]

---

## Project Objective
The goal of this project is to build a predictive model that helps banks or financial institutions evaluate loan applications quickly and accurately. The model learns patterns from historical loan application data and uses them to predict loan approval outcomes.

---

## Features
- Interactive web interface
- Real time loan approval prediction
- Machine learning based decision system
- Simple form based user input
- Fast and easy deployment

---

## Technologies Used
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Machine Learning

---

## Machine Learning Model
The application uses Logistic Regression, a supervised machine learning algorithm used for binary classification tasks.

The model is trained using historical loan data and learns relationships between applicant features and loan approval decisions.

Steps followed in the model development process:

1. Data collection
2. Data preprocessing
3. Feature selection
4. Model training
5. Model evaluation
6. Deployment using Streamlit

---

## Input Parameters
The model takes several user inputs to make predictions.

- Gender
- Married status
- Number of dependents
- Education
- Self employed status
- Applicant income
- Co applicant income
- Loan amount
- Loan amount term
- Credit history
- Property area

---

## Output
The system predicts whether the loan application will be:

- Approved
- Rejected

---

## Project Structure

```

loan-prediction-app
│
├── app3.py
├── loan_model.pkl
├── dataset.csv
├── requirements.txt
└── README.md

```

Description of files:

app3.py  
Main Streamlit application file that handles the user interface and prediction logic.

loan_model.pkl  
Serialized trained machine learning model.

dataset.csv  
Dataset used for training and testing the model.

requirements.txt  
List of Python dependencies required to run the application.

README.md  
Project documentation.

---

## Installation

Follow these steps to run the project locally.

### 1 Clone the repository

```

git clone [https://github.com/your-username/loan-prediction-app.git](https://github.com/your-username/loan-prediction-app.git)

```

### 2 Navigate to the project folder

```

cd loan-prediction-app

```

### 3 Install required libraries

```

pip install -r requirements.txt

```

### 4 Run the Streamlit application

```

streamlit run app3.py

```

The application will open in your browser automatically.

---

## Deployment

The application can be deployed using Streamlit Cloud by connecting your GitHub repository and selecting the main Streamlit file.

---

## Future Improvements

- Improve model accuracy using advanced algorithms
- Add model evaluation metrics
- Implement data visualization dashboards
- Add authentication system for users
- Deploy using cloud platforms

---

## Author

Gayatri Berde

---

## License

This project is open source and available for learning and educational purposes.
```

A small but important GitHub tip.

At the top of your repository add a **short project description** like this:

Loan Prediction App using Machine Learning and Streamlit to predict loan approval based on applicant data.

If you want, I can also show you how to make your GitHub project **look 10 times more professional** by adding:

* badges
* screenshots
* live app link
* model accuracy section

Those things actually impress recruiters.
