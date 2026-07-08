
"""Bu fayl barcha sahifalarda CSV ni bir xil usulda yuklash uchun kerak."""

import pandas as pd
from translate_columns import column_translate
import streamlit as st


@st.cache_data
def load_data():

    df = pd.read_csv("bankrotlik_data.csv")

    df.rename(columns=column_translate, inplace=True)

    return df
