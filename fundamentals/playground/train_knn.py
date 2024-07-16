import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

def load_embedding_model():
    # Generate embeddings for the text descriptions using the pre-trained embedding model
    # For example: 
    # embeddings = [np.mean([embedding_model[word] for word in text.split() if word in embedding_model.vocab], axis=0) for text in text_descriptions]
    glove_file = 'embeddings/glove.6B.50d.txt'
    # Load the embeddings into a dictionary
    embeddings_dict = {}
    with open(glove_file, 'r') as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.asarray(values[1:], dtype='float32')
            embeddings_dict[word] = vector
    # Convert the embeddings dictionary to a NumPy array
    embeddings = np.stack(list(embeddings_dict.values()))
    return embeddings, embeddings_dict

def generate_embeddings(text_descriptions, embedding_dict):
    words = text_descriptions.split()
    word_embeddings = []
    for word in words:
        if word in embeddings_dict:
            word_embeddings.append(embeddings_dict[word])
        else:
            word_embeddings.append(np.zeros(50))  # use a zero vector for out-of-vocabulary words

    text_embedding = np.mean(word_embeddings, axis=0)
    return text_embedding

def train_knn_model(embeddings):
    # Train a KNN model on the embeddings
    knn_model = NearestNeighbors(n_neighbors=10, metric='cosine')
    knn_model.fit(embeddings)
    return knn_model

def predict_closest_documents(knn_model, query_embedding):
    # Use the KNN model to predict the closest documents to the query embedding
    indices = knn_model.kneighbors([query_embedding], n_neighbors=10, return_distance=False)[0]
    return list(indices)

def lookup_original_word(embedding_dict, indices):
    words = [list(embeddings_dict.keys())[i] for i in indices]
    return words

if __name__ == '__main__':
    embeddings, embeddings_dict = load_embedding_model()
    text_descriptions = "In the above code, we first load the GloVe 50-dimensional embeddings file into a dictionary called embeddings_dict"
    query_embeddings = generate_embeddings(text_descriptions, embeddings_dict)
    print(query_embeddings)
    together_embeddings = np.vstack([query_embeddings, embeddings])
    knn_model = train_knn_model(together_embeddings)
    indices = predict_closest_documents(knn_model, query_embeddings)
    print(lookup_original_word(embeddings_dict, indices))
    
    


