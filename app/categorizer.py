from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

categories = ["Food","Travel","Bills","Shopping","Salary","Transfer","Others"]
embeddings = model.encode(categories)

def categorize(desc):

    sim = cosine_similarity(
        model.encode([desc]),
        embeddings
    )

    return categories[sim.argmax()]
