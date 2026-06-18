# House Price Prediction

## Objective

Predict house prices using machine learning algorithms based on housing features such as area, bedrooms, bathrooms, and location.

## Tools Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

## Algorithms Used

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

## Data Preprocessing

* Removed unnecessary columns
* Handled date features
* Removed records with invalid house prices
* Removed extreme outliers using the IQR method
* Encoded categorical variables

## Model Performance

| Model             | R² Score |
| ----------------- | -------- |
| Linear Regression | 0.7801   |
| Decision Tree     | 0.5145   |
| Random Forest     | 0.7298   |
| Gradient Boosting | 0.7222   |

## Evaluation Metrics

* MAE: 77,486.82
* RMSE: 112,555.29

## Key Findings

* Linear Regression achieved the highest R² score.
* Data cleaning and outlier removal significantly improved model performance.
* House features such as living area, bedrooms, bathrooms, and location contributed to price prediction.

## Conclusion

Linear Regression performed best in this analysis with an R² score of 0.7801. The project demonstrates how machine learning can be used to predict house prices and support real estate decision-making.

