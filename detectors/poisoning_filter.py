from detectors.injection_detector import is_injection
from detectors.intent_mismatch import intent_mismatch
from detectors.token_anomaly import token_anomaly

def is_poisoned(query: str, context: str) -> bool:
    return (
        is_injection(context)
        or intent_mismatch(query, context)
        or token_anomaly(context)
    )

