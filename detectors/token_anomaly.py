# Detect abnormal instructional / imperative language

def token_anomaly(text: str) -> bool:
    imperatives = ["ignore", "override", "system", "must"]
    text = text.lower()
    count = sum(text.count(word) for word in imperatives)
    return count >= 2

