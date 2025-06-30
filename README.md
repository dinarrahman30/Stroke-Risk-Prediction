# Dashboard Stroke Risk Prediction
Author: [Dinar Wahyu Rahman](https://www.linkedin.com/in/dinar-wahyu-rahman)


| | Description |
| ----------- | ----------- |
| Dataset | [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) |
| Problem | According to the World Health Organization (WHO), stroke is the second leading cause of death worldwide, accounting for approximately 11% of all deaths. |
| Machine Learning Solution | The proposed solution is to build a machine learning-based classification model to predict whether a patient is at high risk of stroke (1) or not (0). This is done by analyzing risk attributes such as age, hypertension history, average glucose level, smoking status, and occupation. This model can assist medical professionals in taking preventive actions earlier. |
| Processing Method | * **Data preprocessing**: Perform imputation for missing values (especially in the `bmi` column). <br> * Apply a resampling technique to the training data to fix the imbalance. <br> * **SMOTE (Synthetic Minority Over-sampling Technique)**: A technique to handle imbalanced classification problems by synthesizing new examples for the minority class. <br> * Use `LabelEncoder()` to convert categorical data into a numerical format. Example: 'Male' becomes 0 and 'Female' becomes 1. <br> * Split the dataset into training (80%) and testing (20%) sets to evaluate model performance. |
| Model Architecture | We used several machine learning models, including: <br> * **Logistic Regression**: This model serves as the baseline for binary classification. It's suitable for linear and interpretable problems, but can be limited for more complex, non-linear data. <br> * **Random Forest**: An ensemble of decision trees that can capture complex interactions and is more robust against overfitting than a single decision tree. <br> * **XGBoost (without tuning)**: A powerful gradient boosting algorithm widely used in ML competitions. It builds models iteratively by correcting previous errors. <br> * **XGBoost (after tuning with GridSearchCV)**: After hyperparameter tuning, XGBoost’s performance—especially its recall for the minority class (stroke)—usually improves significantly. |
| Evaluation Metrics | * **Accuracy**: Measures overall prediction performance. <br> * **Precision**: Ensures the model does not frequently misclassify non-stroke patients as stroke. <br> * **Recall (Sensitivity)**: Ensures the model detects as many high-risk stroke patients as possible. <br> * **F1-Score**: Harmonic mean of precision and recall for balanced evaluation. |
| Model Performance | * The **tuned XGBoost** model achieved the best results, especially in detecting stroke cases (minority class). <br> * **Random Forest** also performed well and consistently. <br> * **Logistic Regression** works well as a baseline but is less suitable for complex data. <br> * The final model selection should consider the trade-off between accuracy, recall, and interpretability, depending on medical/business needs. <br> If the priority is detecting stroke cases (minimizing false negatives), then **recall for class 1 (stroke)** is the key metric to monitor. |
| Demo/Notebook | * [Demo Prototype](https://stroke-risk-prediction-web.up.railway.app/). <br> * [Modeling Notebook](https://colab.research.google.com/drive/11zbHEcZnVXXD-Fqe_FPWvMxwJFWk4QIO?usp=sharing). |


#### Website Appearance
![image](https://github.com/user-attachments/assets/cc42a7a5-0a7b-4f0d-9b81-9b20f4bf7a1b)

