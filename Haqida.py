import streamlit as st

st.set_page_config(
    page_title="Haqida",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ Loyiha haqida")

st.markdown("""
# Korxonalar bankrotligini tahlil qilish tizimi

Ushbu dastur korxonalarning moliyaviy ko'rsatkichlari asosida
bankrotlik ehtimolini aniqlash uchun ishlab chiqilgan.

Dastur Streamlit platformasi yordamida yaratilgan.
""")

st.divider()

c1,c2 = st.columns(2)

with c1:

    st.subheader("Loyiha imkoniyatlari")

    st.success("Dashboard")

    st.success("Dataset")

    st.success("Filtrlash")

    st.success("Solishtirish")

    st.success("Prognoz")

    st.success("CSV yuklab olish")

with c2:

    st.subheader("Ishlatilgan texnologiyalar")

    st.info("Python")

    st.info("Streamlit")

    st.info("Pandas")

    st.info("Plotly")

    st.info("Scikit-learn")

st.divider()

st.subheader("Muallif")

st.write("""
**Talaba:** Maqsuda Abdijabborova

**Mavzu:**

Korxonalar bankrotligini sun'iy intellekt yordamida tahlil qilish va prognozlash.
""")

st.divider()

st.caption("© 2026")
