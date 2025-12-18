from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def intent_mismatch(query: str, context: str) -> bool:
    q_emb = model.encode(query, convert_to_tensor=True)
    c_emb = model.encode(context, convert_to_tensor=True)
    similarity = util.cos_sim(q_emb, c_emb).item()
    return similarity < 0.4

