import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data

st.set_page_config(
    page_title="Filtrlash",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Korxonalarni filtrlash")

# ==========================
# Ma'lumotlarni yuklash
# ==========================

df = load_data()
st.write(df["Bankrot_holati"].value_counts())

# ==========================
# Sidebar
# ==========================

st.sidebar.header("Filtrlash parametrlari")

# Bankrotlik holati
holat = st.sidebar.selectbox(
    "Bankrotlik holati",
    ["Barchasi", "Bankrot", "Bankrot emas"]
)

# Joriy likvidlik
likvidlik = st.sidebar.slider(
    "Joriy likvidlik koeffitsienti",
    float(df["Joriy_likvidlik_koeffitsienti"].min()),
    float(df["Joriy_likvidlik_koeffitsienti"].max()),
    (
        float(df["Joriy_likvidlik_koeffitsienti"].min()),
        float(df["Joriy_likvidlik_koeffitsienti"].max())
    )
)

# Qarz darajasi
qarz = st.sidebar.slider(
    "Qarz darajasi (%)",
    float(df["Qarz_darajasi_foizi"].min()),
    float(df["Qarz_darajasi_foizi"].max()),
    (
        float(df["Qarz_darajasi_foizi"].min()),
        float(df["Qarz_darajasi_foizi"].max())
    )
)

# ROA
roa = st.sidebar.slider(
    "AKR (ROA)",
    float(df["AKR_C_foiz_va_amortizatsiyagacha"].min()),
    float(df["AKR_C_foiz_va_amortizatsiyagacha"].max()),
    (
        float(df["AKR_C_foiz_va_amortizatsiyagacha"].min()),
        float(df["AKR_C_foiz_va_amortizatsiyagacha"].max())
    )
)

# ==========================
# Filtrlash
# ==========================

filtered = df.copy()

if holat == "Bankrot":
    filtered = filtered[
        filtered["Bankrot_holati"] == 1
    ]

elif holat == "Bankrot emas":
    filtered = filtered[
        filtered["Bankrot_holati"] == 0
    ]

filtered = filtered[
    filtered["Joriy_likvidlik_koeffitsienti"].between(
        likvidlik[0],
        likvidlik[1]
    )
]

filtered = filtered[
    filtered["Qarz_darajasi_foizi"].between(
        qarz[0],
        qarz[1]
    )
]

filtered = filtered[
    filtered["AKR_C_foiz_va_amortizatsiyagacha"].between(
        roa[0],
        roa[1]
    )
]

# ==========================
# Statistikalar
# ==========================

jami = len(df)
filtrlangan = len(filtered)
olib_tashlangan = jami - filtrlangan

c1, c2, c3 = st.columns(3)

c1.metric("🏢 Jami korxonalar", jami)
c2.metric("✅ Filtrlangan", filtrlangan)

st.divider()

# ==========================
# Grafik
# ==========================

counts = filtered["Bankrot_holati"].value_counts()

chart = pd.DataFrame({
    "Holat": ["Bankrot emas", "Bankrot"],
    "Soni": [
        counts.get(0, 0),
        counts.get(1, 0)
    ]
})

fig = px.bar(
    chart,
    x="Holat",
    y="Soni",
    text="Soni",
    color="Holat",
    title="Filtrlangan korxonalar"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================
# Jadval
# ==========================

st.subheader("Filtrlangan ma'lumotlar")

st.dataframe(
    filtered,
    use_container_width=True
)

# ==========================
# CSV yuklab olish
# ==========================

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Filtrlangan CSV ni yuklab olish",
    data=csv,
    file_name="filtrlangan_korxonalar.csv",
    mime="text/csv"
)

# ==========================
# Statistik ma'lumot
# ==========================

st.subheader("Statistik ma'lumot")

st.dataframe(
    filtered.describe(),
    use_container_width=True
)
