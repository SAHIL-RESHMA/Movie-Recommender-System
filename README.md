# 🎬 Movie Recommender System (User-Based Collaborative Filtering)

This project implements a movie recommender system using **user-based collaborative filtering**. It analyzes user preferences from historical movie rating data to suggest personalized movie recommendations based on user similarity.

---

## 📌 Key Features

- Developed using **Python**, leveraging libraries such as **Pandas**, **Matplotlib**, and **Seaborn**.
- Built on the **MovieLens 100k** dataset.
- Constructed a **user-item rating matrix**.
- Utilized **Pearson correlation** to compute user similarity.
- Filtered recommendations based on minimum rating thresholds for higher accuracy.

---

## 🧠 Understanding Collaborative Filtering

Collaborative Filtering recommends items by identifying patterns in user interactions:

- **User-Based Filtering**: Finds users with similar preferences and recommends items they liked.
- **Item-Based Filtering** (not covered in this project): Recommends items similar to what a user has liked in the past.

This project focuses on **User-Based Collaborative Filtering**.

---

## 📂 Dataset Overview

**Source**: [MovieLens 100k Dataset](https://grouplens.org/datasets/movielens/)

**Files Used**:
- `u.data`: Contains user ratings (user_id, item_id, rating, timestamp).
- `Movie_Id_Titles`: Maps item_id to movie titles.

---

## ⚙️ How It Works

1. **Data Preprocessing**
   - Load and merge user ratings with movie metadata.
   - Create a pivot table to form the user-item matrix.

2. **Ratings Analysis**
   - Compute the average rating and number of ratings per movie.
   - Filter out movies with low number of ratings for reliable recommendations.

3. **Recommendation Engine**
   - Choose a reference movie (e.g., *Star Wars (1977)*).
   - Compute correlations between this movie and others based on user ratings.
   - Filter out results with low number of ratings and sort by correlation.

---

## 🔍 Sample Output

Recommendations for users who liked **Star Wars (1977)**:

| Movie Title                       | Correlation | Number of Ratings |
|----------------------------------|-------------|-------------------|
| Empire Strikes Back (1980)       | 0.78        | 300               |
| Return of the Jedi (1983)        | 0.76        | 250               |
| Raiders of the Lost Ark (1981)   | 0.74        | 220               |

*Note: Output may vary depending on dataset version and filtering thresholds.*

---

## 📊 Libraries Used

- [`pandas`](https://pandas.pydata.org/)
- [`numpy`](https://numpy.org/)
- [`matplotlib`](https://matplotlib.org/)
- [`seaborn`](https://seaborn.pydata.org/)

---

## 🚀 Future Enhancements

- Integrate **item-based** collaborative filtering.
- Extend to **content-based** filtering using genre or text metadata.
- Deploy as an interactive web app using **Flask** or **Streamlit**.
- Implement real-time recommendations and user interface.

---

## 📈 Evaluation Metrics (Planned)

To evaluate the performance of recommendation algorithms:

- **Precision / Recall / F1-Score**
- **Mean Absolute Error (MAE)**
- **Root Mean Square Error (RMSE)**
- **Coverage**
- **Diversity**

---

## 💼 Real-World Applications

- **Netflix / Prime Video**: Suggest shows or movies based on viewing history.
- **Amazon / Flipkart**: Personalized product recommendations.
- **Spotify / YouTube**: Music/video recommendations.
- **E-learning platforms**: Course or topic suggestions based on interest.

---

## 📄 License

This project is released under the **MIT License**. Feel free to use, modify, and distribute for educational and professional purposes.

---
