# Weather Classification Report☁️❄️🌧️🌞
![Alt text](https://storage.googleapis.com/kaggle-datasets-images/1096724/1844417/738dc0eaa6139c390b8bf0dc4c583268/dataset-cover.jpg?t=2021-01-14-09-13-57)


## Dataset Overview

The dataset contains weather information for various cities. The dataset consists of the following columns:

1. Temperature             
2. Humidity                
3. Wind Speed              
4. Precipitation (%)       
5. Cloud Cover             
6. Atmospheric Pressure    
7. UV Index                
8. Season                  
9. Visibility (km)         
10. Location                
11. Weather Type            

## Preprocessing Steps

1. **Null Value Handling**: 
   - Null values were handled by imputing the mean value for numerical features and the mode value for categorical features.

2. **Categorical Variables**:
   - Categorical variables were encoded using the `LabelEncoder` class from the `sklearn.preprocessing` module.

3. **Normalization and Standardization**:
   - The numerical features were normalized and standardized using the `MinMaxScaler` and `StandardScaler` classes from the `sklearn.preprocessing` module.

4. **Visualization**:
   - The distribution of the target variable was visualized using a count plot. The distribution of numerical features was visualized using pair plots.

5. **Data Splitting**:
   - The dataset was split into training and testing sets for model evaluation.

## Model Evaluation

Three different models were applied to the dataset:

### 1. Logistic Regression

- **Accuracy**: 0.87
- **Classification Report**:
  - **Precision, Recall, F1-Score, and Support** for each class are detailed.
- **Confusion Matrix**:
  - The confusion matrix shows the counts of true positives, false positives, true negatives, and false negatives.

### 2. Decision Tree

- **Accuracy**: 0.90
- **Classification Report**:
  - **Precision, Recall, F1-Score, and Support** for each class are detailed.
- **Confusion Matrix**:
  - The confusion matrix shows the counts of true positives, false positives, true negatives, and false negatives.

### 3. Random Forest

- **Accuracy**: 0.92
- **Classification Report**:
  - **Precision, Recall, F1-Score, and Support** for each class are detailed.
- **Confusion Matrix**:
  - The confusion matrix shows the counts of true positives, false positives, true negatives, and false negatives.

## Reasons for Choosing These Models

- Logistic Regression: It is a simple and easy-to-understand algorithm that is used for binary classification problems. It is a good starting point for building a machine learning model.

- Decision Tree Classifier: It is a non-linear model that can capture complex relationships in the data. It is also easy to interpret and visualize, which can help in understanding how the model is making predictions.

- Random Forest Classifier: It is an ensemble model that combines multiple decision trees to improve the performance of the model. It is known for its high accuracy and ability to handle large datasets with high dimensionality.


## Models comparison:

All the models have been trained and tested on the same dataset. The accuracy of the models is as follows:

- Logistic Regression: 0.87
- Decision Tree Classifier: 0.90
- Random Forest Classifier: 0.92

The Random Forest Classifier has the highest accuracy among the three models, so it is the best model for this dataset.




## Conclusion

In this project, we have analyzed the weather dataset and built three different machine learning models to classify the weather type based on various features. The Random Forest Classifier performed the best among the three models, with an accuracy of 0.92. The model can be used to predict the weather type based on the input features and can be further improved by tuning hyperparameters and using more advanced techniques.

