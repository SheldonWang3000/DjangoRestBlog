from django.db import models

class Comment(models.Model):
    blog = models.ForeignKey('posts.Post', on_delete=models.CASCADE) 
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField(default="")
    username = models.TextField(default="User")
    avatar = models.URLField(default="https://www.sheldonweb.com/media/default_avatar.png")
    publish_date = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __str__(self):
        return self.content