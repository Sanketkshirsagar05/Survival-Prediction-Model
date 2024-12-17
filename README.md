# Survival-Prediction-Model

Website of steamlit : https://survival-prediction-model-n8qmjra3wngeuexe7pqfnv.streamlit.app/

## Overview

The **Survival Prediction Model** leverages machine learning techniques to predict survival probabilities in critical scenarios, such as the Titanic disaster. This project demonstrates how data-driven approaches and classification algorithms can provide insights into survival likelihood based on key features.

## Features

- Implementation of multiple classification algorithms:
  - Logistic Regression
  - Support Vector Machines (SVM)
  - Decision Tree
  - Random Forest
  - K-Nearest Neighbors (KNN)
- Preprocessing of data:
  - Handling missing values
  - Feature scaling
  - Encoding categorical variables
- Evaluation metrics:
  - Accuracy, precision, recall, F1-score, confusion matrices, and ROC-AUC.
- Model optimization using hyperparameter tuning.
- Deployment-ready model pipeline using `joblib`.

## Dataset

The dataset used is the well-known Titanic dataset from [Kaggle](https://www.kaggle.com/c/titanic). It includes the following features:
- **PassengerId**: Unique identifier for each passenger
- **Pclass**: Ticket class (1st, 2nd, 3rd)
- **Sex**: Gender of the passenger
- **Age**: Age of the passenger
- **Fare**: Ticket fare
- **SibSp**: Number of siblings/spouses aboard
- **Parch**: Number of parents/children aboard
- **Embarked**: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)
- **Survived**: Target variable indicating survival (1 = Survived, 0 = Not Survived)

## Requirements

To run the project, ensure you have the following installed:
- Python 3.x
- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`


## Result

![Survival-Prediction-Model](https://github.com/user-attachments/assets/20b82e4c-dff6-4b2d-96f6-79da4487525d)

