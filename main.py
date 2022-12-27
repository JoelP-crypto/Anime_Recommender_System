import pickle

import pandas as pd
import streamlit as st
import requests


def recommend(Anime):

    anime_index = anime[anime['title'] == Anime].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[2:15]

    recommended_anime = []
    for i in anime_list:
        recommended_anime.append(anime.iloc[i[0]].title)
    return recommended_anime


anime_dict = pickle.load(open('anime_dict.pkl', 'rb'))
anime = pd.DataFrame(anime_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title("Anime Recommendation System")




selected_anime_name= st.selectbox(
    'Select an anime of your liking',
    anime['title'].values
)

if st.button("Recommend ME"):
    recommendations = recommend(selected_anime_name)
    for i in recommendations:
        st.write(i)


