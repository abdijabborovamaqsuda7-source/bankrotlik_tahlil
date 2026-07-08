import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

st.set_page_config(
    page_title="Prognoz",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Bankrotlik ehtimolini baholash")

# Modelni yuklash
model = joblib.load("bankrot_model.pkl")

st.write("Korxona ko'rsatkichlarini kiriting.")

c1,c2 = st.columns(2)

with c1:

    liquidity = st.number_input(
        "Joriy likvidlik",
        value=1.5
    )

    debt = st.number_input(
        "Qarz koeffitsienti",
        value=0.5
    )

with c2:

    roa = st.number_input(
        "Aktivlar rentabelligi",
        value=0.1
    )

    profit = st.number_input(
        "Operatsion foyda",
        value=0.2
    )

if st.button("Hisoblash"):

    X = pd.DataFrame({
    "Joriy_likvidlik_koeffitsienti": [liquidity],
    "Qarz_darajasi_foizi": [debt],
    "AKR_C_foiz_va_amortizatsiyagacha": [roa],
    "Operatsion_foyda_darajasi": [profit]
})

    probability = model.predict_proba(X)[0][1]

    percent = round(probability*100,2)

    if percent < 40:

        st.success("Korxona barqaror.")

    elif percent < 70:

        st.warning("Korxonada o'rtacha xavf mavjud.")

    else:

        st.error("Bankrotlik xavfi yuqori.")

    st.metric(
        "Bankrotlik ehtimoli",
        f"{percent}%"
    )

    st.progress(percent/100)

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=percent,

        title={'text':"Bankrotlik (%)"},

        gauge={

            'axis':{'range':[0,100]},

            'bar':{'color':'red'},

            'steps':[

                {'range':[0,40],'color':'green'},

                {'range':[40,70],'color':'yellow'},

                {'range':[70,100],'color':'red'}

            ]

        }

    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )
