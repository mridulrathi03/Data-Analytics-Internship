# Spam Email Detection

## Objective

Build a machine learning model to classify messages as spam or ham (non-spam) based on their content.

## Tools Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

## Algorithms Used

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Random Forest Classifier
* AdaBoost Classifier

## Data Preprocessing

* Checked for missing values
* Removed duplicate records
* Converted categorical labels into numerical values
* Applied TF-IDF Vectorization to transform text into numerical features

## Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 95.64%   |
| KNN                 | 90.31%   |
| Random Forest       | 98.16%   |
| AdaBoost            | 95.45%   |

## Key Findings

* The dataset contained 5,157 SMS messages.
* Random Forest achieved the highest accuracy.
* The model correctly classified most spam and non-spam messages.
* Text vectorization helped convert message content into machine-learning-friendly features.

## Conclusion

Random Forest achieved the best performance with an accuracy of 98.16%, demonstrating the effectiveness of machine learning techniques for spam detection.

