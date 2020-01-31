from django.db import models

# Create your models here.
class Park(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField()
    photo_url = models.TextField()
    

    def __str__(self):
        return self.name


class Comment(models.Model):
    park = models.ForeignKey(Park, on_delete=models.CASCADE, related_name='comments', null=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField(null=True)
    

    def __str__(self):
        return self.author