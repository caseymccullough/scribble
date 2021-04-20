from django.db import models

class Post (models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        result = "Post: " + self.title
        return result
        
class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=100, default="anonymous")
    body = models.CharField(max_length=250, default="undefined")
     
    def __str__(self):
        return self.body[:20] + ". . ."
