from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    release_year = models.IntegerField()
    def __str__(self) -> str:
        return self.title
