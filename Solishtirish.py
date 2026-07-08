import streamlit as st
import pandas as pd
import plotly.express as px
from translate_columns import column_translate

# ===========================================
# Sahifa sozlamalari
# ===========================================

st.set_page_config(
    page_title="Solishtirish",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Ko'rsatkichlarni solishtirish")

# ===========================================
# CSV yuklash
# ===========================================

@st.cache_data
def load_data():

    df = pd.read_csv("bankrotlik_data.csv")

    df.rename(columns=column_translate, inplace=True)

    return df


df = load_data()

# ===========================================
# Faqat sonli ustunlar
# ===========================================

numeric_df = df.select_dtypes(include="number")

columns = numeric_df.columns.tolist()

st.sidebar.header("Ustunlarni tanlang")

col1 = st.sidebar.selectbox(
    "1-ustun",
    columns,
    index=1
)

col2 = st.sidebar.selectbox(
    "2-ustun",
    columns,
    index=2
)

# ===========================================
# O'rtacha qiymatlar
# ===========================================

avg1 = round(numeric_df[col1].mean(),3)
avg2 = round(numeric_df[col2].mean(),3)

c1,c2 = st.columns(2)

c1.metric(col1,avg1)

c2.metric(col2,avg2)

st.divider()

# ===========================================
# Bar Chart
# ===========================================

chart = pd.DataFrame({

    "Ko'rsatkich":[col1,col2],

    "Qiymat":[avg1,avg2]

})

fig = px.bar(

    chart,

    x="Ko'rsatkich",

    y="Qiymat",

    text="Qiymat",

    title="O'rtacha qiymatlarni solishtirish"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ===========================================
# Line Chart
# ===========================================

st.subheader("📈 Line Chart")

line_df = numeric_df[[col1,col2]].head(100)

st.line_chart(line_df)

# ===========================================
# Scatter Plot
# ===========================================

st.subheader("📉 Scatter Plot")

fig2 = px.scatter(

    numeric_df,

    x=col1,

    y=col2,

    color=numeric_df[col1],

    title=f"{col1} va {col2}"

)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ===========================================
# Statistika
# ===========================================

st.subheader("📋 Statistik ma'lumot")

stats = pd.DataFrame({

    "Ko'rsatkich":[col1,col2],

    "Minimum":[
        numeric_df[col1].min(),
        numeric_df[col2].min()
    ],

    "Maksimum":[
        numeric_df[col1].max(),
        numeric_df[col2].max()
    ],

    "O'rtacha":[
        avg1,
        avg2
    ],

    "Median":[
        numeric_df[col1].median(),
        numeric_df[col2].median()
    ],

    "Standart og'ish":[
        round(numeric_df[col1].std(),3),
        round(numeric_df[col2].std(),3)
    ]

})

st.dataframe(
    stats,
    use_container_width=True
)

# ===========================================
# CSV yuklab olish
# ===========================================

csv = numeric_df[[col1,col2]].to_csv(index=False).encode("utf-8")

st.download_button(

    "📥 Solishtirilgan ma'lumotni yuklab olish",

    csv,

    "solishtirish.csv",

    "text/csv"

)
