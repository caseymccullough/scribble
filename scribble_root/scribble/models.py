from django.db import models
class Post (models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title, "by", self.author

class Comment (models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts") 