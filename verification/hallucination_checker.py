from sentence_transformers import SentenceTransformer, util

# Load a lightweight sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def check_hallucination(model_output: str, reference_fact: str, threshold: 
float = 0.9) -> bool:
    """
    Detects hallucination by checking semantic similarity between
    model output and a trusted reference fact.

    Returns True if hallucination is detected.
    """
    output_emb = model.encode(model_output, convert_to_tensor=True)
    ref_emb = model.encode(reference_fact, convert_to_tensor=True)

    similarity = util.cos_sim(output_emb, ref_emb).item()
    return similarity < threshold

