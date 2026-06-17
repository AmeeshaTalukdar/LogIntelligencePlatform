from backend.processors.processor_regex import classify_with_regex
from backend.processors.processor_bert import classify_with_bert
from backend.processors.processor_llm import classify_with_llm

def classify_log(source, log_msg):

    # 1. LLM route
    if source == "LegacyCRM":
        return {
            "label": classify_with_llm(log_msg),
            "method": "llm",
            "confidence": 0.80
        }

    # 2. Regex first
    regex = classify_with_regex(log_msg)
    if regex:
        return {
            "label": regex,
            "method": "regex",
            "confidence": 0.95
        }

    # 3. BERT fallback (SAFE OUTPUT ALWAYS)
    bert = classify_with_bert(log_msg)

    return {
        "label": bert.get("label", "Unclassified"),
        "method": "bert",
        "confidence": float(bert.get("confidence") or 0.0)
    }