from django.conf import settings
from django.db import models
from django.utils import timezone


class Piece(models.Model):
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="portfolio_pieces/", default="portfolio_pieces/wloczykij_WIP.jpg")
    medium = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save

    def __str__(self):
        return self.title
