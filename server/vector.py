from pymilvus import MilvusClient
from pymilvus import model
from pymilvus import connections


# connections.disconnect("vector.db")
# connections.disconnect("vector.db")

# try:
#   print(connections)
#   client = MilvusClient("vector.db")
# except:
#   connections.disconnect("vector.db")
#   client = MilvusClient("vector.db")

# # This should delete the collection upon each backend server restart. 
# # We will want to change this to preserve our embeddings
# # over time. 
# if client.has_collection(collection_name="demo_collection"):
#   client.drop_collection(collection_name="demo_collection")
# client.create_collection(
#     collection_name="demo_collection",
#     # I assume tweeking the dimensionality of vectors is variable we'll need to 
#     # tweek. I expect it's effects reach chunksize, embedding model, similarity search accuracy
#     # and speed 
#     dimension=768,
# )

async def reset_collection(database_name, collection_name):
  client = MilvusClient(database_name)
  if client.has_collection(collection_name=collection_name):
    client.drop_collection(collection_name=collection_name)
  client.create_collection(
      collection_name=collection_name,
      # I assume tweeking the dimensionality of vectors is variable we'll need to 
      # tweek. I expect it's effects reach chunksize, embedding model, similarity search accuracy
      # and speed 
      dimension=768,
  )
  connections.disconnect("vector.db")

# many embedding models to choose from with milvus
# https://milvus.io/docs/embeddings.md
embedding_fn = model.DefaultEmbeddingFunction()

async def embed_and_insert(sentences):
    data = await embed_sentences(sentences)
    insert_result = await insert_data_into_collection(data)
    return insert_result

# embeds sentences into vectors
# creates a list of dictionaries for the vector_db
async def embed_sentences(sentences):
    # here we create a list of embeddings by passing the
    # list of sentences into `embedding_fn.encode_documents`
    #
    vectors = embedding_fn.encode_documents(sentences)

    # creates an array of dictionaries via list comprehension
    # each with id, vector, text, and subject
    data = [
      {"id": i, "vector": vectors[i], "text": sentences[i], "subject":"crucial conversations" }
      for i in range(len(vectors))
    ]

    print("Data has", len(data), "entities, each with fields: ", data[0].keys())
    return data


# inserts data into the collection
async def insert_data_into_collection(data):
    client = MilvusClient("vector.db")
    # collection_name should match the name of the collection you want
    # to insert into... duh
    result = client.insert(collection_name="demo_collection", data=data)

    print(result)
    connections.disconnect("vector.db")
    return result

def text_from_single_query_result(result):
    text = [result['entity']['text'] for result in result[0]]
    return '\n'.join(text)

# for skateboard, it may be wise to limit the queries down to one sentence
# though we can likely test how longer sentences do
async def process_query(query, num_results=5):
    client = MilvusClient("vector.db")
    query_vector = embedding_fn.encode_queries(query)

    result = client.search(
        collection_name="demo_collection",
        data=query_vector,
        # filter=
        limit=num_results,
        output_fields=["text"]
    )

    result_text = text_from_single_query_result(result)
    # print(result_text)
    connections.disconnect("vector.db")
    return result_text