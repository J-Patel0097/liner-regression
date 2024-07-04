import streamlit as st
import pandas as pd
import numpy as np
import pickle

# load the model
clf = pickle.load(open("mymodel.pkl","rb"))

def predict(data):
    clf = pickl.load(open("mymodel.pkl","rb"))
    return clf.predict(data)
    
st.title("Advertising Spends Prediction using Machine Learning")
st.markdown("This Model Identify total spends on advertising")

st.header("Advertising Spends on various Media")
col1,col2 = st.columns(2)

with col1:
    st.text("TV")
    tv = st.slider("Adver, spends on TV", 1.0, 10000.0, 0.5)
    st.text("Radio")
    rd = st.slider("Adver, spends on Radio", 1.0, 10000.0, 0.5)
    st.text("Newspaper")
    newspaper = st.slider("Adver, spends on Newspaper", 1.0, 10000.0, 0.5)

    
st.text('')
if st.button("Seles Prediction "):
    result = clf.predict(np.array([[tv,rd,newspaper]]))
    st.text(result[0])

st.markdown("developed By Jay Patel in daman nilt")