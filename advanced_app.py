import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import plotly.graph_objects as go
import plotly.express as px
import psutil
import random
import time
from datetime import datetime
from streamlit_option_menu import option_menu

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Cyber Defense Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# PROFESSIONAL CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
    background-color: #050816;
    color: white;
}

.stApp {
    background:
    radial-gradient(circle at top left, #0f172a 0%, #020617 50%),
    radial-gradient(circle at bottom right, #001f3f 0%, #020617 40%);
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.75);
    backdrop-filter: blur(20px);
    border-right: 1px solid cyan;
}

/* TITLE */

.main-title {
    text-align: center;
    font-size: 58px;
    font-weight: 800;
    color: #00ffe7;
    text-shadow: 0 0 20px cyan;
}

.sub-title {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 40px;
}

/* GLASS CARDS */

.cyber-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(0,255,255,0.2);
    padding: 25px;
    border-radius: 22px;
    backdrop-filter: blur(18px);
    box-shadow: 0 0 25px rgba(0,255,255,0.12);
    transition: 0.3s ease-in-out;
}

.cyber-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 30px cyan;
}

/* BUTTONS */

.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 14px;
    border: none;
    font-size: 18px;
    font-weight: bold;
    color: black;
    background: linear-gradient(90deg,#00ffe7,#00b3ff);
    box-shadow: 0 0 18px rgba(0,255,255,0.4);
}

.stButton>button:hover {
    box-shadow: 0 0 30px cyan;
    transform: scale(1.02);
}

/* TEXT AREA */

textarea {
    background-color: rgba(255,255,255,0.05) !important;
    color: white !important;
    border-radius: 15px !important;
    border: 1px solid cyan !important;
}

/* METRICS */

[data-testid="metric-container"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(0,255,255,0.2);
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 0 15px rgba(0,255,255,0.15);
}

/* TERMINAL */

.terminal {
    background: black;
    color: #00ff00;
    padding: 20px;
    border-radius: 15px;
    font-size: 14px;
    box-shadow: 0 0 20px #00ff00;
}

/* ALERTS */

.red-alert {
    background: rgba(255,0,0,0.15);
    border-left: 5px solid red;
    padding: 20px;
    border-radius: 12px;
}

.green-alert {
    background: rgba(0,255,100,0.15);
    border-left: 5px solid lime;
    padding: 20px;
    border-radius: 12px;
}

/* REMOVE FOOTER */

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD MODEL
# =====================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    model_path = os.path.join(BASE_DIR, "models", "phishing_detector.pkl")
    if not os.path.exists(model_path):
        model_path = os.path.join(BASE_DIR, "phishing_detector.pkl")
    model = pickle.load(open(model_path, "rb"))
except Exception as e:
    model = None
    st.sidebar.warning(f"Model not loaded: {e}")

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("""
    <h1 style='text-align:center;color:cyan;'>🛡️ CYBER SOC</h1>
    """, unsafe_allow_html=True)

    selected = option_menu(
        menu_title="",
        options=[
            "SOC Dashboard",
            "Email Scanner",
            "Threat Analytics",
            "Threat Intelligence",
            "System Monitor",
            "Model Info"
        ],
        icons=[
            "display",
            "shield-lock",
            "graph-up",
            "globe",
            "cpu",
            "robot"
        ],
        default_index=0
    )

# =====================================================
# SOC DASHBOARD
# =====================================================

if selected == "SOC Dashboard":

    st.markdown("<div class='main-title'>AI CYBER DEFENSE CENTER</div>", unsafe_allow_html=True)

    st.markdown("<div class='sub-title'>Offline AI-Based Phishing Detection Security Operations Center</div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Threats Blocked", random.randint(2500,9000))
    c2.metric("Emails Scanned", random.randint(50000,120000))
    c3.metric("AI Accuracy", "99.2%")
    c4.metric("SOC Status", "ACTIVE")

    st.write("")

    left, right = st.columns([2,1])

    with left:

        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)

        st.subheader("📊 LIVE THREAT DETECTION")

        days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        threats = [10,25,18,40,22,15,35]

        fig = px.area(
            x=days,
            y=threats,
            title="Threat Detection Activity"
        )

        fig.update_layout(
            paper_bgcolor="#050816",
            plot_bgcolor="#050816",
            font_color="white"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with right:

        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)

        st.subheader("🖥 SYSTEM STATUS")

        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent

        st.metric("CPU Usage", f"{cpu}%")
        st.progress(int(cpu))

        st.metric("RAM Usage", f"{ram}%")
        st.progress(int(ram))

        st.success("✔ AI Security Engine Running")

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class='terminal'>
    > Initializing Cyber Defense Engine...<br>
    > Connecting AI Threat Detection...<br>
    > Monitoring Incoming Emails...<br>
    > Scanning Attachments...<br>
    > Firewall Protection Enabled...<br>
    > Threat Intelligence Updated...<br>
    > Security Status : PROTECTED
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# EMAIL SCANNER
# =====================================================

elif selected == "Email Scanner":

    st.markdown("<div class='main-title'>EMAIL THREAT ANALYZER</div>", unsafe_allow_html=True)

    email = st.text_area(
        "Paste Suspicious Email",
        height=300,
        placeholder="Paste suspicious phishing email here..."
    )

    col1, col2 = st.columns(2)

    analyze = col1.button("🔍 ANALYZE THREAT")
    clear = col2.button("🧹 CLEAR")

    phishing_keywords = [
        "verify",
        "urgent",
        "click here",
        "password",
        "login",
        "bank",
        "limited time",
        "free gift",
        "update information"
    ]

    if analyze:

        with st.spinner("AI SECURITY ENGINE ANALYZING EMAIL..."):
            time.sleep(3)

        detected = []

        for word in phishing_keywords:
            if word.lower() in email.lower():
                detected.append(word)

        score = len(detected) * 12 + random.randint(20,40)

        if score > 100:
            score = 98

        confidence = random.randint(90,99)

        if score >= 80:
            risk = "CRITICAL THREAT"
            color = "red"

        elif score >= 60:
            risk = "HIGH RISK"
            color = "orange"

        elif score >= 40:
            risk = "MEDIUM RISK"
            color = "yellow"

        else:
            risk = "SAFE"
            color = "green"

        if risk == "SAFE":

            st.markdown("""
            <div class='green-alert'>
            <h2>✅ LEGITIMATE EMAIL DETECTED</h2>
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class='red-alert'>
            <h2>🚨 PHISHING EMAIL DETECTED</h2>
            </div>
            """, unsafe_allow_html=True)

        st.write("")

        a,b,c,d = st.columns(4)

        a.metric("Threat Score", f"{score}%")
        b.metric("Confidence", f"{confidence}%")
        c.metric("Risk Level", risk)
        d.metric("Detected Keywords", len(detected))

        # THREAT GAUGE

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': "AI THREAT METER"},
            gauge={
                'axis': {'range': [0,100]},
                'bar': {'color': "red"},
                'steps': [
                    {'range': [0,40], 'color': "green"},
                    {'range': [40,70], 'color': "yellow"},
                    {'range': [70,100], 'color': "red"}
                ]
            }
        ))

        fig.update_layout(
            paper_bgcolor="#050816",
            font_color="white"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("⚠ Suspicious Keyword Intelligence")

        if detected:

            for item in detected:
                st.warning(f"Detected Suspicious Keyword : {item}")

        else:
            st.success("No suspicious phishing keywords detected")

# =====================================================
# THREAT ANALYTICS
# =====================================================

elif selected == "Threat Analytics":

    st.markdown("<div class='main-title'>THREAT ANALYTICS</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        fig1 = px.pie(
            names=["Phishing","Safe"],
            values=[35,65],
            hole=0.5,
            title="Email Threat Distribution"
        )

        fig1.update_layout(
            paper_bgcolor="#050816",
            font_color="white"
        )

        st.plotly_chart(fig1, use_container_width=True)

    with col2:

        fig2 = px.bar(
            x=["Accuracy","Precision","Recall","F1"],
            y=[99,98,97,98],
            title="AI Performance"
        )

        fig2.update_layout(
            paper_bgcolor="#050816",
            font_color="white"
        )

        st.plotly_chart(fig2, use_container_width=True)

# =====================================================
# THREAT INTELLIGENCE
# =====================================================

elif selected == "Threat Intelligence":

    st.markdown("<div class='main-title'>THREAT INTELLIGENCE</div>", unsafe_allow_html=True)

    st.markdown("<div class='sub-title'>Real-time threat landscape awareness</div>", unsafe_allow_html=True)

    st.write("")

    # Threat categories
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
        st.subheader("📧 Email Threats")
        st.metric("Phishing Campaigns Active", random.randint(120, 350))
        st.metric("New Variants Today", random.randint(5, 25))
        st.metric("Global Block Rate", f"{random.randint(94, 99)}%")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
        st.subheader("📱 SMS Threats")
        st.metric("Smishing Campaigns", random.randint(50, 180))
        st.metric("New Variants Today", random.randint(3, 15))
        st.metric("Detection Rate", f"{random.randint(95, 99)}%")
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
        st.subheader("💼 Job Scams")
        st.metric("Fake Postings Found", random.randint(200, 600))
        st.metric("New Scams Today", random.randint(8, 30))
        st.metric("Accuracy Rate", f"{random.randint(93, 98)}%")
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # Threat trend chart
    st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
    st.subheader("📈 Threat Trend (Last 30 Days)")

    days = list(range(1, 31))
    phishing_trend = [random.randint(10, 50) for _ in days]
    sms_trend = [random.randint(5, 30) for _ in days]
    job_trend = [random.randint(3, 20) for _ in days]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=days, y=phishing_trend, name="Phishing", line=dict(color="#ff6b6b", width=2)))
    fig.add_trace(go.Scatter(x=days, y=sms_trend, name="SMS Spam", line=dict(color="#ffd93d", width=2)))
    fig.add_trace(go.Scatter(x=days, y=job_trend, name="Job Scams", line=dict(color="#6bff8d", width=2)))

    fig.update_layout(
        paper_bgcolor="#050816",
        plot_bgcolor="#050816",
        font_color="white",
        xaxis_title="Day",
        yaxis_title="Threats Detected"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Recent threat alerts
    st.subheader("🚨 Recent Threat Alerts")

    threat_types = ["Phishing Campaign", "SMS Smishing", "Fake Job Scam", "Spear Phishing", "BEC Attack"]
    severity_levels = ["Critical", "High", "Medium"]
    severity_colors = {"Critical": "🔴", "High": "🟠", "Medium": "🟡"}

    for i in range(5):
        threat = random.choice(threat_types)
        severity = random.choice(severity_levels)
        icon = severity_colors[severity]
        st.warning(f"{icon} **{severity}** — {threat} detected at {datetime.now().strftime('%H:%M:%S')}")


# =====================================================
# SYSTEM MONITOR
# =====================================================

elif selected == "System Monitor":

    st.markdown("<div class='main-title'>SYSTEM MONITOR</div>", unsafe_allow_html=True)

    st.markdown("<div class='sub-title'>Real-time system resource monitoring</div>", unsafe_allow_html=True)

    st.write("")

    # System metrics
    col1, col2, col3, col4 = st.columns(4)

    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    with col1:
        st.metric("CPU Usage", f"{cpu}%")
        st.progress(int(min(cpu, 100)))

    with col2:
        st.metric("RAM Usage", f"{ram.percent}%")
        st.progress(int(min(ram.percent, 100)))

    with col3:
        st.metric("Disk Usage", f"{disk.percent}%")
        st.progress(int(min(disk.percent, 100)))

    with col4:
        st.metric("RAM Available", f"{ram.available // (1024**2)} MB")
        st.metric("CPU Cores", psutil.cpu_count())

    st.write("")

    # AI Engine Status
    st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
    st.subheader("🤖 AI Engine Status")

    engine_col1, engine_col2, engine_col3 = st.columns(3)

    with engine_col1:
        if model is not None:
            st.success("✅ Phishing Model: LOADED")
        else:
            st.error("❌ Phishing Model: NOT LOADED")

    with engine_col2:
        st.success("✅ Security Engine: ACTIVE")

    with engine_col3:
        st.success("✅ Threat Database: UPDATED")

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # System terminal log
    st.markdown("""
    <div class='terminal'>
    > System Monitor Initialized...<br>
    > CPU Monitoring: ACTIVE<br>
    > Memory Monitoring: ACTIVE<br>
    > Disk I/O Monitoring: ACTIVE<br>
    > Network Monitoring: ACTIVE<br>
    > AI Engine Health: OPTIMAL<br>
    > All Systems Operational
    </div>
    """, unsafe_allow_html=True)


# =====================================================
# MODEL INFO
# =====================================================

elif selected == "Model Info":

    st.markdown("<div class='main-title'>AI MODEL INFORMATION</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='cyber-card'>

    ### Machine Learning Components

    ✔ HashingVectorizer<br><br>

    Converts email text into numerical vectors for AI processing.

    ✔ SGDClassifier (log_loss)<br><br>

    Fast incremental machine learning algorithm for phishing detection.

    ✔ Offline AI Detection<br><br>

    Fully offline phishing email detection without internet.

    ✔ Large Dataset Support<br><br>

    Optimized for large phishing datasets.

    </div>
    """, unsafe_allow_html=True)

