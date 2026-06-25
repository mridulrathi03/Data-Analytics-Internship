# Movie Recommendation System

## Objective

Build a movie recommendation system using movie review data and recommend similar reviews based on their content.

## Tools Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook

## Techniques Used

* TF-IDF Vectorization
* Cosine Similarity
* Content-Based Recommendation

## Data Preprocessing

* Checked for missing values
* Removed duplicate records
* Prepared review text for feature extraction

## Methodology

1. Loaded and explored the IMDB movie review dataset.
2. Converted review text into numerical vectors using TF-IDF.
3. Calculated similarity scores using Cosine Similarity.
4. Built a recommendation function to identify similar reviews.
5. Generated recommendations based on review content.

## Key Findings

* The dataset contained movie reviews and sentiment labels only.
* User ratings and user-movie interaction data were not available.
* A content-based recommendation approach was implemented instead of collaborative filtering.
* TF-IDF and Cosine Similarity successfully identified reviews with similar content.

## Conclusion

A content-based movie recommendation system was developed using TF-IDF Vectorization and Cosine Similarity. The project demonstrated how recommendation systems can be built using textual data when user-rating information is unavailable.

