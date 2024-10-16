from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status, mixins

from .services import embedder
from .serializers import EmbedSerializer, FaceCompareSerializer
from .models import Embed
from .utils import get_similar_person


class EmbedViewSet(ModelViewSet):
    queryset = Embed.objects.all()
    serializer_class = EmbedSerializer

    def create(self, request, *args, **kwargs):
        files = request.FILES.getlist("images")

        if not files:
            return Response(
                {"error": "No images provided."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        embed_instance = embedder(files, request.data["organization"])

        return Response(
            {
                "embed_id": embed_instance.id,
                "organization": embed_instance.organization,
                "embedding": embed_instance.embedding,
                "created_at": embed_instance.created_at,
            },
            status=status.HTTP_201_CREATED,
        )


class FaceCompareViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = FaceCompareSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = request.FILES["image"]
        embed_id, similarity = get_similar_person(
            organization=serializer.data["organization"], image=image
        )

        if embed_id is None:
            return Response(
                {"error": "No matching face found."}, status=status.HTTP_200_OK
            )

        return Response(
            {"embed_id": embed_id, "similarity_score": similarity},
            status=status.HTTP_200_OK,
        )
