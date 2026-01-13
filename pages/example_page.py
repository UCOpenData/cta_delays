#hashmark
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sidebar import init_sidebar

init_sidebar()

@st.cache_data
def load_data():
    return pd.read_csv('./datasets/fake_data.csv')

def some_plot_function(data):
    fig, ax = plt.subplots(figsize=(5, 6))
    ax.set_title("Plot Title")
    ax.set_xlabel("Var 1")
    ax.set_ylabel("Var 2")
    ax.scatter(x = data["Var1"], y = data["Var2"])
    return(fig)

df = load_data()

st.dataframe(df)

fig = some_plot_function(df)

st.pyplot(fig)