import streamlit as st
import pickle

movies = pickle.load(open('movies.pkl', 'rb'))

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(max_features=5000, stop_words="english")

vectors = cv.fit_transform(movies["tags"]).toarray()

similarity = cosine_similarity(vectors)


st.set_page_config(page_title="CineMatch AI",page_icon="🎬",layout="wide")
st.markdown("<h1 style='text-align: center;'>🎬 CineMatch AI</h1>",unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray;'>Discover your next favorite movie</p>",unsafe_allow_html=True)

selected_movie = st.selectbox("🎥 Choose a movie",movies['title'].values)

def recommend(movie):
    rnum = movies.index[movies['title'].str.lower() == movie.lower()][0]
    data = list(enumerate(similarity[rnum]))
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)[1:6]
    recommended_movies = []
    for i in sorted_data:
        recommended_movies.append((movies.iloc[i[0]].id, movies.iloc[i[0]].title))
    return (recommended_movies)

import requests
@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=461356b6f4aae5ca2a2b42b81a48c506"

    response = requests.get(url)

    print(response.status_code)
    data = response.json()
    if data["poster_path"] is None:
        return None
    full_url = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return full_url


left, center, right = st.columns([2,1,2])

with center:
    recommend_clicked = st.button("🎥 Recommend")


if recommend_clicked:
    with st.spinner("Finding similar movies..."):
        columns = st.columns(5)
        recommendations = recommend(selected_movie)

        for column, (movie_id, title) in zip(columns, recommendations):
            with column:
                poster_url = fetch_poster(movie_id)
                if poster_url:
                    st.image(poster_url, use_container_width=True)
                st.write(title)
