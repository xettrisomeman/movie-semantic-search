import os
import cohere
import pinecone

from dotenv import load_dotenv

load_dotenv()


COHERE_API = os.getenv("COHERE_API")
PINECONE_API = os.getenv("PINECONE_API")

# init cohere
co = cohere.Client(COHERE_API)

# init pinecone
pinecone.init(PINECONE_API)

## get pinecone index(Vector index)
index_name = "cohere-pinecone-semanticsearch-movie"
index = pinecone.Index(index_name)


# print(index.describe_index_stats())
def movie_search(query: str):
    embed = co.embed(texts=[query], model="large").embeddings
    response = index.query(embed, top_k=5, include_metadata=True)["matches"]
    return response
