# Used Car Price Prediction Analysis

This report summarizes the analysis conducted on the **Pakwheels Used Car Dataset** to predict used car prices.

## Data Preprocessing

### Key Steps:
1. **Dropped Column**:
   - The `assembly` column was removed due to a high percentage of missing values.

2. **Imputed Missing Values**:
   - Filled missing values in the `body`, `fuel`, and `color` columns with the most frequent value (mode).
   - Filled missing values in the `year` and `engine` columns with the median value.
   - Removed rows where the target variable `price` was missing.

3. **Categorical Variable Encoding**:
   - Converted categorical variables such as `city`, `body`, `make`, `model`, `transmission`, `fuel`, `color`, and `registered` into numerical values using one-hot encoding.

4. **Standardization**:
   - Standardized the numerical features, including `year`, `engine`, `mileage`, and `price`, to ensure they are on the same scale.

5. **Boolean Conversion**:
   - Converted all boolean columns to 1 and 0 for model compatibility.

## Exploratory Data Analysis

### Box Plot of Price
A box plot was created to visualize the distribution of the `price` variable, highlighting the presence of outliers and the overall range of prices in the dataset.

### Scatter Plot of Mileage vs. Price
A scatter plot was used to examine the relationship between `mileage` and `price`. This visualization helped identify trends or patterns that could influence the predictive models.

## Model Training and Evaluation

Three different regression models were trained and evaluated on the preprocessed dataset:

### 1. Decision Tree Regression
- The Decision Tree model surpassed Linear Regression, demonstrating lower error and improved predictive accuracy.

### 2. Support Vector Regression (SVR)
- Support Vector Regression also delivered solid results, though with a higher error compared to the Decision Tree model.

### 3. Linear Regression
- Linear Regression served as a baseline model with moderate performance.

### Cnclusion
The performance of each model was evaluated using the Mean Squared Error (MSE) and the R² Score. These metrics provided insights into how well each model predicted the prices of used cars based on the available features.
