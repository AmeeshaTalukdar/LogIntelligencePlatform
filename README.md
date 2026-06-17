# LogIntelligencePlatform


Python Version Streamlit Intelligence

An AI-powered log analysis and observability platform that automatically
classifies system logs using a Hybrid Intelligence Pipeline: Regex → BERT → LLM
Fallback.

Transform raw, unstructured logs into actionable insights through machine
learning, semantic understanding, and executive-level analytics.

🚀 Features

🔍 Analysis Modes

  - Single Log Analysis: Real-time classification of individual log strings.
  - Batch Processing: Upload CSV files to classify thousands of logs
    simultaneously.
  - Observability Mode: Live monitoring interface for system health.

🧠 Hybrid AI Pipeline

1.  Regex Engine: Ultra-fast, rule-based classification for high-frequency known
    patterns (e.g., User Actions, Backups).
2.  BERT Semantic Classifier: Uses Sentence Transformers and a trained ML model
    to understand context and intent (e.g., Infrastructure vs. Security).
3.  LLM Fallback: Leverages LLMs (via Groq) for complex, ambiguous, or
    business-specific logs that require deep reasoning.

📊 Insights & Reporting

  - Executive Dashboard: High-level metrics on model usage, confidence trends,
    and label distribution.
  - Debug Mode: Deep-dive into model confidence scores and pipeline routing
    logic.
  - Exportable Reports: Download classification results in CSV or PDF format.

🏗️ Architecture

The system follows a waterfall logic to optimize for speed and cost-efficiency:

graph TD
    A[Log Input] --> B{Regex Match?}
    B -- Yes --> C[Final Classification]
    B -- No --> D[BERT Classifier]
    D --> E{High Confidence?}
    E -- Yes --> C
    E -- No --> F[LLM Fallback]
    F --> C

📁 Project Structure

project-nlp-log-classification/
├── backend/
│   ├── service.py            # Main logic orchestrator
│   └── processors/           # Pipeline layers
│       ├── processor_regex.py
│       ├── processor_bert.py
│       └── processor_llm.py
├── frontend/
│   └── app.py                # Streamlit UI
├── models/
│   └── log_classifier.joblib # Pre-trained BERT weights
├── resources/                # Sample data & outputs
├── shared/
│   └── schemas.py            # Data models
├── requirements.txt
└── README.md

⚙️ Installation

1.  Clone the repository:

    git clone <repository-url>
    cd project-nlp-log-classification

2.  Create a virtual environment:

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.  Install dependencies:

    pip install -r requirements.txt

🔑 Environment Variables

The platform uses Groq for high-speed LLM inference. Create a .env file in the
root directory:

GROQ_API_KEY=your_api_key_here

▶️ Running the Application

Launch the Streamlit dashboard from the project root:

PYTHONPATH=. streamlit run frontend/app.py

Access the UI at: http://localhost:8501

🧪 Sample Logs

| Log Message                               | Expected Label       | Method |
| :---------------------------------------- | :------------------- | :----- |
| `Database connection timeout after 30s`   | Infrastructure Error | BERT   |
| `Multiple failed login attempts detected` | Security Event       | BERT   |
| `User "admin" logged out`                 | User Action          | Regex  |
| `Legacy API /v1/old is deprecated`        | Deprecation Warning  | LLM    |

📈 Future Enhancements

- [ ] Real-time Streaming: Integration with Kafka or AWS Kinesis.
- [ ] Anomaly Detection: Identify outliers that don't fit any known category.
- [ ] Alerting Engine: Slack/Email notifications based on error severity.
- [ ] Database Persistence: Move from CSV to PostgreSQL/Elasticsearch.
- [ ] Multi-tenancy: Role-based access control (RBAC) for different teams.

💡 Project Summary

This project demonstrates a production-grade approach to log observability. By
combining deterministic rules (Regex), semantic ML (BERT), and generative AI
(LLMs), it achieves a balance between high performance, low latency, and deep
intelligence.

It serves as a practical demonstration of modern AI-powered monitoring systems.

Developed for AI-powered Observability & Log Intelligence.
