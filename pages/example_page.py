#hashmark
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from sidebar import init_sidebar

init_sidebar()

@st.cache_data
def load_data():
    df = pd.read_csv('./datasets/bus_delay_notices.csv')
    df = df.rename(columns = {'Bus Route':'route', 'Delay Notice Time':'start',
                              'Delay End Notice Time':'end', 'Time Delayed':'time',
                              'Notes':'cause'})
    df['start'] = pd.to_datetime(df['start'])
    df['end'] = pd.to_datetime(df['end'])
    df['mins'] = [np.dot([60, 1], pd.to_numeric(time.split(':'))) for time in df['time']]
    return df

def by_bus_route(data):
    time_by_route = data.groupby('route').agg({'mins':'sum'}).sort_values(by='mins', ascending = False)
    fig, ax = plt.subplots(figsize=(5, 6))
    ax.set_title("Plot Title")
    ax.set_xlabel("Var 1")
    ax.set_ylabel("Var 2")
    plt.bar(x = time_by_route.index, height = time_by_route['mins'])
    return(fig)

delays = load_data()

st.dataframe(delays)

st.write(delays.dtypes)

fig = by_bus_route(delays)

st.pyplot(fig)