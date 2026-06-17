import os
import re
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
def classify_with_llm(log_msg):

    if not groq_api_key:
        return {
            "label": "Unclassified",
            "confidence": 0.5
        }

    client = Groq(api_key=groq_api_key)

    prompt = f"""
Classify the log message into:
(1) Workflow Error
(2) Deprecation Warning

If unsure, return Unclassified.

Return format:
<category>...</category>

Log: {log_msg}
"""

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="deepseek-r1-distill-llama-70b",
        temperature=0.5
    )

    content = chat_completion.choices[0].message.content

    match = re.search(r"<category>(.*?)</category>", content, re.DOTALL)

    label = match.group(1).strip() if match else "Unclassified"

    return {
        "label": label,
        "confidence": 0.75
    }
if __name__ == "__main__":
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))