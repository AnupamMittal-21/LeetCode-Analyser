import streamlit as st
import pickle
import pandas as pd

leet_dict = pickle.load(open('leet_dict.pkl','rb'))
df = pd.DataFrame(leet_dict)
st.title("Hey How are you! ")
st.write(df)