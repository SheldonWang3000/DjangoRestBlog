from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1) 
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    viewed_times = models.IntegerField(default=0)
    abstract = models.TextField(default="Abstract")
    sticky = models.BooleanField(null=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.sticky == True:
            try:
                queryObject = Post.objects.get(sticky=True)
                if queryObject.pk != self.pk:
                    queryObject.sticky = None
                    queryObject.save()
            except Post.DoesNotExist:
                print('no sticky post')
        super(Post, self).save(*args, **kwargs)