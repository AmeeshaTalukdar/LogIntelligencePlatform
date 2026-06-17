import os
import joblib
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "log_classifier.joblib")

model_embedding = SentenceTransformer('all-MiniLM-L6-v2')
model_classification = joblib.load(MODEL_PATH)

def classify_with_bert(log_message):
    embeddings = model_embedding.encode([log_message])

    probabilities = model_classification.predict_proba(embeddings)[0]
    predicted_label = model_classification.predict(embeddings)[0]

    confidence = float(max(probabilities))

    label = predicted_label if confidence >= 0.5 else "Unclassified"

    return {
        "label": label,
        "confidence": confidence
    }


if __name__ == "__main__":
    logs = [
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
        "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
        "System crashed due to drivers errors when restarting the server",
        "Hey bro, chill ya!",
        "Multiple login failures occurred on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer"
    ]
    for log in logs:
        label = classify_with_bert(log)
        print(log, "->", label)
