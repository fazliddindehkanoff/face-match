# FaceMatch

FaceMatch is an AI-powered Django application that uses the DeepFace library to find facial similarities by comparing image embeddings. The project offers two endpoints: one for saving user images as embeddings and another for comparing a given image against saved embeddings to find a matching face. This tool is ideal for applications such as identity verification, duplicate detection, or face matching in various organizational contexts.

## Features

- **Facial Embedding Generation**: Converts uploaded images into numerical embeddings using deep learning models.
- **Face Similarity Comparison**: Compares new images with stored embeddings to find similar faces, providing a similarity score.
- **Multiple Model Support**: Leverages various models like Facenet, VGG-Face, and others from the DeepFace library.
- **Organizational Segmentation**: Manages embeddings on a per-organization basis for better data isolation.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Machine Learning**: DeepFace for facial recognition
- **Database**: SQLite (default) or any other supported by Django ORM

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/FaceMatch.git
    cd FaceMatch
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the server**:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### 1. Embedding Endpoint
   - **URL**: `/api/embeddings/`
   - **Method**: `POST`
   - **Description**: Saves images for a specific organization and generates embeddings.
   - **Request**:
     ```json
     {
       "organization": "string",
       "images": [file]
     }
     ```
   - **Response**:
     ```json
     {
       "embed_id": "integer",
       "organization": "string",
       "embedding": "string",
       "created_at": "datetime"
     }
     ```

### 2. Face Comparison Endpoint
   - **URL**: `/api/face-compare/`
   - **Method**: `POST`
   - **Description**: Compares an uploaded image with the saved embeddings for a specific organization.
   - **Request**:
     ```json
     {
       "organization": "string",
       "image": file
     }
     ```
   - **Response**:
     ```json
     {
       "embed_id": "integer",
       "similarity_score": "float"
     }
     ```

## Project Structure

- **views.py**: Contains API views for embedding generation and face comparison.
- **services.py**: Handles core logic for embedding generation, comparison, and utility functions for processing images.
- **utils.py**: Provides helper functions for saving images, embedding processing, and finding similar faces.
- **models.py**: Defines database models for storing embeddings and associated image metadata.
- **serializers.py**: Serializes input data for the API endpoints.

## Example Usage

### Save Embeddings
To save embeddings for an organization, send a `POST` request to `/api/embeddings/` with the following body:
```bash
curl -X POST http://localhost:8000/api/embeddings/ \
-F "organization=MyOrganization" \
-F "images=@/path/to/image1.jpg" \
-F "images=@/path/to/image2.jpg"
```
### Compare Faces
To compare a face, send a POST request to /api/face-compare/:

```bash
curl -X POST http://localhost:8000/api/face-compare/ \
-F "organization=MyOrganization" \
-F "image=@/path/to/query_image.jpg"
```

## Contributing

Feel free to open issues or submit pull requests for improvements. Contributions to enhance functionality or fix bugs are always welcome.