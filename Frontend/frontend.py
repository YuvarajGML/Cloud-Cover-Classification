import textwrap
import streamlit as st
import requests

API_URL = "https://cloud-cover-api.onrender.com/predict"

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="WeatherIQ · Prediction Engine",
    page_icon="🌤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# Custom CSS — Professional Dark Theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700&family=DM+Mono:wght@300;400;500&display=swap');

/* ── Reset & Base ───────────────────────────── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background-color: #070d1a !important;
    color: #e2e8f0 !important;
    font-family: 'Syne', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 80% 50% at 20% -10%, rgba(20,184,166,0.08) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 110%, rgba(99,102,241,0.06) 0%, transparent 55%),
        #070d1a !important;
}

[data-testid="stHeader"] { background: transparent !important; }

.block-container {
    padding: 2.5rem 3rem 4rem !important;
    max-width: 1320px !important;
}

/* ── Typography ─────────────────────────────── */
h1, h2, h3, h4 {
    font-family: 'Syne', sans-serif !important;
    letter-spacing: -0.02em;
}

/* ── Navbar Strip ───────────────────────────── */
.nav-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.75rem 0 1.75rem;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 2.5rem;
}
.nav-logo {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}
.nav-logo-icon {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, #14b8a6, #6366f1);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
}
.nav-logo-text {
    font-size: 1.25rem;
    font-weight: 700;
    color: #f8fafc;
    letter-spacing: -0.03em;
}
.nav-logo-sub {
    font-size: 0.7rem;
    font-family: 'DM Mono', monospace;
    color: #64748b;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-top: -2px;
}
.nav-badge {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    color: #14b8a6;
    border: 1px solid rgba(20,184,166,0.3);
    padding: 4px 10px;
    border-radius: 999px;
    letter-spacing: 0.06em;
}

/* ── Section Labels ─────────────────────────── */
.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #475569;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.05);
}

/* ── Input Card ─────────────────────────────── */
.input-card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 1.75rem;
    backdrop-filter: blur(12px);
}

.input-group-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #334155;
    margin: 1.5rem 0 0.6rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}
.input-group-label:first-child { margin-top: 0; }

/* ── Streamlit Input Overrides ──────────────── */
[data-testid="stNumberInput"] label,
[data-testid="stSlider"] label,
[data-testid="stSelectbox"] label {
    font-size: 0.78rem !important;
    color: #94a3b8 !important;
    font-weight: 400 !important;
    letter-spacing: 0.01em !important;
    font-family: 'Syne', sans-serif !important;
}

[data-testid="stNumberInput"] input {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 8px !important;
    color: #f1f5f9 !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.9rem !important;
}
[data-testid="stNumberInput"] input:focus {
    border-color: rgba(20,184,166,0.5) !important;
    box-shadow: 0 0 0 3px rgba(20,184,166,0.08) !important;
}

[data-testid="stSelectbox"] > div > div {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 8px !important;
    color: #f1f5f9 !important;
}

/* Slider track */
[data-testid="stSlider"] [data-baseweb="slider"] > div > div > div {
    background: rgba(255,255,255,0.08) !important;
}
[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
    background: #14b8a6 !important;
    border-color: #14b8a6 !important;
}

/* ── Output Panel ───────────────────────────── */
.output-panel {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 1.75rem;
    height: 100%;
    position: relative;
    overflow: hidden;
}
.output-panel::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #14b8a6, transparent);
    opacity: 0.6;
}

/* ── Result Display ─────────────────────────── */
.result-idle {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 3rem 1rem;
    gap: 1rem;
    opacity: 0.35;
}
.result-idle-icon {
    font-size: 2.5rem;
    filter: grayscale(1);
}
.result-idle-text {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #475569;
}

.result-box {
    background: linear-gradient(135deg, rgba(20,184,166,0.06), rgba(99,102,241,0.06));
    border: 1px solid rgba(20,184,166,0.18);
    border-radius: 12px;
    padding: 1.75rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.result-box::after {
    content: '';
    position: absolute;
    inset: -1px;
    border-radius: 12px;
    background: linear-gradient(135deg, rgba(20,184,166,0.12), transparent, rgba(99,102,241,0.12));
    z-index: -1;
}

.result-weather-icon {
    font-size: 3.5rem;
    display: block;
    margin-bottom: 0.75rem;
    line-height: 1;
}
.result-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #64748b;
    margin-bottom: 0.4rem;
}
.result-value {
    font-size: 1.9rem;
    font-weight: 700;
    color: #f8fafc;
    letter-spacing: -0.03em;
    line-height: 1.1;
    margin-bottom: 0.25rem;
}
.result-confidence {
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: #14b8a6;
    margin-top: 0.4rem;
}

/* ── Confidence Bar ─────────────────────────── */
.conf-bar-wrap {
    margin-top: 1.25rem;
}
.conf-bar-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 6px;
}
.conf-bar-title {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #475569;
}
.conf-bar-value {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    color: #14b8a6;
}
.conf-bar-track {
    height: 4px;
    background: rgba(255,255,255,0.06);
    border-radius: 999px;
    overflow: hidden;
}
.conf-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #14b8a6, #6366f1);
    border-radius: 999px;
    transition: width 0.6s cubic-bezier(.4,0,.2,1);
}

/* ── Stat Chips ─────────────────────────────── */
.stat-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 1.25rem;
}
.stat-chip {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 8px;
    padding: 6px 12px;
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    color: #94a3b8;
    flex: 1;
    min-width: 80px;
    text-align: center;
}
.stat-chip span {
    display: block;
    font-size: 0.62rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #475569;
    margin-top: 2px;
}

/* ── Submit Button ──────────────────────────── */
.stButton > button {
    width: 100% !important;
    height: 48px !important;
    background: linear-gradient(135deg, #14b8a6, #0d9488) !important;
    color: #0a0f1a !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.04em !important;
    border: none !important;
    border-radius: 10px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    margin-top: 0.5rem !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #2dd4bf, #14b8a6) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(20,184,166,0.25) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Form Submit ────────────────────────────── */
[data-testid="stForm"] {
    border: none !important;
    padding: 0 !important;
}

/* ── Divider ────────────────────────────────── */
hr {
    border-color: rgba(255,255,255,0.05) !important;
    margin: 2rem 0 !important;
}

/* ── Footer ─────────────────────────────────── */
.footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(255,255,255,0.05);
    margin-top: 2rem;
}
.footer-stack {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}
.footer-tag {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #1e293b;
    background: rgba(255,255,255,0.04);
    padding: 4px 10px;
    border-radius: 6px;
    border: 1px solid rgba(255,255,255,0.05);
}
.footer-copy {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    color: #1e293b;
    letter-spacing: 0.05em;
}

/* ── Spinner ────────────────────────────────── */
[data-testid="stSpinner"] {
    color: #14b8a6 !important;
}

/* ── Error ──────────────────────────────────── */
[data-testid="stAlert"] {
    background: rgba(239,68,68,0.08) !important;
    border: 1px solid rgba(239,68,68,0.2) !important;
    border-radius: 10px !important;
    color: #fca5a5 !important;
}

/* ── Scrollbar ──────────────────────────────── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.08); border-radius: 999px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Navbar
# ─────────────────────────────────────────────
st.markdown("""
<div class="nav-bar">
    <div class="nav-logo">
        <div class="nav-logo-icon">🌤</div>
        <div>
            <div class="nav-logo-text">WeatherIQ</div>
            <div class="nav-logo-sub">Prediction Engine</div>
        </div>
    </div>
    <div class="nav-badge">ML · v2.4.1</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Weather icon map
# ─────────────────────────────────────────────
WEATHER_ICONS = {
    "sunny": "☀️",
    "cloudy": "☁️",
    "rainy": "🌧️",
    "snowy": "❄️",
    "stormy": "⛈️",
    "windy": "💨",
    "foggy": "🌫️",
    "partly cloudy": "⛅",
    "clear": "🌤",
    "drizzle": "🌦️",
}

def get_weather_icon(prediction: str) -> str:
    prediction_lower = prediction.lower()
    for key, icon in WEATHER_ICONS.items():
        if key in prediction_lower:
            return icon
    return "🌡️"

# ─────────────────────────────────────────────
# Layout — Two Columns
# ─────────────────────────────────────────────
left, spacer, right = st.columns([1.15, 0.06, 0.85])

# ─────────────────────────────────────────────
# LEFT — Inputs
# ─────────────────────────────────────────────
with left:
    st.markdown('<p class="section-label">01 — Input Parameters</p>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="input-card">', unsafe_allow_html=True)

        # Atmospheric
        st.markdown('<p class="input-group-label">Atmospheric Conditions</p>', unsafe_allow_html=True)
        atm1, atm2, atm3 = st.columns(3, gap="medium")
        with atm1:
            temperature = st.number_input("Temperature (°C)", value=20.0, step=0.5, format="%.1f")
        with atm2:
            pressure = st.number_input("Pressure (hPa)", value=1013.0, step=0.5, format="%.1f")
        with atm3:
            visibility = st.number_input("Visibility (km)", value=10.0, step=0.5, format="%.1f")

        # Moisture & Wind
        st.markdown('<p class="input-group-label">Moisture & Wind</p>', unsafe_allow_html=True)
        mw1, mw2 = st.columns(2, gap="medium")
        with mw1:
            humidity = st.slider("Humidity (%)", 0, 100, 50)
            precipitation = st.slider("Precipitation (%)", 0, 100, 0)
        with mw2:
            wind_speed = st.number_input("Wind Speed (km/h)", value=5.0, step=0.5, format="%.1f")

        # Sky & Environment
        # Environment
        st.markdown('<p class="input-group-label">Environment</p>', unsafe_allow_html=True)

        env1, env2 = st.columns(2, gap="medium")

        with env1:
            season = st.selectbox(
                "Season",
                ["Winter", "Spring", "Summer", "Autumn"]
            )

        with env2:
            location = st.selectbox(
                "Location Type",
                ["inland", "coastal", "mountain"]
            )

        st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# RIGHT — Output
# ─────────────────────────────────────────────
with right:
    st.markdown('<p class="section-label">02 — Prediction Output</p>', unsafe_allow_html=True)

    st.markdown('<div class="output-panel">', unsafe_allow_html=True)

    # Submit
    with st.form("prediction_form"):
        submit = st.form_submit_button("⟶  Run Prediction")

    output_placeholder = st.empty()

    if submit:
        payload = {
            "Temperature": temperature,
            "Humidity": humidity,
            "Wind_Speed": wind_speed,
            "Precipitation": precipitation,
            "Atmospheric_Pressure": pressure,
            "Visibility": visibility,
            "Season": season,
            "Location": location
        }
        with st.spinner("Running inference…"):
            try:
                res = requests.post(API_URL, json=payload, timeout=60)

                if res.status_code == 200:
                    data = res.json()

                    if "error" in data:
                        output_placeholder.error(f"Model error: {data['error']}")
                    else:
                        prediction = data["prediction"]
                        confidence = data.get("confidence", None)
                        icon = get_weather_icon(prediction)

                        conf_pct = f"{confidence * 100:.1f}%" if confidence else "—"
                        bar_width = f"{confidence * 100:.1f}%" if confidence else "0%"

                        conf_bar_html = ""
                        if confidence:
                            conf_bar_html = textwrap.dedent(f"""
                                <div class="conf-bar-wrap">
                                    <div class="conf-bar-header">
                                        <span class="conf-bar-title">Confidence</span>
                                        <span class="conf-bar-value">{conf_pct}</span>
                                    </div>
                                    <div class="conf-bar-track">
                                        <div class="conf-bar-fill" style="width:{bar_width}"></div>
                                    </div>
                                </div>
                            """).strip()

                        result_html = textwrap.dedent(f"""
                            <div class="result-box">
                                <span class="result-weather-icon">{icon}</span>
                                <div class="result-label">Predicted Condition</div>
                                <div class="result-value">{prediction}</div>
                                {conf_bar_html}
                            </div>
                            <div class="stat-chips">
                                <div class="stat-chip">{temperature}°C<span>Temp</span></div>
                                <div class="stat-chip">{humidity}%<span>Humidity</span></div>
                                <div class="stat-chip">{wind_speed} km/h<span>Wind</span></div>
                                <div class="stat-chip">{pressure} hPa<span>Pressure</span></div>
                            </div>
                        """).strip()

                        with output_placeholder.container():
                            st.markdown(result_html, unsafe_allow_html=True)

                else:
                    output_placeholder.error(f"Server returned {res.status_code}. Check the API is running.")

            except requests.exceptions.ConnectionError:
                output_placeholder.error("Cannot reach API at `localhost:8000`. Is the FastAPI server running?")
            except requests.exceptions.Timeout:
                output_placeholder.error("Request timed out after 10 seconds.")
            except Exception as e:
                output_placeholder.error(f"Unexpected error: {str(e)}")

    else:
        with output_placeholder.container():
            st.markdown(textwrap.dedent("""
                <div class="result-idle">
                    <div class="result-idle-icon">⛅</div>
                    <div class="result-idle-text">Awaiting input</div>
                </div>
            """).strip(), unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-stack">
        <span class="footer-tag">FastAPI</span>
        <span class="footer-tag">Scikit-learn</span>
        <span class="footer-tag">Streamlit</span>
        <span class="footer-tag">ML Pipeline</span>
    </div>
    <div class="footer-copy">WeatherIQ © 2025</div>
</div>
""", unsafe_allow_html=True)
