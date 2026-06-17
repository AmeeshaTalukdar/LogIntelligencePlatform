import streamlit as st
import pandas as pd
import time
from datetime import datetime
import plotly.express as px
import os, sys
from io import BytesIO

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ---------------- PATH FIX ----------------
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT)

from backend.service import classify_log


# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="LogOS - AI Observability Platform",
    page_icon="🧠",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================
if "logs" not in st.session_state:
    st.session_state.logs = []


# =========================================================
# SIDEBAR CONTROL PLANE
# =========================================================
st.sidebar.title("🧠 LogOS Control Plane")

mode = st.sidebar.selectbox(
    "System Mode",
    ["🛰 Observability", "📊 Executive", "🐞 Debug"]
)

upload = st.sidebar.file_uploader("Upload CSV Logs", type=["csv"])


# =========================================================
# THEME ENGINE
# =========================================================
if mode == "🛰 Observability":
    bg = "#0b0f19"
    accent = "#22d3ee"
elif mode == "📊 Executive":
    bg = "#f5f7fb"
    accent = "#1d4ed8"
else:
    bg = "#050505"
    accent = "#00ff88"

st.markdown(f"""
<style>
.main {{
    background-color: {bg};
    color: white;
}}

.stButton>button {{
    background: {accent};
    color: white;
    border-radius: 10px;
    height: 3em;
    font-weight: 600;
}}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPERS
# =========================================================
def confidence_bucket(x):
    if x >= 0.75:
        return "High"
    elif x >= 0.5:
        return "Medium"
    return "Low"


def run_model(source, log):
    res = classify_log(source, log)
    return (
        res.get("label", "Unknown"),
        res.get("method", "unknown"),
        float(res.get("confidence") or 0)
    )


def generate_pdf(data):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("LogOS AI Observability Report", styles["Title"]))
    content.append(Spacer(1, 12))

    for item in data[-30:]:
        line = f"{item['time']} | {item['label']} | {item['method']} | {item['confidence']}"
        content.append(Paragraph(line, styles["Normal"]))
        content.append(Spacer(1, 6))

    doc.build(content)
    buffer.seek(0)
    return buffer


# =========================================================
# HEADER
# =========================================================
st.title("🧠 LogOS - AI Observability Platform")
st.caption("Regex → BERT → LLM intelligent routing engine")


# =========================================================
# CSV INGESTION
# =========================================================
if upload:
    df = pd.read_csv(upload)

    col = "log_message" if "log_message" in df.columns else df.columns[0]

    results = []

    for _, row in df.iterrows():
        label, method, conf = run_model("stream", row[col])

        results.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "log": row[col],
            "label": label,
            "method": method,
            "confidence": conf
        })

    batch_df = pd.DataFrame(results)

    st.subheader("📦 Batch Results")
    st.dataframe(batch_df)

    st.download_button(
        "⬇ Download CSV",
        batch_df.to_csv(index=False).encode(),
        file_name="logs.csv"
    )

    st.session_state.logs.extend(results)


# =========================================================
# SINGLE LOG INPUT
# =========================================================
st.markdown("## 🧾 Live Log Analyzer")

log_input = st.text_area("Enter log message", height=120)

col1, col2, col3 = st.columns(3)

run = col1.button("🚀 Analyze")
reset = col2.button("🧹 Reset")
pdf = col3.button("📄 Export PDF")


if reset:
    st.session_state.logs = []
    st.rerun()


# =========================================================
# ANALYZE SINGLE LOG
# =========================================================
if run and log_input:

    label, method, conf = run_model("stream", log_input)

    entry = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "log": log_input,
        "label": label,
        "method": method,
        "confidence": conf
    }

    st.session_state.logs.append(entry)

    st.subheader("📊 Result")

    if conf >= 0.75:
        st.success(f"🟢 HIGH → {label}")
    elif conf >= 0.5:
        st.warning(f"🟡 MEDIUM → {label}")
    else:
        st.error(f"🔴 LOW → {label}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Model", method.upper())
    col2.metric("Confidence", f"{conf:.2f}")
    col3.metric("Bucket", confidence_bucket(conf))

    st.progress(min(conf, 1.0))


# =========================================================
# PDF EXPORT
# =========================================================
if pdf:
    if not st.session_state.logs:
        st.warning("No logs to export")
    else:
        pdf_buffer = generate_pdf(st.session_state.logs)

        st.download_button(
            "⬇ Download PDF",
            pdf_buffer,
            file_name="logos_report.pdf",
            mime="application/pdf"
        )


# =========================================================
# DASHBOARD
# =========================================================
if st.session_state.logs:

    df = pd.DataFrame(st.session_state.logs)

    st.markdown("---")
    st.subheader("📊 System Dashboard")

    # KPI ROW
    c1, c2, c3 = st.columns(3)

    c1.metric("Total Logs", len(df))
    c2.metric("Avg Confidence", f"{df['confidence'].mean():.2f}")
    c3.metric("Unique Labels", df["label"].nunique())

    # MODEL USAGE
    st.markdown("### 🧠 Model Usage")
    st.bar_chart(df["method"].value_counts())

    # CONFIDENCE
    df["bucket"] = df["confidence"].apply(confidence_bucket)
    st.markdown("### 🎯 Confidence Distribution")
    st.bar_chart(df["bucket"].value_counts())

    # LABELS
    st.markdown("### 🏷 Top Labels")
    st.bar_chart(df["label"].value_counts().head(10))

    # HEATMAP STYLE TREND
    df["index"] = range(len(df))
    fig = px.line(df, x="index", y="confidence", title="Confidence Trend Over Time")
    st.plotly_chart(fig, use_container_width=True)


# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.caption("🧠 LogOS • AI Observability SaaS • Production Demo UI")
