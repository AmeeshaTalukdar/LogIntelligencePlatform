
🧠 AI Log Intelligence Platform

Transforming System Noise into Actionable Intelligence

Python Streamlit Groq BERT

The AI Log Intelligence Platform is a next-generation observability tool that
solves the "log fatigue" problem. By combining deterministic speed with semantic
depth, it classifies logs through a sophisticated Hybrid Waterfall Pipeline.

🏗️ System Architecture

Our architecture follows a "Waterfall" logic, ensuring that the system is fast
for known patterns and intelligent for unknown anomalies.

graph TD
    %% Ingest
    A[Raw Log String] --> B{1. Regex Engine}
    
    %% Level 1
    B -- "Match Found" --> C[Label: Known Event]
    B -- "No Match" --> D{2. BERT Semantic}
    
    %% Level 2
    D -- "Confidence > 0.8" --> E[Label: Semantic Match]
    D -- "Low Confidence" --> F{3. LLM Fallback}
    
    %% Level 3
    F -- "Reasoning" --> G[Label: Complex Insight]
    
    %% Final
    C & E & G --> H[Unified Analytics Dashboard]
    H --> I[CSV/PDF Reports]

    style B fill:#10B981,stroke:#fff,color:#fff
    style D fill:#3B82F6,stroke:#fff,color:#fff
    style F fill:#8B5CF6,stroke:#fff,color:#fff
    style H fill:#f96,stroke:#333

🧠 The Hybrid Intelligence Pipeline

| Layer       | Technology     | Use Case                                                      | Cost/Speed             |
| :---------- | :------------- | :------------------------------------------------------------ | :--------------------- |
| **Layer 1** | **Regex**      | High-frequency, fixed patterns (User login, backup success).  | ⚡ Instant / $0         |
| **Layer 2** | **BERT**       | Semantic variations (Infrastructure errors, security events). | 🚀 Fast / Low           |
| **Layer 3** | **LLM (Groq)** | Ambiguous, business-specific, or new "Zero-day" logs.         | 🧠 Reasoning / Variable |

🖥️ UI Experience (Three Modes)

The platform features a Cyber-Dark interface designed for high-pressure
environments:

🛰️ 1. Observability Mode

  - Live Stream: A vertical scrolling feed where logs are color-coded by their
    origin (Regex, BERT, or LLM).
  - Real-time Gauges: Visual indicators of current system health and error
    density.

📊 2. Executive Mode

  - Distribution Analysis: Pie charts showing Model Usage Distribution (e.g.,
    "90% logs handled by Regex").
  - Trends: Confidence scores plotted over time to monitor model drift.
  - ROI Tracker: Visualizing the cost saved by using BERT instead of hitting the
    LLM for every log.

🐞 3. Debug Mode

  - Confidence Breakdown: See the raw softmax scores from the BERT model.
  - LLM Chain-of-Thought: View the internal reasoning provided by the LLM when
    it handles complex fallback logs.

🚀 Features

  - 🔍 Single Log Analysis: Instant classification with confidence breakdown.
  - 📦 Batch Log Processing: Upload CSVs for bulk categorization and automated
    labeling.
  - 📈 Advanced Analytics: Real-time metrics on label frequency and system
    reliability.
  - 📄 Enterprise Reporting: One-click exports for audit-ready PDF and CSV
    reports.

📁 Project Structure

project-nlp-log-classification/
├── backend/
│   ├── service.py            # The Intelligence Orchestrator
│   └── processors/           # Modular Pipeline Layers
│       ├── processor_regex.py
│       ├── processor_bert.py
│       └── processor_llm.py
├── frontend/
│   └── app.py                # Streamlit Glassmorphism UI
├── models/
│   └── log_classifier.joblib # Serialized BERT Classifier
├── shared/
│   └── schemas.py            # Pydantic Data Models
├── requirements.txt
└── README.md

⚙️ Quick Start

1. Setup Environment

git clone <repository-url>
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. Configure API Keys Create a .env file:

GROQ_API_KEY=your_api_key_here

3. Launch the Platform

PYTHONPATH=. streamlit run frontend/app.py

📈 Future Enhancements

- [ ] Real-time Streaming: Apache Kafka / Redis Pub-Sub integration.
- [ ] Anomaly Detection: Identify log clusters that don't match any known
  labels.
- [ ] FastAPI Backend: Decoupling the UI from the processing engine for scale.
- [ ] OpenTelemetry: Native support for distributed tracing.

💡 Summary

This platform demonstrates a production-ready AI pipeline. It respects the
constraints of modern engineering: speed (Regex), semantic context (BERT), and
deep reasoning (LLM), proving that hybrid systems are the future of enterprise
observability.

Created with ❤️ for the AI Ops Community.
