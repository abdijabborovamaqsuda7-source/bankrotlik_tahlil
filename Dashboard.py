import streamlit as st
import pandas as pd
import plotly.express as px
from translate_columns import column_translate
from utils import load_data

df = load_data()

# ==============================
# Sahifa sozlamalari
# ==============================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard")

# ==============================
# CSV yuklash
# ==============================

@st.cache_data
def load_data():

    df = pd.read_csv("bankrotlik_data.csv")

    df.rename(columns=column_translate, inplace=True)

    return df


df = load_data()

# ==============================
# Asosiy statistikalar
# ==============================

total = len(df)

if "Bankrot_holati" in df.columns:

   bankrupt = int(df["Bankrot_holati"].sum())

else:

    bankrupt = 0

active = total - bankrupt

percent = round(bankrupt / total * 100, 1)

# ==============================
# Statistik kartalar
# ==============================

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "🏢 Jami korxonalar",
    total
)

c2.metric(
    "❌ Bankrot",
    bankrupt
)

c3.metric(
    "✅ Faol",
    active
)

c4.metric(
    "📈 Bankrotlik %",
    f"{percent}%"
)

st.divider()

# ==============================
# Bar Chart
# ==============================

chart = pd.DataFrame({

    "Holat":[

        "Bankrot",

        "Faol"

    ],

    "Soni":[

        bankrupt,

        active

    ]

})

fig = px.bar(

    chart,

    x="Holat",

    y="Soni",

    text="Soni",

    title="Korxonalar holati"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# ==============================
# O'rtacha qiymatlar
# ==============================

numeric = df.select_dtypes(include="number")

st.subheader("📋 O'rtacha moliyaviy ko'rsatkichlar")

mean_df = numeric.mean().round(3)

st.dataframe(

    mean_df,

    use_container_width=True

)

st.divider()

# ==============================
# Statistik jadval
# ==============================

st.subheader("📊 Statistik tahlil")

st.dataframe(

    numeric.describe().round(2),

    use_container_width=True

)
