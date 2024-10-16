from django.db import models


class Embed(models.Model):
    embedding = models.TextField()  # Store the embedding as a binary field
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.IntegerField()


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    embed = models.ForeignKey(
        Embed,
        on_delete=models.CASCADE,
        related_name="images",
    )
