# 🎬 CineMatch AI

A content-based Movie Recommendation System built using Machine Learning and Natural Language Processing.

🔗 Live Demo: https://cinematch-ai-ml.streamlit.app/

---

## Features

- 🎥 Recommend similar movies instantly
- 🖼️ Fetches movie posters using the TMDB API
- ⚡ Fast recommendations using cosine similarity
- 🚫 Automatically skips movies without posters
- 🌐 Deployed with Streamlit Cloud

---

## Tech Stack

- Python
- Pandas
- Scikit-learn
- CountVectorizer
- Cosine Similarity
- Streamlit
- TMDB API
- Git & GitHub

---

## How It Works

1. Merge movie and credits datasets
2. Clean and preprocess metadata
3. Create a combined text feature (tags)
4. Convert text into vectors using CountVectorizer
5. Compute cosine similarity between all movies
6. Recommend the most similar movies
7. Fetch movie posters dynamically from TMDB

---

## Dataset

TMDB 5000 Movie Dataset

---

## Installation

```bash
git clone https://github.com/AnushRagu/CineMatch-AI.git
cd CineMatch-AI

pip install -r requirements.txt

streamlit run app.py
```

---

## Project Structure

```
CineMatch-AI
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── data
├── notebooks
└── README.md
```

---

## Future Improvements

- User accounts
- Personalized recommendations
- Genre filtering
- Search history
- Trending movie suggestions

---

## Author

**Anush Ragu**

B.Tech Artificial Intelligence & Machine Learning
