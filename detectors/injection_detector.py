# Prompt Injection Detector

def is_injection(text: str) -> bool:
    keywords = [
        "ignore", "override", "forget",
        "system", "instructions", "must"
    ]
    text = text.lower()
    hits = sum(1 for k in keywords if k in text)
    return hits >= 2

