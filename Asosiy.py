import streamlit as st

st.set_page_config(
    page_title="Bankrotlik tahlili",
    page_icon="📊",
    layout="wide"
)
st.write("Test")
st.title("📊 Korxonalar bankrotligini tahlil qilish tizimi")

st.markdown("""
Ushbu dastur korxonalarning moliyaviy ko'rsatkichlari asosida
bankrotlik holatini tahlil qilish uchun ishlab chiqilgan.
""")

st.info("""
👈 Chap tomondagi menyudan kerakli bo'limni tanlang.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Ma'lumotlar",
        "6819"
    )

with col2:
    st.metric(
        "Ustunlar",
        "96"
    )

with col3:
    st.metric(
        "Model",
        "AI"
    )

st.divider()

st.subheader("Loyiha imkoniyatlari")

st.write("""
✅ Dashboard

✅ CSV ko'rish

✅ Filtrlash

✅ Solishtirish

✅ Bar Chart

✅ Bankrotlik prognozi
""")