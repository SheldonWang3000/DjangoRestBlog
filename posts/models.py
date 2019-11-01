from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    viewed_times = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    # title = models.CharField(max_length=120)
    # slug = models.SlugField(unique=True)
    # image = models.ImageField(upload_to=upload_location, 
    #         null=True, 
    #         blank=True, 
    #         width_field="width_field", 
    #         height_field="height_field")
    # height_field = models.IntegerField(default=0)
    # width_field = models.IntegerField(default=0)
    # content = models.TextField()
    # draft = models.BooleanField(default=False)
    # publish = models.DateField(auto_now=False, auto_now_add=False)
    # read_time =  models.IntegerField(default=0) # models.TimeField(null=True, blank=True) #assume minutes
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    # objects = PostManager()