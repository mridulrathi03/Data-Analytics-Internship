# Emoji Prediction Using Machine Learning

## Objective

Build a machine learning model capable of predicting appropriate emojis based on the content of text messages.

## Dataset

* Emoji Prediction Dataset
* 70,000 text samples
* 20 emoji categories
* Text messages mapped to numerical emoji labels

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook

## Project Workflow

1. Loaded and explored the dataset.
2. Analyzed emoji label distribution.
3. Performed text preprocessing.
4. Applied TF-IDF Vectorization to convert text into numerical features.
5. Split the dataset into training and testing sets.
6. Trained multiple machine learning models:

   * Logistic Regression
   * Naive Bayes
   * Random Forest Classifier
   * K-Nearest Neighbors (KNN)
7. Compared model performance using accuracy scores.
8. Evaluated the best-performing model using a confusion matrix and classification report.

## Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 31.50%   |
| Random Forest       | 29.60%   |
| Naive Bayes         | 28.96%   |
| KNN                 | 17.11%   |

## Key Findings

* Logistic Regression achieved the highest accuracy of 31.50%.
* The dataset contained 20 emoji categories, making it a challenging multi-class classification problem.
* TF-IDF vectorization successfully transformed textual data into machine-readable features.
* The model was able to learn relationships between text content and emoji labels.
* Class imbalance affected prediction performance for some emoji categories.

## Conclusion

This project demonstrated the application of Natural Language Processing (NLP) and machine learning techniques for emoji prediction. By using TF-IDF vectorization and classification algorithms, the model successfully predicted emojis from textual content and provided practical experience in multi-class text classification.

## Author

**Mridul Rathi**

B.Tech CSE (Data Science)

