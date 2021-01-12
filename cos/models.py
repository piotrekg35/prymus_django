from django.db import models
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    short_description = models.TextField()
    published_at = models.DateTimeField()
    cover=models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.title