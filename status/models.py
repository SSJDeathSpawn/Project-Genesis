from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True)
    def __str__(self):
        return self.title

class Reply(models.Model):
    class Meta:
        verbose_name_plural = "replies"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.text
