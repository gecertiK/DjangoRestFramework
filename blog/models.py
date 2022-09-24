from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250, blank=True, default='')
    description = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
