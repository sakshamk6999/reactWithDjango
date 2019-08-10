from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title