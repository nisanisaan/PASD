import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime, timedelta
import plotly.graph_objects as go

# ========================================================
# PAGE CONFIG
# ========================================================
st.set_page_config(
    page_title="G-Ture",
    page_icon="✨",
    layout="wide"
)

# ========================================================
# LANGUAGE SWITCHER
# ========================================================
language = st.selectbox(
    "",
    ["🇺🇸 English", "🇮🇩 Indonesia"]
)

# ========================================================
# TRANSLATION
# ========================================================
if language == "🇮🇩 Indonesia":

    text = {

        "hero_title_1": "Prediksi Harga",
        "hero_title_2": "Emas Masa Depan",

        "hero_subtitle":
        "Platform prediksi harga emas berbasis machine learning "
        "dengan tampilan modern, elegan, dan profesional "
        "untuk membantu analisis tren pasar masa depan.",

        "prediction": "Prediksi Harga Emas",

        "prediction_method": "Metode Prediksi",

        "single_day": "Satu Hari",

        "date_range": "Rentang Hari",

        "select_date": "Pilih Tanggal",

        "select_range": "Pilih Rentang Tanggal",

        "analyze_btn": "Analisis Prediksi",

        "result": "Hasil Analisis",

        "recommendation": "Rekomendasi Pasar",

        "chart": "Grafik Prediksi Harga Emas",

        "table": "Data Prediksi",

        "uptrend": "Tren Harga Naik",

        "downtrend": "Tren Harga Turun",

        "market_range": "Estimasi Rentang Harga Pasar",

        "footer": "Luxury Gold Prediction Platform"
    }

else:

    text = {

        "hero_title_1": "Predict Future",
        "hero_title_2": "Gold Prices",

        "hero_subtitle":
        "Luxury gold forecasting platform powered by "
        "machine learning to help analyze future "
        "market trends with elegant visualization "
        "and professional insights.",

        "prediction": "Gold Prediction",

        "prediction_method": "Prediction Method",

        "single_day": "Single Day",

        "date_range": "Date Range",

        "select_date": "Select Date",

        "select_range": "Select Date Range",

        "analyze_btn": "Analyze Gold Prediction",

        "result": "Prediction Analysis Result",

        "recommendation": "Market Recommendation",

        "chart": "Gold Price Prediction Chart",

        "table": "Prediction Data",

        "uptrend": "Uptrend Market",

        "downtrend": "Downtrend Market",

        "market_range": "Estimated Market Price Range",

        "footer": "Luxury Gold Prediction Platform"
    }

# ========================================================
# CUSTOM CSS
# ========================================================
st.markdown("""
<style>

/* ======================================================
FONT
====================================================== */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* ======================================================
GLOBAL
====================================================== */
html, body, [class*="css"] {

    font-family: 'Poppins', sans-serif;

    background-color: #1A0F04;

    color: #FBF5D2;
}

/* ======================================================
APP BACKGROUND
====================================================== */
.stApp {

    background:
        radial-gradient(circle at top left,
        rgba(239,187,85,0.16),
        transparent 25%),

        radial-gradient(circle at bottom right,
        rgba(173,109,21,0.14),
        transparent 20%),

        #1A0F04;
}

/* ======================================================
CONTAINER
====================================================== */
.main .block-container {

    max-width: 1150px;

    padding-top: 20px;

    padding-bottom: 60px;
}

/* ======================================================
LANGUAGE SWITCHER
====================================================== */
.stSelectbox {

    width: 170px;
}

/* ======================================================
HERO SECTION
====================================================== */
.hero {

    margin-top: 30px;

    margin-bottom: 70px;
}

/* ======================================================
HERO CENTER
====================================================== */
.hero-center {

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;
}

/* ======================================================
APP NAME
====================================================== */
.app-name {

    font-size: 96px;

    font-weight: 700;

    line-height: 1;

    color: #EFBB55;

    letter-spacing: 2px;

    margin-bottom: 18px;

    text-shadow:
        0 0 25px rgba(239,187,85,0.35);
}

/* ======================================================
HERO TITLE
====================================================== */
.hero-title {

    font-size: 64px;

    line-height: 1.1;

    font-weight: 700;

    color: #FBF5D2;

    margin-bottom: 24px;
}

.hero-title span {

    color: #EFBB55;
}

/* ======================================================
SUBTITLE
====================================================== */
.hero-subtitle {

    font-size: 18px;

    line-height: 1.9;

    color: #FEE39F;

    max-width: 700px;

    text-align: center;
}

/* ======================================================
GLASS CARD
====================================================== */
.glass-card {

    background:
        rgba(255,255,255,0.05);

    border:
        1px solid rgba(239,187,85,0.10);

    backdrop-filter:
        blur(12px);

    border-radius:
        26px;

    padding:
        34px;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.30);

    margin-bottom:
        32px;
}

/* ======================================================
HEADINGS
====================================================== */
h3 {

    color:
        #FBF5D2 !important;

    font-size:
        28px !important;

    margin-bottom:
        22px !important;
}

/* ======================================================
LABEL
====================================================== */
.stRadio label,
.stDateInput label {

    color:
        #FEE39F !important;

    font-weight:
        500;
}

/* ======================================================
RADIO
====================================================== */
div[role="radiogroup"] {

    gap: 12px;
}

/* ======================================================
INPUT
====================================================== */
.stDateInput input {

    background:
        rgba(255,255,255,0.05) !important;

    color:
        #FBF5D2 !important;

    border:
        1px solid rgba(239,187,85,0.20) !important;

    border-radius:
        14px !important;
}

/* ======================================================
BUTTON
====================================================== */
div.stButton > button:first-child {

    background:
        linear-gradient(
            135deg,
            #EFBB55,
            #AD6D15
        ) !important;

    color:
        #1A0F04 !important;

    border:
        none !important;

    border-radius:
        16px !important;

    width:
        100%;

    height:
        58px;

    font-size:
        16px;

    font-weight:
        700;

    transition:
        0.3s ease;

    box-shadow:
        0 12px 30px rgba(239,187,85,0.28);
}

div.stButton > button:first-child:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 16px 35px rgba(239,187,85,0.38);
}

/* ======================================================
INFO BOX
====================================================== */
.stAlert {

    background:
        rgba(239,187,85,0.08) !important;

    border:
        1px solid rgba(239,187,85,0.16) !important;

    border-radius:
        18px !important;

    color:
        #FBF5D2 !important;
}

/* ======================================================
PLOTLY
====================================================== */
.js-plotly-plot {

    border-radius:
        24px;

    overflow:
        hidden;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.35);
}

/* ======================================================
DATAFRAME
====================================================== */
[data-testid="stDataFrame"] {

    border-radius:
        18px;

    overflow:
        hidden;

    border:
        1px solid rgba(239,187,85,0.10);
}

/* ======================================================
TEXT
====================================================== */
p, span {

    color:
        #FBF5D2 !important;
}

/* ======================================================
FOOTER
====================================================== */
.footer {

    text-align:
        center;

    margin-top:
        50px;

    color:
        #AD6D15;

    font-size:
        14px;
}

</style>
""", unsafe_allow_html=True)

# ========================================================
# HERO SECTION
# ========================================================
st.markdown(f"""

<div class="hero">

<div class="hero-center">

<div class="app-name">
G-Ture
</div>

<div class="hero-title">
{text["hero_title_1"]}<br>
<span>{text["hero_title_2"]}</span>
</div>

<div class="hero-subtitle">
{text["hero_subtitle"]}
</div>

</div>

</div>

""", unsafe_allow_html=True)

# ========================================================
# INPUT SECTION
# ========================================================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.subheader(text["prediction"])

# ========================================================
# METHOD
# ========================================================
tipe_cek = st.radio(
    text["prediction_method"],
    [
        text["single_day"],
        text["date_range"]
    ],
    horizontal=True
)

# ========================================================
# DATE LIMIT
# ========================================================
min_date = datetime(2026, 1, 1)
max_date = datetime(2027, 12, 31)

# ========================================================
# DATE INPUT
# ========================================================
if tipe_cek == text["single_day"]:

    tgl_pilihan = st.date_input(
        text["select_date"],
        value=min_date,
        min_value=min_date,
        max_value=max_date
    )

    tgl_mulai = tgl_pilihan
    tgl_selesai = tgl_pilihan

else:

    rentang_tgl = st.date_input(
        text["select_range"],
        value=(min_date, min_date + timedelta(days=7)),
        min_value=min_date,
        max_value=max_date
    )

    if isinstance(rentang_tgl, tuple) and len(rentang_tgl) == 2:
        tgl_mulai, tgl_selesai = rentang_tgl
    else:
        tgl_mulai = min_date
        tgl_selesai = min_date

st.write("")

btn_cek = st.button(text["analyze_btn"])

st.markdown('</div>', unsafe_allow_html=True)

# ========================================================
# LOAD MODEL
# ========================================================
@st.cache_resource
def load_gold_model():
    with open("model_emas.pkl", "rb") as file:
        return pickle.load(file)

try:
    model = load_gold_model()

except Exception:
    st.error("Failed to load model_emas.pkl")
    st.stop()

# ========================================================
# PREDICTION PROCESS
# ========================================================
if btn_cek:

    with st.spinner("Analyzing prediction..."):

        base_date = datetime(2023, 1, 1).date()

        count_days = (
            tgl_selesai - tgl_mulai
        ).days + 1

        date_list = [
            tgl_mulai + timedelta(days=x)
            for x in range(count_days)
        ]

        input_matrix = []

        for d in date_list:

            hari_ke = (d - base_date).days
            bulan = d.month
            tahun = d.year

            input_matrix.append([
                hari_ke,
                bulan,
                tahun
            ])

        input_data = pd.DataFrame(
            input_matrix,
            columns=['hari_ke', 'bulan', 'tahun']
        )

        list_prediksi = model.predict(input_data)

        preds_flat = np.array(
            list_prediksi
        ).flatten()

        df_hasil = pd.DataFrame({
            'Tanggal': pd.to_datetime(date_list),
            'Harga_Prediksi': preds_flat
        })

        df_hasil['Harga_Prediksi'] = (
            df_hasil['Harga_Prediksi']
            .astype(float)
        )

        harga_hari_pertama = float(
            df_hasil['Harga_Prediksi'].iloc[0]
        )

        harga_hari_terakhir = float(
            df_hasil['Harga_Prediksi'].iloc[-1]
        )

        toleransi = 0.02

        batas_bawah = (
            harga_hari_pertama * (1 - toleransi)
        )

        batas_atas = (
            harga_hari_terakhir * (1 + toleransi)
        )

    # ====================================================
    # RESULT SECTION
    # ====================================================
    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    st.subheader(text["result"])

    st.info(
        f"""
        {text["market_range"]}

        IDR {batas_bawah:,.0f}
        —
        IDR {batas_atas:,.0f}
        """
    )

    st.write("")

    st.subheader(text["recommendation"])

    if harga_hari_terakhir >= harga_hari_pertama:

        st.markdown(f"""
        <div style="
            background: rgba(239,187,85,0.08);
            padding: 24px;
            border-radius: 18px;
            border-left: 5px solid #EFBB55;
        ">

        <h4 style="color:#EFBB55;">
        {text["uptrend"]}
        </h4>

        <p style="line-height:1.9;">
        Gold prices are predicted to increase
        during the selected period.
        </p>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div style="
            background: rgba(239,187,85,0.08);
            padding: 24px;
            border-radius: 18px;
            border-left: 5px solid #AD6D15;
        ">

        <h4 style="color:#EFBB55;">
        {text["downtrend"]}
        </h4>

        <p style="line-height:1.9;">
        Gold prices are predicted to decline
        during the selected period.
        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ====================================================
    # CHART
    # ====================================================
    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    st.subheader(text["chart"])

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df_hasil['Tanggal'],
            y=df_hasil['Harga_Prediksi'],
            mode='lines+markers',

            line=dict(
                color='#EFBB55',
                width=4
            ),

            marker=dict(
                color='#FEE39F',
                size=7,

                line=dict(
                    color='#AD6D15',
                    width=1
                )
            )
        )
    )

    fig.update_layout(

        plot_bgcolor='#1A0F04',
        paper_bgcolor='#1A0F04',

        font=dict(
            color='#FBF5D2',
            family='Poppins'
        ),

        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(239,187,85,0.08)',
            linecolor='#AD6D15'
        ),

        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(239,187,85,0.08)',
            tickformat=",.0f",
            linecolor='#AD6D15'
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # ====================================================
    # TABLE
    # ====================================================
    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    st.subheader(text["table"])

    df_tampil = df_hasil.copy()

    df_tampil['Tanggal'] = (
        df_tampil['Tanggal']
        .dt.strftime('%d-%m-%Y')
    )

    df_tampil['Harga_Prediksi'] = (
        df_tampil['Harga_Prediksi']
        .apply(lambda x: f"IDR {x:,.0f}")
    )

    st.dataframe(
        df_tampil,
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ========================================================
# FOOTER
# ========================================================
st.markdown(f"""

<div class="footer">
G-Ture — {text["footer"]}
</div>

""", unsafe_allow_html=True)