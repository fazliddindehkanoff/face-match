import numpy as np

from deepface import DeepFace
from sklearn.metrics.pairwise import cosine_similarity

from .models import Embed, Image


def get_embedding(image_path, model_name="Facenet"):
    embedding = DeepFace.represent(img_path=image_path, model_name=model_name)
    return np.array(embedding)[0]["embedding"]


def compare_embeddings_cosine(embedding1, embedding2):
    if isinstance(embedding1, str):
        print("embedding1 is a string")
        embedding1 = np.fromstring(embedding1.strip("[]"), sep=",")

    if isinstance(embedding2, str):
        print("embedding2 is a string")
        embedding2 = np.fromstring(embedding2.strip("[]"), sep=",")

    similarity = cosine_similarity([embedding1], [embedding2])
    return similarity[0][0]


def check_same_person(embedding1, embedding2, threshold=0.8):
    similarity = compare_embeddings_cosine(embedding1, embedding2)
    return similarity > threshold, similarity


def embedder(files, organization):
    embed_instance = Embed.objects.create(organization=organization)
    embeddings = []

    for uploaded_file in files:
        image_instance = Image.objects.create(
            image=uploaded_file,
            embed=embed_instance,
        )
        embedding = get_embedding(image_instance.image.path)
        embeddings.append(embedding)

    combined_embedding = np.mean(embeddings, axis=0)

    # Convert the numpy array to a comma-separated string
    embed_instance.embedding = ",".join(map(str, combined_embedding))
    embed_instance.save()

    return embed_instance
