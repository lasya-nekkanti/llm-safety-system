from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

class Retriever:
    def __init__(self, documents):
        self.documents = documents
        self.embeddings = model.encode(documents, convert_to_tensor=True)

    def retrieve(self, query):
        query_emb = model.encode(query, convert_to_tensor=True)
        similarities = util.cos_sim(query_emb, self.embeddings)[0]
        best_idx = similarities.argmax().item()
        return self.documents[best_idx]

