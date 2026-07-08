import streamlit as st
import pandas as pd

from translate_columns import column_translate

# ==========================
# Sahifa sozlamalari
# ==========================

st.set_page_config(
    page_title="Dataset",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Dataset")

# ==========================
# CSV yuklash
# ==========================

@st.cache_data
def load_data():

    df = pd.read_csv("bankrotlik_data.csv")

    df.rename(columns=column_translate, inplace=True)

    return df


df = load_data()

# ==========================
# Umumiy ma'lumot
# ==========================

st.success("CSV fayli muvaffaqiyatli yuklandi.")

c1, c2, c3 = st.columns(3)

c1.metric("Jami satr", len(df))

c2.metric("Jami ustun", len(df.columns))

c3.metric("Bo'sh qiymatlar", df.isnull().sum().sum())

st.divider()

# ==========================
# Ustun tanlash
# ==========================

st.subheader("Ko'rsatiladigan ustunlar")

selected_columns = st.multiselect(

    "Kerakli ustunlarni tanlang",

    df.columns,

    default=df.columns[:8]

)

if len(selected_columns) == 0:

    st.warning("Kamida bitta ustun tanlang.")

    st.stop()

filtered_df = df[selected_columns]

# ==========================
# Qidiruv
# ==========================

st.subheader("Qidiruv")

search = st.text_input(
    "Qidirish uchun qiymat kiriting"
)

if search:

    mask = filtered_df.astype(str).apply(

        lambda x: x.str.contains(

            search,

            case=False,

            na=False

        )

    )

    filtered_df = filtered_df[mask.any(axis=1)]

# ==========================
# Nechta satr ko'rsatish
# ==========================

rows = st.slider(

    "Ko'rsatiladigan satrlar soni",

    5,

    100,

    20

)

st.divider()

st.subheader("Dataset")

st.dataframe(

    filtered_df.head(rows),

    use_container_width=True

)

# ==========================
# CSV yuklab olish
# ==========================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(

    label="📥 CSV yuklab olish",

    data=csv,

    file_name="dataset.csv",

    mime="text/csv"

)

st.divider()

# ==========================
# Statistik ma'lumot
# ==========================

st.subheader("Tanlangan ustunlar haqida")

st.write(filtered_df.describe(include="all"))
