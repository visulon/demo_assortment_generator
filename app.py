import streamlit as st
import pickle
import requests
import numpy as np

df = pickle.load(open('data.pkl','rb'))
df = df.head(100)

st.title("Assortment Recommendation System")

AssortmentName = df['AssortmentName'].values

selected_Assortment = st.selectbox("Select a character",AssortmentName)

Assortment_id = np.where(df['AssortmentName'].values == selected_Assortment)[0][0]
x = df[['x','y']].values

distances = []
for i in range(len(x)):
    distances.append(np.linalg.norm(x[Assortment_id] - x[i]))

recommended_id = []
for i in range(5):
    x = sorted(list(enumerate(distances)),key=lambda x:x[1])[i][0]
    recommended_id.append(i)
recommended_Assortment = df['AssortmentName'].values[recommended_id]

st.text(recommended_Assortment)