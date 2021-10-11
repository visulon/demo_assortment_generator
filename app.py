import streamlit as st
import pickle
import requests
import numpy as np

df = pickle.load(open('data.pkl','rb'))
df = df.head(274)

st.title("Assortment Recommendation System")

AssortmentName = df['AssortmentName'].values

selected_Assortment = st.selectbox("Select a Assortment",AssortmentName)

# fetch closest match
Assortment_id = []
for i in range(5):
    a = np.where(df['AssortmentName'].values == selected_Assortment)[0][0]
    Assortment_id.append(a)
x = df[['x','y']].values

distances = []
for i in range(len(x)):
    distances.append(np.linalg.norm(x[Assortment_id] - x[i]))



recommended_id = []
for i in range(5):
    b = sorted(list(enumerate(distances)),key=lambda x:x[1])[i][0]
    recommended_id.append(b)

recommended_Assortment = df['AssortmentName'].values[recommended_id]

st.text(recommended_Assortment)