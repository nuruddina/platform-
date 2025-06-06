import streamlit as st

st.title("My Platform")
st.write("welcome to my platform")
st.write("dghjj")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 15, 25, 30]
})

st.write("Sample DataFrame", df)

plt.plot(df["x"], df["y"])
st.pyplot(plt)
