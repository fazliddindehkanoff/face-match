import os
from .models import Embed
from .services import get_embedding, check_same_person


def save_image(image, directory="images"):
    """
    Saves an uploaded image to the specified directory.

    Args:
        image: The uploaded image file.
        directory: The directory where the image will be saved.

    Returns:
        The path to the saved image file.
    """
    os.makedirs(directory, exist_ok=True)  # Ensure the directory exists
    image_path = os.path.join(directory, image.name)
    with open(image_path, "wb+") as destination:
        for chunk in image.chunks():
            destination.write(chunk)
    return image_path


def find_similar_embed(organization, embedded_image):
    """
    Finds a similar embedding for the given organization.

    Args:
        organization: The organization to filter embeddings.
        embedded_image: The embedding to compare against.

    Returns:
        A tuple of (embed_id, similarity score) if a match is found,
        otherwise (None, 0).
    """
    for embed in Embed.objects.filter(organization=organization):
        is_match, similarity = check_same_person(
            embed.embedding,
            embedded_image,
        )
        if is_match:
            return embed.id, round(similarity * 100, 2)

    return None, 0


def get_similar_person(organization, image):
    """
    Finds a similar person embedding for the given organization and image.

    Args:
        organization: The organization to filter embeddings.
        image: The uploaded image to find a similar person for.

    Returns:
        A tuple of (embed_id, similarity score) if a match is found,
        otherwise (None, 0).
    """
    image_path = save_image(image)
    embedded_image = get_embedding(image_path)
    return find_similar_embed(organization, embedded_image)
